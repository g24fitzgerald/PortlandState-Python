var mongoose = require('mongoose');

var schema = new mongoose.Schema({
  title: { type: String, required: true },
  userId: { type: String, required: true },
  created: Date
});

var model = mongoose.model('Playlist', schema);

// Make this available to our other files
module.exports = model;
