

var express = require('express');
var router = express.Router();
var TwitterClient = require('easy-twitter');
//_Create a new Twitter app and get the keys needed
//we want to put it in this rout instead of the app.js because it will only be USED in twitterapi.js
var twitter = new TwitterClient({
 consumer_key: process.env.CONSUMER_KEY, //proccess obj exists within node that holds info about many things including the key: value pairs in .env file
 consumer_secret: process.env.CONSUMER_SECRET,
 access_token_key: process.env.ACCESS_TOKEN_KEY,
 access_token_secret : process.env.ACCESS_TOKEN_SECRET
});

//path module for grabbing images
var path = require('path');

router.post('/tweetmessage', function(req, res, next){
  //Add our message to codezillas twitter page
  var message = req.body.tweet;

  twitter.tweet(message)
    .then(function(data){
      //Tweet was successfully posted
      res.send('Tweet was successfully posted');
    })
    .catch(function(error){
      console.error(error);
      res.send('no bueno senor');
    });

});

router.post('/tweetmedia', function(req, res, next){
  //rout used to tweet message w/ img to codezillas twitter page
  var message = req.body.tweet;
  var imgUrl = path.join(__dirname, '../public/images/') + req.body.img;
  // var imgUrl = __dirname + '/../public/images/' + req.body.img; //dirname is a premade placement variable (a string of the exact location of this file)
  twitter.uploadMedia(message, imgUrl).then(function(data){
    res.send('Tweet media was successfully posted');
  }).catch(function(error){
    console.error(error);
    res.send('there was an error with tweet media');
  });
});
//when we go to a routs url, we're going to send something from our server
//specified here
module.exports = router;
