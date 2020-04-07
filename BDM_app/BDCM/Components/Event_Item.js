import React from 'react'
import {StyleSheet, View, Text, Button, TouchableOpacity} from 'react-native'
import data from '../Helpers/story2'

class EventItem extends React.Component{

    //_find_node = () => {
    //    const node_name = event.res_node
    //    return (data.getElementbyId(node_name))
    //}

    render(){
        console.log('Transmitted choice')
        console.log(this.props)
        //const {event, navigate_func} = this.props
        const event = this.props.event
        const res_node = data.find((e) => e.id === event.res_node)
        return(
            <TouchableOpacity
             style={styles.glob_container}
             onPress={()=>{this.props.navigate(res_node)}}>
                <View>
                <Text style={styles.description}>{event.description}</Text>
                </View>
            </TouchableOpacity>
        );
    }
}

const styles = StyleSheet.create({
    glob_container:{
        backgroundColor: '#000000',
        borderColor: '#ffffff',
        justifyContent: 'space-between',
        flex:1,
        borderWidth: 3,
    },
    narration:{
        textAlign: 'left',
        flex: 1,
        color: '#00ff00',
        margin: 2,
    },
    description:{
        textAlign: 'left',
        flex: 1,
        color: '#00ff00',
        margin: 2,
    }
})

export default EventItem;