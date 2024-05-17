from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import pyshark
from threading import Thread
import sys

# Create the Flask app and configure it with a secret key
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Use a secure, random secret in production
socketio = SocketIO(app)

# Function to capture packets and emit the data to the client
def capture_and_emit():
    cap = pyshark.LiveCapture(interface='eth0')
    protocol_data = {}

    # Continuously capture packets and update the data
    for packet in cap.sniff_continuously():
        try:
            protocol = packet.highest_layer
            length = int(packet.length)
            if protocol in protocol_data:
                protocol_data[protocol] += length
            else:
                protocol_data[protocol] = length

            # Emit the updated data for each protocol
            emit_data = [{'protocol': p, 'bandwidth': bw} for p, bw in protocol_data.items()]
            socketio.emit('new_data', emit_data)

        # Handle exceptionsls
        except AttributeError:
            continue

# Route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Event handler for client connection
@socketio.on('connect')
def on_connect():
    print("Client connected")
    thread = Thread(target=capture_and_emit)
    thread.daemon = True
    thread.start()

# Event handler for client disconnection
if __name__ == '__main__':
    # This allows unsafe Werkzeug in development but should be removed for production
    socketio.run(app, debug=True, host='0.0.0.0', allow_unsafe_werkzeug=True)
