import React, { Component } from 'react';
import '../css/resume.css';
import resume from '../images/resume.png'

class Contact extends Component {
  render() {
    return (
      <div>
        <div className="canva-embed" data-height-ratio="1.2941" data-design-id="DACLSgKp0F8">
          <img src={resume} className="resume" alt="Gina Fitzgerald CV" />
        </div>
        <script async src="https://sdk.canva.com/v1/embed.js"></script><a href="https://www.canva.com/design/DACLSgKp0F8/view?utm_content=DACLSgKp0F8&utm_campaign=designshare&utm_medium=embeds&utm_source=link" target="_blank">Dark Blue Shape Corporate Resume</a> by <a href="https://www.canva.com/g24fitzgerald?utm_campaign=designshare&utm_medium=embeds&utm_source=link" target="_blank">Gina Fitzgerald</a>
      </div>
    )
  }
}

export default Contact;

// style="padding:129.41% 5px 5px 5px;background:rgba(0,0,0,0.03);border-radius:8px;"
