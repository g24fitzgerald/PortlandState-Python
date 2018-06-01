$(document).ready(function(){
  $('#getImage').on('click', getPicture);
  $('#getText').on('click', getJ);

  function getPicture(e){
    var request = $.ajax({
      url: 'http://www.splashbase.co/api/v1/images/random',
      method: 'GET'
    });

    request.done(function(response){

      // $('#email').html(response.text);
      $('#picture').attr('src', response.url);

    });
    request.fail(function(error){
      //the fail parameter will be called if there is an error. The string error
      console.log('there was an error: ', error);
    });

  };
  function getJ(e){
    var request = $.ajax({
      url: 'http://hipsterjesus.com/api',
      method: 'GET'
    });

    request.done(function(response){

      $('#email').html(response.text);
    });
    request.fail(function(error){
      console.log('there was an error: ', error);
    });
  }
});
