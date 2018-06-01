import React, { Component } from 'react'
import firebase from '../fb_configs.js'

class Form extends Component {
  constructor(props){
    super(props)
    this.state = {
      formText: ""
    }
  }
  sendTodo(e){
    e.preventDefault()
    firebase.ref.push(this.state.formText)
    console.log('you pushed : ', this.state.formText)
    // document.querySelector('.todo-input').value = '';
    this.refs.todoInput.value = ''; //this.refs.todoInput is equal to our todo-input tag
  }
  updateTodoState(e){
    this.setState({
      formText: e.target.value
    })
    console.log(this.state.formText);
  }
  render() {
    return (
      <form className="todo-form" onSubmit={ this.sendTodo.bind(this) }>
        <input onKeyUp={this.updateTodoState.bind(this)}
              className="todo-input"
              ref="todoInput"
              type="text" placeholder="add todos..." />
        <input className="todo-submit" type="submit" value="Send" />
      </form>
    );
  }
}

export default Form
