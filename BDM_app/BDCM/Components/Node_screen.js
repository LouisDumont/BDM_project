import React from 'react'
import {View, Text, StyleSheet, FlatList, Button, ScrollView} from 'react-native'
//import ScrollText from 'react-scroll-text'
import Full_button from './Full_Button'
//import data from '../Helpers/story2'
import EventItem from './Event_Item'
import Full_Button from './Full_Button'

class NodeScreen extends React.Component{
    constructor(props){
        super(props);
        //this.count=0
        // Advice: use state only for variables that should change the display
        this.state = {count:0, _node:this.props.node}
        //this._navigate = this._navigate.bind(this)
        console.log('Transmitted node:')
        console.log(this.state._node)
    }

    _navigate = (node) => {
        //this.node = this.node
        //this.forceUpdate()
        //this.count += 1
        //this.forceUpdate()
        //this.setState({count: this.state.count+2})
        console.log('navigate called')
        this.setState({_node: node})
    }

    render(){
        //const node = this.props.node
        return(
            <View style={styles.container}>
              <ScrollView style={styles.narration}>
                <Text style={styles.general_text}>
                  {this.state._node.description}
                </Text>
              </ScrollView>
              <View style={styles.container}>
                <FlatList
                  data={this.state._node.choices}
                  keyExtractor={(item) => item.id.toString()}
                  renderItem={({item}) => <EventItem event={item} navigate={this._navigate}/>}
                  //renderItem = {({item}) => <Full_Button event={item}/>}
                />
              </View>
            </View> 
        );
    }
}

const styles = StyleSheet.create({
    container: {
        marginTop: 23,
        flex: 1,
        backgroundColor: '#333333',
        justifyContent: 'center',
    },
    narration:{
        //height: 200,
        backgroundColor: '#000000',
        borderColor: '#ffffff',
        //justifyContent: 'space-between',
        flex:1,
        borderWidth: 3,
    },
    general_text: {
        alignContent: 'center',
        color: '#00ff00',
        //justifyContent: 'center',
        textAlign: 'left',
    },
  });

export default NodeScreen;