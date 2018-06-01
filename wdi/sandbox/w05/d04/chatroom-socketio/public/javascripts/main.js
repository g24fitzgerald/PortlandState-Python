var socket = io();

function persistChat(htmlString){
  //if chatlog exists in browser storage
  localStorage.setItem('chatlog', htmlString);
};

function setUpSocket(){

  socket.on('connected', function(greeting){
    console.log(greeting);
  });
  socket.on('message', function(message){ //when socket is on and somethign called message happens, do this
    $('#messages').prepend([
      '<li>', message, '</li>'
    ].join('')); //when we want to add a big block of html, prepend an array with .join
    //pass in html in ul
    persistChat( $('#messages').html() );
  });
};

function addEventListeners(){
  $('#sendmessage').on('submit', function(e){
    e.preventDefault();
    //HERE's WHERE WE GET THE VAL OF INPUT!!! REMEMBER THIS
    var $message = $(this).find('#m');

    socket.emit('send message', $message.val());
    //empty the input
    $message.val('');
  });
};
function getChat(){
  if (localStorage.getItem('chatlog')){
    $('#messages').html(localStorage.getItem('chatlog'));
  }
}
//main function calls event listeners, and binds sockets together
function main(){
  addEventListeners();
  setUpSocket();
  getChat();
};

//when page is loaded, call main function
$(document).ready(main);
