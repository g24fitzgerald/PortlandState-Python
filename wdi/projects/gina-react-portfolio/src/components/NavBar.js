import React, { Component } from 'react';
import NavLink from './NavLink';
import '../css/navbar.css';
class NavBar extends Component {
  render () {
    return (
      <header role="banner" className="bs-docs-nav navbar navbar-default navbar-static-top">
        <div className="nav-container">
          <div className="navbar-header">
            <a className="navbar-brand" href="/">Gina Fitzgerald | Web Developer</a>
            <button type="button" className="navbar-toggle collapsed">
              <span className="sr-only">navigation</span>
              <span className="icon-bar"></span>
              <span className="icon-bar"></span>
              <span className="icon-bar"></span>
            </button>
          </div>
          <div className="navbar-collapse bs-navbar-collapse collapse">
            <ul id="top" className="nav navbar-nav" role="navigation">
              <li><NavLink to="/" onlyActiveOnIndex>Biography </NavLink></li>
              <li><NavLink to="/portfolio">Portfolio</NavLink></li>
              <li><NavLink to="/contact">Resume</NavLink></li>
              <li><a href="https://github.com/G24FITZGERALD">Github</a></li>
            </ul>
          </div>
        </div>
      </header>
    )
  }
}
export default NavBar;
