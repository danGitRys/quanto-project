<template>
<h1>
    Test
</h1>
</template>

<script>
import axios from "axios"
import { getBaseTransformPreset } from '@vue/compiler-core';


export default {
    
    data() {
        return {
            drawer: true,
            rail: true,
        }
    },

    methods:{
        getTeam(){
            console.log("test")
            axios.get("http://localhost:8000/getTeam/"+this.$route.params.id,{
           
        }).then(response => {
            console.log(response)
            
        })
        .catch(error=> {
            console.log(error)
            alert("Invalid Login")
        })
        }
    },

    beforeMount(){
        this.getTeam()
    }


};

</script>