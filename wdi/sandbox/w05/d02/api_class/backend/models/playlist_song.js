//connect songs to playlists (setting up associations)
var mongoose = require('mongoose');
var Schema = mongoose.Schema,
  ObjectId = Schema.ObjectId;

var schema = new mongoose.Schema({
  playlist: {
    type: ObjectId,
    required: true,
    ref: 'Playlist',
    index: true
  },
  song: {
    type: ObjectId,
    required: true,
    index: true
  },
  created: Date
});

var model = mongoose.model('PlaylistSong', schema);

// Make this available to our other files
module.exports = model;
