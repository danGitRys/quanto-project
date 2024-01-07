// src/store/myStore.js

import { defineStore } from "pinia";

export const projectId = defineStore("projectId", {
  state: () => ({
    projectId: null,
  }),
  actions: {
    setProjectId(id) {
      this.projectId = id;
    },
    getProjectId() {
      return this.projectId;
    },
  },
});
