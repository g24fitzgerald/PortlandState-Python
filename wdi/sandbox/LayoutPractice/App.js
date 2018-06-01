import React, { Component } from 'react';
import {View, Text, StyleSheet, TouchableHighlight} from 'react-native';
import Foo from './Foo'

export default class App extends Component {
  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.welcome}>
          foo
        </Text>
        <TouchableHighlight onPress={() => {  //this is a button with onPress event that's passed a function
          this.props.navigator.push({  //the function makes our navigator push to the next scene
            title: 'Boom',
            index: 1,
            component: Foo
          })
        }}>
          <Text style={styles.instructions}>
            Bar
          </Text>
        </TouchableHighlight>
        <Text style={styles.instructions}>
        </Text>
      </View>
    );
  }
}
//here
const styles = StyleSheet.create({
  container: { //this shows up behind everythin
    backgroundColor: 'pink',
    flex: 1,
    justifyContent: 'space-around',
    flexDirection: 'column'
  },
  welcome: {
    // backgroundColor: 'green',
    // flex: 1
  },
  instructions: {
    // backgroundColor: 'maroon',
    // flex: 2
  },
});
