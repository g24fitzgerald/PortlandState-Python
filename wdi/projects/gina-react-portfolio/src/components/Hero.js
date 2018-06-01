import React, { Component } from 'react';
import logo from '../images/gf.png';

class Hero extends Component {
  render() {
    return (
      <div className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1 className="hero-header">Gina Fitzgerald</h1>
      </div>
    )
  }
}

export default Hero;
