import React, { Component } from 'react'
import './App.css'
import List from './components/list.js'
import Form from './components/form.js'


class App extends Component {
  render() {
    return (
      <div className="App">
        <h1 className="heading">Worlds best todo app</h1>
        <List />
        <Form />
      </div>
    );
  }
}

export default App
