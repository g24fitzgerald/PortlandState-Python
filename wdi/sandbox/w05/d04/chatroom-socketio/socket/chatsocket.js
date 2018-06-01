module.exports = function(server){
  //set up io that passes server io to it
  var io = require('socket.io')(server);

  //1. listen 2.emit (send things out for certain listeners)

  //create a listener for the event 'connect'.
  io.on('connect',function(socket){   //When the connect event fires, we run the specified function
    console.log('Backend Socket is connected!');
    socket.emit('connected', 'Hello from the backend!'); //here we emit our event we named 'connected' and perform function

    socket.on('send message', function(message){
      console.log('message', message);
      io.emit('message', message);
    });
  });

};
