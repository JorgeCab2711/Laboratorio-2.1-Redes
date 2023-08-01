// file: client.js
const io = require('socket.io-client');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const sio = io.connect('http://192.168.1.42:3000');
const user = 'Jorge';

sio.on('connect', () => {
    console.log("Conectado al servidor!");
    messageLoop();
});

sio.on('mensaje_servidor', (msg) => {
    console.log("\n", msg);
});

function messageLoop() {
    rl.question("> ", (mensaje) => {
        sio.emit('mensaje_python', `${user}: ${mensaje}`);
        if (mensaje === "/exit") {
            sio.emit('mensaje_python', `${user} se ha desconectado del servidor...`);
            rl.close();
            sio.disconnect();
        } else {
            messageLoop();
        }
    });
}
