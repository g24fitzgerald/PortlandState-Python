
$(document).ready(function(){

  $('.desc').text('This is a great practice app');

  //targets all a elements upon clicking
  $('a').on('click', function(event){

    //
    var linkText = $(this).text();
    alert("This is the linkText test: " + linkText);

    //h3
    $('.destination').text(linkText);
    //event is an object that the browser creates. We see it in the top function
    event.preventDefault();
    //sets variable to the previously coded href attribute
    var oldHref = $(this).attr('href');
    //hilariously tells viewer to enjoy the site they think they're going to
    alert('Enjoy ' + oldHref);

    //targets the a element clicked and redirects attribute href to point to bing
    $('this').attr('href', 'http://www.bing.com/')
  });

});
