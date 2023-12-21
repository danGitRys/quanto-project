import { defineStore } from "pinia";

export const teamroles = defineStore("teamroles", {
  state: () => ({
    role: ["Teamleader", "Member"],
  }),
});