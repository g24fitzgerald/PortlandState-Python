import React, { Component } from 'react';
import '../css/footer.css';
class Footer extends Component {
  render() {
    return (
      <footer className="footer">
      <div className="col-md-12">
        <ul className="social-network social-circle">
            <li><a href="https://twitter.com/Fitzgemerald" className="icoTwitter" title="Twitter"><i className="fa fa-twitter"></i></a></li>
            <li><a href="mailto:g24fitzgerald@gmail.com" className="icoGoogle" title="Google +"><i className="fa fa-google-plus"></i></a></li>
            <li><a href="https://www.linkedin.com/in/gina-fitzgerald" className="icoLinkedin" title="Linkedin"><i className="fa fa-linkedin"></i></a></li>
        </ul>
      </div>
      </footer>
    );
  }
}

export default Footer;
