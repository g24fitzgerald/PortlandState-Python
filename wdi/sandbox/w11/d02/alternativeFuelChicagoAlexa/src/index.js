/**
    Copyright 2014-2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.

    Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

        http://aws.amazon.com/apache2.0/

    or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
*/

/**
 * This simple sample has no external dependencies or session management, and shows the most basic
 * example of how to create a Lambda function for handling Alexa Skill requests.
 *
 * Examples:
 * One-shot model:
 *  User: "Alexa, tell Hello World to say hello"
 *  Alexa: "Hello World!"
 */

/**
 * App ID for the skill
 */
var APP_ID = 'amzn1.ask.skill.14fd8105-aa10-46fe-b7fd-f0808d15bc46'; //replace with "amzn1.echo-sdk-ams.app.[your-unique-value-here]";

/**
 * The AlexaSkill prototype and helper functions
 */
var AlexaSkill = require('./AlexaSkill');
var axios = require('axios');
/**
 * AskChuck is a child of AlexaSkill.
 * To read more about inheritance in JavaScript, see the link below.
 *
 * @see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Introduction_to_Object-Oriented_JavaScript#Inheritance
 */
var FindFuel= function () {
    AlexaSkill.call(this, APP_ID);
};

// Extend AlexaSkill
FindFuel.prototype = Object.create(AlexaSkill.prototype);
FindFuel.prototype.constructor = FindFuel;

// AskChuck.prototype.eventHandlers.onSessionStarted = function (sessionStartedRequest, session) {
//     console.log("AskChuck onSessionStarted requestId: " + sessionStartedRequest.requestId
//         + ", sessionId: " + session.sessionId);
//     // any initialization logic goes here
// };

FindFuel.prototype.eventHandlers.onLaunch = function (launchRequest, session, response) {
    console.log("AskChuck onLaunch requestId: " + launchRequest.requestId + ", sessionId: " + session.sessionId);
    var speechOutput = "Ask for the location of an alternative fuel station in Chicago";
    var repromptText = "You can ask for the location of an alternative fuel station in Chicago";
    response.ask(speechOutput, repromptText);
};

// AskChuck.prototype.eventHandlers.onSessionEnded = function (sessionEndedRequest, session) {
//     console.log("AskChuck onSessionEnded requestId: " + sessionEndedRequest.requestId
//         + ", sessionId: " + session.sessionId);
//     // any cleanup logic goes here
// };

FindFuel.prototype.intentHandlers = {
    // register custom intent handlers
    "GetAlternativeFuelIntent": function (intent, session, response) {
      axios.get('https://data.cityofchicago.org/resource/alternative-fuel-locations.json?')
      .then(function(resp){
        var output = [];
        for (var i = 0; i < resp.data.length; i++) {
          output.push(resp.data[i].street_address + ' ' + resp.data[i].city);
        }
        response.tellWithCard(output, "Location", output);
      })
      .catch(function(error){
        console.log(error);
      });
    },
    //any slot variables are received by intent from lambda funciton
    // "GetCustomFactIntent": function(intent, session, response){
    //   var firstName = intent.slots.FirstName.value;
    //
    //   axios.get('http://api.icndb.com/jokes/random?lastName=&firstName=' + firstName)
    //   .then(function(resp){
    //     console.log(resp);
    //     response.tellWithCard(resp.data.value.joke, "Chuck Norris Fact", resp.data.value.joke);
    //   })
    //   .catch(function(error){
    //     console.log(error);
    //   });
    // },

    "AMAZON.HelpIntent": function (intent, session, response) {
        response.ask("You can ask for the location of an alternative fuel source!", "You can ask about alternative fuel source!");
    }
};

// Create the handler that responds to the Alexa Request.
exports.handler = function (event, context) {
    // Create an instance of the AskChuck skill.
    var findFuel = new FindFuel();
    findFuel.execute(event, context);
};
