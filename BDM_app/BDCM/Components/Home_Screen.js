import React from 'react'
import {View, Text, StyleSheet} from 'react-native'

class Home_Screen extends React.Component{
    render(){
        return(
            <View style={styles.container}>
            <Text style={styles.general_text}>
                Welcome to your Home Screen!
            </Text>
          </View>
        );
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
    }
  });

export default Home_Screen;