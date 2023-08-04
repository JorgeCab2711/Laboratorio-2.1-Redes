#clien.py

# archivo: cliente.py

#Se implemento Hamming para la detección de errores.

import socketio

sio = socketio.Client()


def calcRedundantBits(m):
    for i in range(m):
        if(2**i >= m + i + 1):
            return i

def posRedundantBits(data, r):
    j = 0
    k = 1
    m = len(data)
    res = ''
    
    #Si le posicion es potencia de 2, se agrega un 0
    
    for i in range(1, m + r+1):
        if(i == 2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1
            
    return res[::-1]

def hammingEncode(mensaje):
    # Convert string to binary
    data = ''.join(format(ord(i), '08b') for i in mensaje)
    
    # Calculate redundant bits
    r = calcRedundantBits(len(data))
    
    # Determine the positions of Redundant Bits
    arr = posRedundantBits(data, r)
    
    # Return encoded message
    return arr

@sio.event
def connect():
    print("Conectado al servidor!")
    while True:
        user = 'Ale'
        mensaje = input("> ")
        
        if mensaje != "":
            # Apply Hamming encoding to the message
            encodedMensaje = hammingEncode(mensaje)
            sio.emit('mensaje_python', f'{user}: {encodedMensaje}')

        if mensaje == "/exit":
            sio.emit('mensaje_python', f"{user} se ha desconectado del servidor...")
            break

@sio.event
def mensaje_servidor(msg):
    print("\n",msg)

sio.connect('http://192.168.1.42:3000')
