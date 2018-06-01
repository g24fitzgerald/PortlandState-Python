var express = require('express');

//Create our app
var app = express();

//tell which folder we want to server
app.use(express.static('public')); //lets you add functionality to app

app.listen(3000, function(){
  console.log('Express server is up on port 3000')
}); 
