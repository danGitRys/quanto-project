<script setup>
  import HelloWorld from '@/components/HelloWorld.vue'
  import TopBar from '@/components/TopBar.vue'
import { ref, reactive } from 'vue';
let isPassword = ref(true);
function showPassword(){
    isPassword.value = !isPassword.value;
}
const email = ref('');
const password = ref('');


// 
function getEmployeeData(){
    // const url = "http://localhost:3001/"
    // fetch(url).then(response => response.json())
    // .then(data => console.log(data))
    // .catch(err => console.log(err))


    const url = "http://localhost:3001/login"
    fetch(url,{
        method:"POST",
        // headers:{
        //     'Content-Type':'application/json'
        // },
        // wandelt die Daten in ein JSON String um 
        body: JSON.stringify({
            email: email.value,
            password: password.value
            
        })
       
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(err => console.log(err))

console.log(email.value)
console.log(password.value)

}



</script>

<template>
    <div class="limiter">
 <div class="loginScreenMainContainer">
    <p class="loginTag">Login</p>
    <div class=" loginScreenInputContainer">
    <input v-model ="email" id="inputEmployeeName" type="text" placeholder="E-Mail">
    <div class="passwordContainer">
    <input v-model ="password" :type="isPassword ? 'password' : 'text' " id ="inputEmployeePassword" placeholder="Password">
    <div @click="showPassword" id="showPassword">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
     <i class="fas fa-eye" :class="{ 'fa-eye-slash': !isPassword }"></i>
    </div>
    
        </div>
     <button @click="getEmployeeData" id="loginButton">LOGIN</button>
</div>

     <div class="logoContainer">
            <div class="logoImage">
            <img src = "../icons/LogoQuantoSolutions.png" alt="logo" id="logo"> 
            </div>
        </div>
    
        </div>

      

     </div>
   


</template>

<style scoped>

.logoImage{
position: absolute;
top: 25%;
left: 35%;
}
.limiter {
    max-height: 100vh;
}
.logoContainer{
    display: inline-block;
    width: 35%;
    height: 500px;
    position: relative;
}

.passwordContainer {
    position: relative;
    width: 300px;
}

.loginScreenMainContainer{
    background: linear-gradient(110deg, #304C5D 40%, #94B8C7 40%);
    min-height: 100vh;
    min-width: 100vh;
}

.loginTag{
    font-size: 48px;
    text-decoration: underline;
    position: relative;
    top: 200px;
    left:60%   
}

.loginScreenInputContainer{
    display: flex;
    flex-direction: column;
    position: relative;
    top: 300px;
    left: 50%;
}
#inputEmployeeName{
    width: 300px;
    height: 40px;
    border: 2px solid black;
    font-size: 24px;
    outline-color: #EF7C00;
}
#inputEmployeeName::placeholder{
    color:#304C5D;
      padding-left: 10px;
}

#inputEmployeePassword{
    width: 300px;
    height: 40px;
    border: 2px solid black;
    font-size: 24px;
    margin-top: 20px;
    padding-right: 40px; /*reserviert Platz für Passwort anschauen Icon*/   
     outline-color: #EF7C00;
    
     
}
#inputEmployeePassword::placeholder{
    color:#304C5D;
    padding-left: 10px;
}

#showPassword {
    display: flex;
    justify-content: center;
    width: 30px;
    position: absolute;
    top: 31px;
    right: 20px;
    cursor: pointer;
}


#loginButton{
    width: 300px;
    height: 40px;
    font-size: 24px;
    margin-top: 20px;
    background-color: #304C5D;
    color: #EF7C00;
    font-weight: bold;
    cursor: pointer;
    border-radius: 10%;
}

#loginButton:hover{
    border: 2px solid #EF7C00;
}


</style>