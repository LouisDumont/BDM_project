import React from 'react'
import {View, Text, StyleSheet} from 'react-native'
import Home_Screen from './Home_Screen'
import NodeScreen from './Node_screen'
import data from '../Helpers/story2'

class Welcome_Screen extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            was_shown: false
        }
    }

    componentDidMount(){
        if (!this.state.was_shown){
            setTimeout(function(){this.setState({was_shown: true});}.bind(this), 1000)
        }
    }

    render(){
        console.log('render function called for Welcome_Screen component')
        if (!this.state.was_shown){
            return (
            <View style={styles.container}>
                <Text style={styles.general_text}>
                    This adventure{"\n"}is brought to you by{"\n"}
                    BDCM
                </Text>
            </View>
            );
            }
        //else {return(<Home_Screen/>)}
        else {return(<NodeScreen node={data[0]}/>)}
    }
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#333333',
      alignItems: 'center',
      justifyContent: 'center',
    },
    general_text: {
        alignContent: 'center',
        color: '#00ff00',
        justifyContent: 'center',
        textAlign: 'center',
        width: '50%',
    }
  });

export default Welcome_Screen;

