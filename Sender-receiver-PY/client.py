import socketio
from translator import *
sio = socketio.Client()

def calculate_hamming(binary):
    n = len(binary)
    r = 0

    # Calculamos el número de bits de redundancia requeridos
    while 2**r < n + r + 1:
        r += 1

    # Código Hamming inicializado con ceros
    hamming_code = [0]*(n + r)

    # Colocamos los bits de la trama en las posiciones correctas
    j = 0
    for i in range(1, n + r + 1):
        if i != 2**j:
            hamming_code[i-1] = int(binary[-1])
            binary = binary[:-1]
        else:
            j += 1

    # Calculamos los bits de redundancia
    j = 0
    for i in range(1, n + r + 1):
        if i == 2**j:
            k = i
            total = 0
            while k <= n + r:
                slice_ = hamming_code[k-1 : k-1+i]
                total += sum(slice_)
                k += 2*i
            hamming_code[i-1] = total % 2
            j += 1

    return ''.join(map(str, reversed(hamming_code)))

def decode_hamming(hamming_code):
    hamming_code = list(map(int, reversed(hamming_code)))
    n = len(hamming_code)
    r = 0

    # Calculamos el número de bits de redundancia
    while 2**r < n + 1:
        r += 1

    # Comprobamos los bits de redundancia
    error_pos = 0
    for i in range(r):
        k = 2**i
        total = 0
        while k <= n:
            slice_ = hamming_code[k-1 : k-1+2**i]
            total += sum(slice_)
            k += 2*2**i
        if total % 2 > 0:
            error_pos += 2**i

    # Corregimos el error, si se encontró alguno
    if error_pos > 0:
        hamming_code[error_pos-1] = 1 - hamming_code[error_pos-1]

    # Eliminamos los bits de redundancia para obtener la trama original
    j = 0
    original = ''
    for i in range(1, n + 1):
        if i != 2**j:
            original += str(hamming_code[i-1])
        else:
            j += 1

    return original, error_pos

@sio.event
def connect():
    print("Conectado al servidor!")
    while True:
        user = 'Ale'
        mensaje = input("> ")
        
        if mensaje != "":
            # Convertir el mensaje a binario
            binary = string_to_binary(mensaje)
            # Calcular el código Hamming
            hamming_code = calculate_hamming(binary)
            # Enviar la trama original
            sio.emit('mensaje_python', f'{user} - Trama original: {binary}')
            # Enviar el mensaje con el código Hamming
            sio.emit('mensaje_python', f'{user} - Código Hamming: {hamming_code}')
            # Decodificar el código Hamming
            original, error_pos = decode_hamming(hamming_code)
            # Enviar la trama original decodificada
            sio.emit('mensaje_python', f'{user} - Trama original decodificada: {original}')
            # Si se encontró un error, enviar la posición del bit corregido
            if error_pos > 0:
                sio.emit('mensaje_python', f'{user} - Se encontró un error y se corrigió en la posición: {error_pos}')

        if mensaje == "/exit":
            sio.emit('mensaje_python', f"{user} se ha desconectado del servidor...")
            break
@sio.event
def mensaje_servidor(msg):
    print("\n",msg)

sio.connect('http://192.168.1.42:3000')
