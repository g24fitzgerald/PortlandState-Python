/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import React, { Component } from 'react';
import {
  AppRegistry,
  StyleSheet,
  Text,
  View,
  Slider,
  TouchableHighlight   //lets user click button to reset state
} from 'react-native';

export default class GAR extends Component {
  constructor(props){
    super(props); //makes react component pass the initial props to the newly contructed object. passed properties of newly contructed child to parent

    this.state = {
      supervision: 2,
      planning: 2,
      teamSelection: 2,
      teamFitness: 2,
      environment: 2,
      complexity: 2
    }
  }

  _total(){  //underscore methods in react if it's your custom method
    return this.state.supervision +
    this.state.planning +
    this.state.teamSelection +
    this.state.teamFitness +
    this.state.environment +
    this.state.complexity;
  }
  _color(){
    let total = this._total()
    if (total <= 23) return 'Green'
    if (total <= 44) return 'Amber'
    return 'Red'
  }
_initialState(){
  return this.setState( {
    supervision: 2,
    planning: 2,
    teamSelection: 2,
    teamFitness: 2,
    environment: 2,
    complexity: 2
  })
}
  render() {
    return (
      <View style={styles.container}>
        <View style={[styles.header, styles[this._color().toLowerCase()] ]}>
          <Text style={styles.headerText}>{this._total()}{ this._color()}</Text>
        </View>
        <View style={styles.sliderSection}>
          <Text>Supervision: {this.state.supervision}</Text>
          <Slider
          minimumValue={0}
          maximumValue={10}
          step={1}
          value={this.state.supervision}
          onValueChange={(number)=>{
            this.setState({
              supervision: number
            })
          }}
          />
        </View>
        <View style={styles.sliderSection}>
          <Text>Planning: {this.state.planning}</Text>
          <Slider
          minimumValue={0}
          maximumValue={10}
          step={1}
          value={this.state.planning}
          onValueChange={(number)=>{
            this.setState({
              planning: number
            })
          }}
          />
        </View>
        <View style={styles.sliderSection}>
          <Text>Team Selection: {this.state.teamSelection}</Text>
          <Slider
          minimumValue={0}
          maximumValue={10}
          step={1}
          value={this.state.teamSelection}
          onValueChange={(number)=>{
            this.setState({
              teamSelection: number
            })
          }}
          />
        </View>
        <View style={styles.sliderSection}>
          <Text>Team Fitness: {this.state.teamFitness}</Text>
          <Slider
          minimumValue={0}
          maximumValue={10}
          step={1}
          value={this.state.teamFitness}
          onValueChange={(number)=>{
            this.setState({
              teamFitness: number
            })
          }}
          />
        </View>
        <View style={styles.sliderSection}>
          <Text>Environment{this.state.environment}</Text>
          <Slider
          minimumValue={0}
          maximumValue={10}
          step={1}
          value={this.state.environment}
          onValueChange={(number)=>{
            this.setState({
              environment : number
            })
          }}
          />
        </View>
        <View style={styles.sliderSection}>
          <Text>Complexity: {this.state.complexity}</Text>
          <Slider
          minimumValue={0}
          maximumValue={10}
          step={1}
          value={this.state.complexity}
          onValueChange={(number)=>{
            this.setState({
              complexity : number
            })
          }}
          />
        </View>
        <TouchableHighlight
          style={styles.button}
          onPress={()=>{
            this.setState( {
              supervision: 2,
              planning: 2,
              teamSelection: 2,
              teamFitness: 2,
              environment: 2,
              complexity: 2
            })
          }}
          >
          <Text style={styles.buttonText}>Reset Values to 2</Text>
        </TouchableHighlight>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5FCFF'
  },
  green: {
    backgroundColor: '#21C064'
  },
  amber: {
    backgroundColor:'#F7941D'
  },
  red: {
    backgroundColor: '#DE4341'
  },
  button: {
    backgroundColor: '#1452E3',
    flex: 2,
    justifyContent: 'center',
    alignItems: 'center'
  },
  buttonText: {
    color: 'white',
    fontSize: 20
  },
  header: {
    backgroundColor: 'green',
    flex: 3,
    fontSize: 30,
    justifyContent: 'center',
    alignItems: 'center'
  },
  headerText: {
    color: 'white',
  },
  sliderSection: {
    flex: 2,
    borderBottomColor: '#ccc',
    borderBottomWidth: 1,
    justifyContent: 'center',
    paddingLeft: 16,
    paddingRight: 16
  }
});

AppRegistry.registerComponent('GAR', () => GAR);
