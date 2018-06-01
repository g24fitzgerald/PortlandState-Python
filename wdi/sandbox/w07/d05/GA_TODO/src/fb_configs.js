import * as firebase from 'firebase'
import dotenv from 'dotenv'

const config = {
    apiKey: "AIzaSyBU4k3lunJTBS-MzJFoHo1amQkO9UQhd6I",
    authDomain: "ga-todo-6b34f.firebaseapp.com",
    databaseURL: "https://ga-todo-6b34f.firebaseio.com",
    storageBucket: "ga-todo-6b34f.appspot.com",
    messagingSenderId: "63928638094"
}

export default {
  ref: firebase.initializeApp(config).database().ref(),
  config: config
}
