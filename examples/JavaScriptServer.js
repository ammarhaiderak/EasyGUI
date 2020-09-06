const net = require('net');

const server = net.createServer((socket) => {
  console.log('Connection from', socket.remoteAddress, 'port', socket.remotePort);

  socket.on('data', (buffer) => {
    //console.log('Request from', socket.remoteAddress, 'port', socket.remotePort);
    console.log('Recieved:',`${buffer.toString('utf-8')}\n`);
    var msg=require('prompt');
    msg.start();
    
    msg.get(['command'], function (err, result) {
    //
    // Log the results.
    //
    //console.log('Command-line input received:');
    console.log('  command: ' + result.command);
    socket.write(`${result.command}\n`);
    
  });
    
  });
  socket.on('Exit', () => {
    console.log('Closed', socket.remoteAddress, 'port', socket.remotePort);
  });
});

//server.maxConnections = 20;
server.listen(4002); 
