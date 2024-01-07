<script setup>
import HelloWorld from '@/components/HelloWorld.vue'
import TopBar from '@/components/TopBar.vue'
import SideBar from '@/components/SideBar.vue'
import { ref, reactive } from 'vue';
import {AuthService} from '@/service/login.js'
import axios from "axios"
import { useRouter } from 'vue-router';

import { useUser } from '@/store/user';

let isPassword = ref(true);
function showPassword() {
  isPassword.value = !isPassword.value;
}
const email = ref("");
const password = ref("");

const User = useUser()
// 
async function getEmployeeData() {
    // const url = "http://localhost:3001/"
    // fetch(url).then(response => response.json())
    // .then(data => console.log(data))
    // .catch(err => console.log(err))
    console.log("Called")
    console.log(email.value)
    const router = useRouter(); 
    try {
        const token = await AuthService.login(email.value, password.value);
        console.log("here comes the token")
        console.log(token);

        window.localStorage.setItem('token', token);
        axios.post("http://localhost:8000/login",{
            token:token
        }).then(response => {
            console.log(response)
            if(response.data['login']==true){
                window.location.href = '/newproject';
            }
            else{
                alert("Invalid Login")
            }
        })
        .catch(error=> {
            console.log(error)
            alert("Invalid Login")
        })


        if (token) {
            User.loginUser(token)
            User.fetchUserData(token)
            window.location.href = '/'
        }

    } catch (error) {
        console.error(error);
        alert("Invalid Login");
    }
   
}
</script>

<template>
  <div class="limiter">
    <div class="loginScreenMainContainer">
      <p class="loginTag">Login</p>
      <div class="loginScreenInputContainer">
        <input
          v-model="email"
          id="inputEmployeeName"
          type="text"
          placeholder="E-Mail"
        />
        <div class="passwordContainer">
          <input
            v-model="password"
            :type="isPassword ? 'password' : 'text'"
            id="inputEmployeePassword"
            placeholder="Password"
          />
          <div @click="showPassword" id="showPassword">
            <link
              rel="stylesheet"
              href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
            />
            <i class="fas fa-eye" :class="{ 'fa-eye-slash': !isPassword }"></i>
          </div>
        </div>
        <button @click="getEmployeeData" id="loginButton">LOGIN</button>
      </div>

      <div class="logoContainer">
        <div class="logoImage">
          <img src="../icons/LogoQuantoSolutions.png" alt="logo" id="logo" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.logoImage {
    position: absolute;
    top: 25%;
    }

    .logoContainer {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 35%;
    height: 500px;
    position: relative;
  
    }





.limiter {
  max-height: 100vh;
}


.passwordContainer {
  position: relative;
  width: 300px;
}

.loginScreenMainContainer {
  background: linear-gradient(110deg, #304c5d 40%, #94b8c7 40%);
  min-height: 100vh;
  min-width: 100vh;
}

.loginTag {
  font-size: 48px;
  text-decoration: underline;
  position: relative;
  top: 200px;
  left: 60%;
}

.loginScreenInputContainer {
  display: flex;
  flex-direction: column;
  position: relative;
  top: 300px;
  left: 50%;
}

#inputEmployeeName {
  width: 300px;
  height: 40px;
  border: 2px solid black;
  font-size: 24px;
  outline-color: #ef7c00;
}

#inputEmployeeName::placeholder {
  color: #304c5d;
  padding-left: 10px;
}

#inputEmployeePassword {
  width: 300px;
  height: 40px;
  border: 2px solid black;
  font-size: 24px;
  margin-top: 20px;
  padding-right: 40px;
  /*reserviert Platz für Passwort anschauen Icon*/
  outline-color: #ef7c00;
}

#inputEmployeePassword::placeholder {
  color: #304c5d;
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

#loginButton {
  width: 300px;
  height: 40px;
  font-size: 24px;
  margin-top: 20px;
  background-color: #304c5d;
  color: #ef7c00;
  font-weight: bold;
  cursor: pointer;
  border-radius: 10%;
}

#loginButton:hover {
  border: 2px solid #ef7c00;
}
</style>
