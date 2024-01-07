import { defineStore } from 'pinia';

export const projectionStore = defineStore('projectionStore', {
  state: () => ({
    sharedData: null,
  }),
  actions: {
    setSharedData(data) {
      this.sharedData = data;
    },
  },
});
