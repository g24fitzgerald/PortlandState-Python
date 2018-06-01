import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, hashHistory, IndexRoute } from 'react-router';
import App from './components/App';
import Biography from './components/Biography';
import Portfolio from './components/Portfolio';
import Contact from './components/Contact';
// import HireMe from './components/HireMe';



ReactDOM.render(
  <Router history={ hashHistory }>
    <Route path="/" component={ App }>
      <IndexRoute component={ Biography } />
      <Route path="/portfolio" component={ Portfolio }/>
      <Route path="/contact" component={ Contact }/>
    </Route>

  </Router>,
  document.getElementById('root')
);
