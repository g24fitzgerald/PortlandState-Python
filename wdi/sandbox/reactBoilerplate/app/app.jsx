var React = require('react');
var ReactDOM = require('react-dom');

var objectOne = {
  name: 'Kim',
  location: 'CA'
};

var objectTwo = {
  age: 30,
  ...objectOne
};

console.log(objectTwo);

ReactDOM.render(
  <h1>Boilerplate app</h1>,
  document.getElementById('app')
);
