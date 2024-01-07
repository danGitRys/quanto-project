import { defineStore } from 'pinia';
import axios from 'axios'

export const useUser = defineStore('User', {
    state: () => ({
        userData: null,
        loggedIn: false,
        token: null,
    }),
    actions: {
        loginUser(token) {
            // this.userData = userData
            this.loggedIn = true
            this.token = token
            localStorage.setItem('token', token)
        },
        logoutUser() {
            this.userData = null
            this.loggedIn = false
            this.token = null
            localStorage.removeItem('token')
        },
        async fetchUserData(token) {
            this.loggedIn = true
            this.token = token
            const request = await axios.post("http://localhost:8000/login",{
                token:token
            }).then(response => {
                if(response.data['login']==true) {
                    this.userData = response.data.employee
                    return response.data.employee
                }
                else{
                    alert("Invalid Login")
                }
            })
            .catch(error=> {
                console.log(error)
                alert("Invalid Login")
            })
        },
    },
    getters: {
        getUserData() {
            return this.userData
        },
        getUser() {
          return this.userData
        },
        isLoggedIn() {
          return this.loggedIn
        },
    },
})