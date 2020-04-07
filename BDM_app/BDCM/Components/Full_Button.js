import React from 'react'
import { StyleSheet, View, TextInput, Button} from 'react-native'

class Full_Button extends React.Component{
    render(){return(
        <View style={styles.full_button}>
            <Button title='Test' onPress={() => {}}/>
        </View>
    )}
}

const styles = StyleSheet.create({
    full_button:{
        //marginTop: 10,
        borderColor: '#ffffff',
        //backgroundColor: '#777777',
        height: 50,
        width: 100
    }
})

export default Full_Button