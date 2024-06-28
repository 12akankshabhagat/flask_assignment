#  12. Build a Flask app that updates data in real-time using WebSocket connections.
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
@socketio.on('send_update')
def handle_send_update(data):
    print('Received update:', data)
    emit('receive_update', data, broadcast=True)  # Broadcast the data to all connected clients

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001, allow_unsafe_werkzeug=True)  # Changed port to 5001
