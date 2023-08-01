# archivo: cliente.py

import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Conectado al servidor!")
    while True:
        user = 'Ale'
        mensaje = input("> ")
        
        if mensaje != "":
            sio.emit('mensaje_python', f'{user}: {mensaje}')

        if mensaje == "/exit":
            sio.emit('mensaje_python', f"{user} se ha desconectado del servidor...")
            break

@sio.event
def mensaje_servidor(msg):
    print("\n",msg)

sio.connect('http://192.168.1.42:3000')
