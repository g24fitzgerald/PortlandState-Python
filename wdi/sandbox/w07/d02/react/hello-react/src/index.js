import React from 'react'; //ES5 sytax: var React = require('react'); core library that react and react DOM utilizes
import ReactDOM from 'react-dom'; //everything from library specific to the DOM
import App from './App'; //specifies a file, not a library because of the ./
import './index.css'; //how we load css, import into js rather than link in html. keeps css modular instead of 1 global css file. webpack will combine them in the end anyway, but its good for development

ReactDOM.render(
  <App />, //JSX component 
  document.getElementById('root') //render to something with id of root
);
