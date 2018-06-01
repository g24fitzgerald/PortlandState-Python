import React, { Component } from 'react'; //object plucking. want compenent property from react object. shortcut for ES6
import logo from './logo.svg'; //declare to use on line 30
import './App.css';

class App extends Component { //extending is a way of inheriting functionality from base class (named component App). Component base comes from react library
  constructor(props) { //constructor functions always run when object is created (here its when a component is created)
    super(props); //function recievs props, super accesses the parent component class, and passes its props to the new component

    this.state = { //the only time we set state directly without setState({})
      clicks: 0
    };
  }

  handleClick() { //create funciton to increment this.state.clicks
    let currentValue = this.state.clicks;
    //never access state variable directly with this.state.clicks = 10. must use setState({})
    this.setState({ //!don't have to manipulate DOM, just updated the value of the state of the component! UI changes
      clicks: ++currentValue  //need to increment before not after currentValue
    });
  }

  render() { //Every component has one function: to render. needs to return JSX
    return ( //use () when it's multi-line JSX
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <p>
          <button onClick={ this.handleClick.bind(this) }>Click me</button>
          Number of clicks: {this.state.clicks}
        </p>
      </div>
    );
  }
}
//when App.js is called, they receive the App class defined at line 5
export default App;
