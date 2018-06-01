import React, { Component } from 'react';
import Slider from 'react-slick';
import image1 from '../images/launder-this-home.png';
import image2 from '../images/mutt-match.png';

import '../css/portfolio.css';

//will this work if I use divs or spans and make the image their background?
class Portfolio extends Component {
  render() {
    var settings = {
      dots: false
    }
    return (
      <div className='container portfolio'>
      	<Slider {...settings}>
        	<div className="row">
            <div className="col-xs-12 col-sm-6 portfolio-div">
            <img className="portfolio-image" src={ image1 } alt="Launder This App" />
            </div>
            <div className="col-xs-12 col-sm-5  carosel-caption">
              <h2>Launder This</h2>
              <p>What it is: An on demand laundry pickup and drop off scheduling mobile app build with ReactNative, using Firebase.</p>
              <p>My contributions: Developed routes and logic to push props from parent to child components, display on confirmation page and push up to firebase upon confirmation, then pull into order history. Styled order history, pickup and drop-off pages</p>
              <a target="https://github.com/g24fitzgerald/wash-app">View on Github</a>
            </div>
          </div>
          <div className="row">
            <div className="col-xs-12 col-sm-6 portfolio-div">
              <img className="portfolio-image" src={ image2 } alt="Mutt Match" />
            </div>
            <div className="col-xs-12 col-sm-5  carosel-caption">
              <h2>Mutt Match</h2>
              <p>What it is: A web application built using NodeJS with an Express framework that employs Auth0 and makes AJAX calls to MongoLab to allow prospective dog-owners to create a profile, answer questions and receive a list of pets that match their lifestyle preferences.Designed by a UX team, built by 3 developers.</p>
              <p>My contributions: I developed the user survey, as well as logic and routing to send survey results to MongoLab database, and pull down only the dogs that match their preferences. Additionally I implemented Auth0 sign in, and styled the homepage to the specifications set by our UX team using HTML5, CSS and bootstrap. </p>
              <a target="https://github.com/g24fitzgerald/mutt_match">View on Github</a>
            </div>
          </div>
        </Slider>
      </div>
    );
  }
}

export default Portfolio;
