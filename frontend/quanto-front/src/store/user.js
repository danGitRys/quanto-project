import { defineStore } from 'pinia';

export const useUser = defineStore('User', {
    state: () => ({
        userData: null,
        loggedIn: false,
        token: null,
    }),
    actions: {
        loginUser(token) {
            this.userData = userData
            this.loggedIn = true
            this.token = token
            sessionStorage.setItem('token', token)
        },
        logoutUser() {
            this.userData = null
            this.loggedIn = false
            this.token = null
            sessionStorage.removeItem('token')
        }
    },
    getters: {
        getUser() {
          return this.userData;
        },
        isLoggedIn() {
          return this.loggedIn;
        },
    },
})