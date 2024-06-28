# 13. Implement notifications in a Flask app using websockets to notify users of updates.

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow all origins for development

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# SocketIO event handler - client sends a message
@socketio.on('send_notification')
def handle_send_notification(data):
    print('Sending notification:', data)
    emit('receive_notification', data, broadcast=True)  # Broadcast the notification to all connected clients

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000, allow_unsafe_werkzeug=True)
