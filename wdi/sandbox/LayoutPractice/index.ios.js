/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import {
  AppRegistry, //AppRegistry = reactDOM.render: it mounts class
  Navigator,
  TouchableHighlight
} from 'react-native';

import App from './App';

class LayoutPractice extends Component {
    render() {
      return (
        <Navigator
        initialRoute={{ title: 'Awesome Scene', index: 0 }}
        renderScene={(route, navigator) =>  {//if you leave the curly brackets off on ES6 function, it will return the first thing after (don't need return statement)
          return <App navigator={ navigator}/>
        }
        }
        />
      )
    }
}

AppRegistry.registerComponent('LayoutPractice', () => LayoutPractice);
