// Utilities
import { defineStore } from "pinia";
import axios from "axios";

export const useAppStore = defineStore("app", {
  state: () => ({
    names: ["Test", "hey"],
    isLoaded: false,
  }),

  actions: {
    fetchDataFromEndpoint() {
      try {
        const response = axios.get("http://localhost:8000/getProject/7");
        this.names = response.data.data;
        console.log(response.data.data);
        this.isLoaded = true;
      } catch (error) {
        console.error("Fehler beim Abrufen der Daten", error);
      }
    },
  },

  getters: {
    getNames() {
      return this.names;
    },
  },
});
