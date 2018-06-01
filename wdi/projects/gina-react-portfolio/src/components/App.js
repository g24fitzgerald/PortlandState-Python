import React, { Component } from 'react';
import '../css/App.css';
import NavBar from './NavBar';
import Hero from './Hero';
import Biography from './Biography';
import Footer from './Footer';

class App extends Component {
  render() {
    return (
      <div className="App">
        <NavBar />
        <Hero />
        <div className="content">
          {this.props.children || <Biography />}
        </div>
        <Footer />
      </div>
    );
  }
}

export default App;
