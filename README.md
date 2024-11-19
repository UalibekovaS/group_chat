# Group Chat Application (WebSockets with Flask)

A real-time group chat application created using **WebSockets** and **Flask**, which allows users to:
- Create new chatrooms
- Join existing chatrooms
- Send messages in the chatrooms

## Features:
- **Create Chatrooms**: Users can create a new chatroom by providing a room name.
- **Join Existing Chatrooms**: Users can select and join any available chatroom from the list.
- **Send Messages**: Once in a chatroom, users can send and receive real-time messages.

## Technologies Used:
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Real-time Communication**: WebSockets (using Flask-SocketIO)
- **Web Server**: Flask

## How to Set Up Locally:

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/group-chat.git
```
### 2. Install Dependencies
Navigate to the project directory and install the necessary dependencies:
```bash
pip install flask flask-socketio
```
### 3. Run the Application
Start the Flask server:
```bash
python server.py
```
The server will start running on http://localhost:5000.
### 4. Open the Chat Application
Open a web browser and navigate to http://localhost:5000 to start using the chat application.

![image](https://github.com/user-attachments/assets/81de3672-0b13-4e07-9d7e-7c8faf5a1ac0)
![image](https://github.com/user-attachments/assets/e94510fc-a15e-4aa5-91ee-349fd997533f)

