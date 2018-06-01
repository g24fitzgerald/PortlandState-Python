import React, { Component } from 'react';
import {IndexLink, Link} from 'react-router';
import Home from './components/Home';
import logo from './logo.svg';
import './App.css';
import { Button } from 'react-bootstrap';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <ul>
            <li><IndexLink to="/" activeClassName="active"> Home </IndexLink></li>
            <li><Link to="/about" activeClassName="active"> About </Link></li>
            <li><Link to="/background" activeClassName="active"> Background </Link></li>
          </ul>
        </div>

        <div className="content">
          {this.props.children}
        </div>
      </div>
    );
  }
}

export default App;
