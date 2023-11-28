<template>
<h1>
    Test
    <v-text-field v-model="id" ></v-text-field>
    <v-text-field v-model="name"></v-text-field>
    <v-text-field v-model="info"></v-text-field>
</h1>

<button @click="getTeam15()">Team Hans Dieter</button>
</template>

<script>
import axios from "axios"
import { getBaseTransformPreset } from '@vue/compiler-core';


export default {
    
    data() {
        return {
            id:'',
            name:'',
            info:''
        }
    },

    methods:{
        getTeam(){
            console.log("test")
            axios.get("http://localhost:8000/getTeam/"+this.$route.params.id,{
           
        }).then(response => {
            console.log(response)
            var responseData = response.data
            var tempData = responseData.data
            this.id = tempData["id"]
            this.name = tempData["name"]
            this.info = tempData["info"]
            
        })
        .catch(error=> {
            console.log(error)
            
        })
        },
        getTeam15(){
            window.location.href = '/getTeam/15';
        }
    },

    beforeMount(){
        this.getTeam()
    }


};

</script>