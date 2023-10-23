<template>
  <div>
    <router-link :to="{name: 'Login' }">Login</router-link> 
  <router-view />
  
</div>
</template>

<script setup>
  import LoginScreen from '@/views/LoginScreen.vue'
</script>
