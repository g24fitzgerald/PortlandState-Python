import $ from 'jquery' //weback lets us import: says go find jquery module in node modues and use the $

(function(){ //self calling anonymous function

  class Game { //how we make objects in ES6 in regular you define a constructor as a function

    constructor(){ //when instantiated, run this
      this.playerScore = 0;
      this.computerScore = 0;
      this.hands = ['rock', 'paper', 'scissors'];
    }

    winGame(playerHand, computerHand){
      this.playerScore+=1;
      $('.roundOutcome').text(`${playerHand} beats ${computerHand}, you win!`);
      $('.playerscore .score').text(this.playerScore);
    }

    loseGame(){
      this.computerScore+=1;
      $('.roundOutcome').text(`${computerHand} beats ${playerHand}, you win!`);
      $('.computerscore .score').text(this.computerScore);
    }
    tieGame(){
      $('.roundOutcome').text(`Tie Game!`);
    }
    computerRoll(){
      //random number between 0 and 2
      let randomNumber = Math.floor((Math.random() * 3));
      return this.hands[randomNumber];
    }
    decideWinner(){
      if(playerHand === 'rock'){
        //determine computers hand
        if (computerHand === 'paper') {
          //lose
          this.loseGame(playerHand, computerHand);
        }else if (computerHand === 'scissors') {
          //win
          this.winGame(playerHand, computerHand);
        } else {
          //tie
          this.tieGame(playerHand, computerHand);
        }

      } else if (playerHand === 'paper'){
        if (computerHand === 'scissors') {
          //lose
          this.loseGame(playerHand, computerHand);
        }else if (computerHand === 'rock') {
          //win
          this.winGame(playerHand, computerHand);
        } else {
          //tie
          this.tieGame(playerHand, computerHand);
        }
      } else if (playerHand === 'scissors'){
        if (computerHand === 'rock') {
          //lose
          this.loseGame(playerHand, computerHand);
        }else if (computerHand === 'paper') {
          //win
          this.winGame(playerHand, computerHand);
        } else {
          //tie
          this.tieGame(playerHand, computerHand);
        }
      }
    }
    playGame(playerHand){
      this.decideWinner(playerHand, this.computerRoll());
    }

  }
  function addEventListeners(){
    let theGame = new Game();
    $('.gameButtons .rock').on('click', (e)=>{
      theGame.playGame('rock');
    });
    $('.gameButtons .paper').on('click', (e)=>{
      theGame.playGame('paper');
    });
    $('.gameButtons .scissors').on('click', (e)=>{
      theGame.playGame('scissors');
    });
  }
  function main() {
    addEventListeners();
  }

  $(document).ready(main);
})();
