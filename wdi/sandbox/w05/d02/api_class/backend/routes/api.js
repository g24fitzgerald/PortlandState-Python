var express = require('express');
var router = express.Router();

var Playlist = require('../models/playlist');
var Song = require('../models/song');
var PlaylistSong = require('../models/playlist_song');

//get all playlists for a user
router.get('/playlists', function(req, res, next) {
  //auth0's way of handling user
  // var userId = req.user.aud;
  // Find ALL documents that match the criteria passed, only return the "name" and "favorite" fields

  Playlist.find({ userId: req.user.aud }, '', function(err, playlists) {
    if (err) console.log(err);
    console.log(playlists);

    res.json(playlists);
  });
});


//get a single playlist by id
router.get('/playlists/:playlistId', function(req, res){
  // Find a single document by the unique ID
  Playlist.findById(req.params.playlistId, '', function(err, playlist) {
    if (err) console.log(err);

    //need to find songs to put in playlist (by accessing from playlistSong)
    //give me every record where playlist song has this playlist id
    PlaylistSong.find({playlist:req.params.playlistId}, 'song')
      //go to playlist with given id, loop through songs ids
     .populate('song') //in my songs collection find the song id that belong in playlist
     .exec(function(err, results){
       if (err) console.error(err);

       //create new array by looping through existing array to restructure in a new array-use map
       var mappedResults = results.map(function(val){
          return val.song;
       });

       res.json({
         playlist: playlist,
         songs: results
       });
     });

  });
});

//create (post) a single playlist for user
router.post('/playlists', function(req, res){
  var userId = req.user.aud;
  var title = req.body.title;

  console.log(title, userId);

  if (!title){
    res.status(400).send('Missing title');
  }
  var newPlaylist = new Playlist({
        title: title,
        userId: userId,
        created: new Date()
    });
  newPlaylist.save(function(err, playlist){
    if (err) console.error(err);
    res.json(playlist);
  });
});

//remove (delete) a playlist
router.delete('/playlists/:playlistId', function(req, res){
  // Find a document by the unique _id field
  Playlist.findByIdAndRemove(req.params.playlistId, function(err) {
    if (err) console.log(err);

    res.json({
      removed: req.params.playlistId
    });
  });
});

//add (post) a song to an existing playlist
router.post('/playlists/:playlistId/songs', function(req, res){
  var artist = req.body.artist;
  var title = req.body.title;
  var playlistId = req.params.playlistId;
  var songId = req.body.spotifySongId;

  if(!artist || !title || !songId) {
    res.status(400).send('Missing parameters');
  }
  // Setup stuff
  var query = { /* query */
    spotifySongId: songId,
    artist: artist,
    title: title
  },
    update = { expire: new Date() },
    options = { upsert: true, new: true, setDefaultOnInsert: true };

  // Find the document
  Song.findOneAndUpdate(query, update, options, function(error, song) {
      if (error) console.error(error);
      console.log(song);

      var newPlaylistSong = new PlaylistSong({
        song: song._id,
        playlist: playlistId
      });
      newPlaylistSong.save(function(err){
        if (err) console.error(err);

        res.json(song);
      })
  });
});

//remove (delete) a song from existing playlist
router.delete('/playlists/:playlistId/songs/:songId', function(req, res){
  res.json({
    playlistId: req.params.playlistId,
    songId: req.params.songId
  });
});
module.exports = router;
