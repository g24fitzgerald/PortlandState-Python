//this code tells the browser to start loading code after the page is loaded

//ex, target the block after the page is loaded.
$(document).ready(function(){

  $(".left").click(function(event){
    $('.block').removeClass('afterClickeCenter').removeClass('afterClickedRight').addClass('afterClickedLeft');
  });
  $(".center").click(function(event){
    $('.block').removeClass('afterClickedLeft').removeClass('afterClickedRight').addClass('afterClickedCenter');
  });
  $(".right").click(function(event){
    $('.block').removeClass('afterClickedLeft').removeClass('afterClickedCenter').addClass('afterClickedRight');
  });
});
