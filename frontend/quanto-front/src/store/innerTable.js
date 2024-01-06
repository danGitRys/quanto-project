// store.js
import { defineStore } from "pinia";
import axios from "axios";

export const useMyStore = defineStore("myStore", {
  state: () => ({
    bookingTimes: [],
  }),

  actions: {
    async fetchBookingTimes(userId, date) {
      const url = `http://localhost:8000/getBookingTimes/${userId}/${date}`;

      try {
        const response = await axios.get(url);
        return response;
        this.bookingTimes = response.data;
      } catch (error) {
        // Hier kannst du Fehlerbehandlung hinzufügen, wenn die Anfrage fehlschlägt
        console.error("Fehler bei der Datenabfrage:", error.message);
      }
    },
  },
});
