import React, { Component } from 'react'
import firebase from '../fb_configs.js'

class List extends Component {
  constructor(props){
    super(props)
    this.state = {
      todos: []
    }
  }
  //will run whenever this component (List) shows up on page
  componentDidMount(){
    //event names: value, child_added, child_removed, child_updated are all

    firebase.ref.on('child_removed', (snapshot)=>{
      console.log('delete key: ', snapshot.key)
      //Look through our state array and find the same object that we deleted from our firebase and remove it from state
      this.state.todos.forEach((todo,index)=>{
        if(snapshot.key === todo.key){
          //delete object from state
          let newTodos = this.state.todos
          newTodos.splice(index, index+1)
          this.setState({
            todos: newTodos
          })

        }
      })
    })

    firebase.ref.on('child_added', (snapshot) => { //everytime something is entered, we have state (with todos) and event child_added function (which will add event in state and cause refresh)
      //add item to database
      console.log("snapshot: ",snapshot.val())
      console.log('snapshot key: ', snapshot.key);

      this.setState({
        // todos: this.state.todos.concat(snapshot.val()) //sets todos to itself, concatenated with the new item sumbmitted
        todos: this.state.todos.concat({ //rather than add to the state just the val, we add an object with val and key
            val: snapshot.val(),
            key: snapshot.key
            })
      })
    })
  }
  deleteTodo(event, key){
    firebase.ref.child(key).remove();
    console.log('key deleted');
  }

    const renderTodos = this.state.todos.map(todo => {
      return(<li key={todo.key} className="todo-item">
        { todo.val }
        <button onClick={ (e) => { this.deleteTodo(event, todo.key) } }>Delete</button>
      </li>)
    })

    return (
      <ul className="todo-list">
        { renderTodos.reverse() }
      </ul>

    );
  }
}

export default List
