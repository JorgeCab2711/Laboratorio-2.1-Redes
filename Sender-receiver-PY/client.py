# archivo: cliente.py

import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Conectado al servidor!")
    while True:
        mensaje = input("Ingresa un mensaje para enviar: \n> ")
        sio.emit('mensaje_python', mensaje)
        if mensaje == "/exit":
            print("Desconectando del servidor...")
            sio.emit('mensaje_python', "Ale se ha desconectado del servidor...")
            break

@sio.event
def mensaje_servidor(msg):
    print("Mensaje del servidor: " + msg)

@sio.event
def Mensaje_server(msg):
    print("Mensaje del servidor: " + msg)

sio.connect('http://192.168.56.1:3000')
