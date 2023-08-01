# archivo: server.py
from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print('Un cliente se ha conectado')

@socketio.on('mensaje_python')
def handle_mensaje_python(msg):
    print(msg)
    # Retransmitir el mensaje a todos los clientes excepto al emisor
    socketio.emit('mensaje_servidor', msg, skip_sid=request.sid)

@socketio.on('disconnect')
def handle_disconnect():
    print('El cliente se ha desconectado')

if __name__ == '__main__':
    print('Servidor corriendo en *:3000')
    socketio.run(app, host='0.0.0.0', port=3000)
