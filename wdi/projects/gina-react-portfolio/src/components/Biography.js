import React, { Component } from 'react';
import '../css/biography.css';
import jsLogo from '../images/javascript.png';
import reactLogo from '../images/react.jpg';
import nodeLogo from '../images/nodejs-logo.png'


class Biography extends Component {
  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-xs-12 col-sm-8 biography-info">
            <div className="col-xs-3">
              <h1>Hello, I'm Gina Fitzgerald</h1>
              <h3>Scientst</h3> <h3>Developer</h3> <h3>Passionate Learner</h3>
              <div><p>I am voraciously inquisitive and my primary motivator in life is learning. </p></div>
              <div><p>
              I bring a background of science and data analytics to web development, which has enabled me to adapt quickly, while staying focused on the greater goal.
              I enjoy a finding a useful solution to a tough challenge. </p> </div>
              <p>I flourish in environments that foster respectful ideas and are comprised of driven, intelligent and collaborative individuals.</p>
            </div>
          </div>
          <div className="col-xs-12 col-sm-4 skills">
            <div className="row">
              <div className="col-xs-12 "><h2>Skills</h2></div>
              <div className="col-xs-12 icons">
                <h3>HTML & CSS</h3>
                <i className="fa fa-html5 fa-5x" aria-hidden="true"></i>
              </div>
              <div className="col-xs-12 icons">
                <h3>Responsive Design</h3>
                <i className="fa fa-mobile fa-5x" aria-hidden="true"></i>
              </div>
              <div className="col-xs-12 icons">
                <h3>Javascript</h3>
                <img src={jsLogo} className="fa img-responsive margin js-logo" alt="Javascript logo" data-pin-nopin="true"/>
              </div>
              <div className="col-xs-12 icons">
                <h3>React & React-Native</h3>
                <img src={reactLogo} className="fa img-responsive margin react-logo" alt="React logo" data-pin-nopin="true" />
              </div>
              <div className="col-xs-12 icons">
                <h3>NodeJS</h3>
                <img src={nodeLogo} className="fa img-responsive margin node-logo" alt="NodeJS logo" data-pin-nopin="true" />
              </div>
            </div>
          </div>
        </div>
      </div>
      )
  }
}

export default Biography;
