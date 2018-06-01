var React = require('react');

var GreeterForm = React.createClass({
  onFormSubmit: function(e) {
    e.preventDefault(); //prevents browser from refreshing

    var updates = {};
    var name = this.refs.name.value;
    var message = this.refs.message.value;

    if (name.length > 0) {
      this.refs.name.value = ''; //empties input field box on submission
      updates.name = name;
    }
    if (message.length > 0) {
      this.refs.message.value=''; //empties textarea on submission
      updates.message = message;
    }
    this.props.onNewData(updates); //passed the value of the input box and text field to onNewName function
  },
  render: function() {
    return (
      <form onSubmit={this.onFormSubmit}>
        <div>
          <input type="text" ref="name" placeholder="Enter name..."/>
        </div>
        <div>
          <textarea ref="message" placeholder="Enter message"> </textarea>
        </div>
        <button>Submit</button>
      </form>
    );
  }
});

module.exports = GreeterForm;
