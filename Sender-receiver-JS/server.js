// archivo: server.js

var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

io.on('connection', function(socket){
  console.log('Un cliente se ha conectado');

  socket.on('mensaje_python', function(msg){
    // Retransmitir el mensaje a todos los clientes
    io.emit('mensaje_servidor', msg);
  });

  socket.on('disconnect', function(){
    console.log('El cliente se ha desconectado');
  });
});

http.listen(3000, function(){
  console.log('Escuchando en *:3000');
});
