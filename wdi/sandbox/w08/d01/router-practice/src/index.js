import React from 'react';
import ReactDOM from 'react-dom';
//import 3 components: router, route and hashHistory, indexRoute(assumes path is index, no need to set path) from react router
import {Router, Route, hashHistory, IndexRoute} from 'react-router';
import NotFound from './components/NotFound';
import App from './App';
import Home from './components/Home';
import About from './components/About';
import Background from './components/Background';
import './index.css';

ReactDOM.render(
  //asking to render everything in this file,
  //which had no reference to anything between tags until we add this.props.children toApp.js
  //when rendering app, we pass the property foobar, and its rendered where we say this.props.children
  // <App>foobar</App>,

  //here we render a router with history attribute (which adds a # to history), and route
  //define rules about how the DOM will work
  //lets us create routes to render different content
  (<Router history={ hashHistory }>
    <Route path="/" component={ App }>
      <IndexRoute component={ Home } />
      <Route path="/about" component={ About } />
      <Route path="/background" component={ Background } />
    </Route>
    <Route path="*" component={NotFound} />
  </Router>),
  document.getElementById('root')
);
