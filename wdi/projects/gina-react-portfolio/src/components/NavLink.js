import React, { Component } from 'react';
import { Link } from 'react-router';
//the purpose of NavLink is so that we don't have to write activeClassName="active" on each link
class NavLink extends Component {
  render() {
    return <Link { ...this.props } activeClassName="active" />;
  }
}

export default NavLink;
