var express = require('express');
var router = express.Router();
var BlogModel = require('../models/blogpost');

//this runs when page is loaded. Not on another method
router.get('/',function(req,res,next){
  //rout to retrieve data
  BlogModel.find({},'',function( err,posts ){
    if(err) console.error('Error gettting posts: ', err);
    //converts this js into a json response which is sent to client
    res.json(posts);
  });
});

//this will not run until a post method is called
router.post('/',function(req,res,next){

  var postInfo = {
    title: req.body.title,
    content: req.body.content,
    author: req.body.author
  };

  var newPost = new BlogModel(postInfo);

  newPost.save(function(err,success){
    res.redirect('/');
  });
});

router.put('/',function(req,res,next){
  var id = req.body.id;
  var updateInfo = {
    title: req.body.title,
    content: req.body.content
  };

  BlogModel.findByIdAndUpdate(id, updateInfo,function(err,post){
    if(err) console.log(err);

    res.send('SUCCESS!');
  });
});

router.delete('/',function(req,res,next){
  var id = req.body.id;
  BlogModel.findByIdAndRemove(id, function(err,post){
    if(err) console.error(err);

    res.send('SUCCESS');
  });
});



module.exports = router;
