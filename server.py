from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "groupchattingsabina"
socketio = SocketIO(app)

rooms = {}
def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        if code not in rooms:
            break
    return code


@app.route("/", methods=["POST", "GET"])
def home():
    session.clear()
    code = None
    name = None
    if request.method == "POST":
        name = request.form.get("name")
        join = request.form.get("join", False)
        create = request.form.get("create", False)
        if create != False:
            room = generate_unique_code(5)
            rooms[room] = {"members": 0, "messages": []}
        session["room"] = room
        session["name"] = name
        return redirect(url_for("room"))
    existing_rooms = list(rooms.keys())
    return render_template("home.html", existing_rooms=existing_rooms)


@app.route("/room", methods=["GET"])
def room():
    room = session.get("room")
    name = session.get("name")
    join_room = request.args.get("room")
    join_name = request.args.get("name")
    if join_room is not None and join_room in rooms:
        # User is joining an existing room, load messages for this room
        room = join_room
        name = join_name
        session["room"] = room
        session["name"] = name
    if room is None or room not in rooms:
        return redirect(url_for("home"))
    return render_template("room.html", code=room, messages=rooms[room]["messages"])

@socketio.on("message")
def message(data):
    room = session.get("room")
    if room not in rooms:
        return

    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")


@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not room:
        return
    if room not in rooms:
        leave_room(room)
        return
    join_room(room)
    send({"name": name, "message": "has entered the room"}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")


@socketio.on("disconnect")
def disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]

    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")


if __name__ == "__main__":
    socketio.run(app, debug=True)
