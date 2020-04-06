import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Welcome_Screen from './Components/Welcome_Screen';
import Home_Screen from './Components/Home_Screen'

export default function App() {
  return (
    //<View style={styles.container}>
    //  <Text>Hello World!</Text>
    //</View>
    <Welcome_Screen/>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
