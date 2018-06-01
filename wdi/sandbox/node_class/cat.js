var cat = require('cat');

//this var is set to whatever is exported from this file (calculator function)
var whatever_we_want_to_call_it = require('./my_module');

//here we call the adder function through the variable
console.log(whatever_we_want_to_call_it.add(1,2) );

//returns google
// cat('http://www.google.com', console.log);
