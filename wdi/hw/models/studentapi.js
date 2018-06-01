var mongoose = require('mongoose');


var schema = new mongoose.Schema({
  name: { type: String, required: true },
  age: Number
});

//defines what collection it goes to by whats in the parenthases. Use uppercase
var studentModel = mongoose.model('Student', schema);

// Make this available to our other files
module.exports = studentModel;
