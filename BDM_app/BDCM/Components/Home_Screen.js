import React from 'react'
import {View, Text, StyleSheet, FlatList} from 'react-native'
import Full_button from './Full_Button'
import data from '../Helpers/story2'
import EventItem from './Event_Item'

class Home_Screen extends React.Component{


  render(){
    return(
      <View style={styles.container}>
        <View style={styles.container}>
          <Text style={styles.general_text}>
            Welcome to your Home Screen! We are working on the app again...
          </Text>
        </View>
        <View style={styles.container, {flex: 2, alignItems: 'flex-start'}}>
          <Full_button/>
          <Full_button/>
        </View>
        <View style={styles.container}>
          <FlatList
            data={data}
            keyExtractor={(item) => item.id.toString()}
            //renderItem={({item}) => <Text>{item.title}</Text>}
            renderItem={({item}) => <EventItem event={item}/>}
          />
        </View>
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