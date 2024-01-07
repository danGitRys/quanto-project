// src/store/myStore.js

import { defineStore } from 'pinia';

export const projectIdStore = defineStore('projectIdStore', {
  state: () => ({
    sharedData: null,
  }),
  actions: {
    setSharedData(data) {
      this.sharedData = data;
    }
   
  },
});
