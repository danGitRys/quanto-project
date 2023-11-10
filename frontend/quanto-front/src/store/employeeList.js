import { defineStore } from "pinia";

export const employeeList = defineStore("employeeList", {
  state: () => ({
    name: ["André", "Lisa"],
  }),
});
