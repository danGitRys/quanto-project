// Utilities
import { defineStore } from "pinia";

export const useAppStore = defineStore("app", {
  state: () => ({
    names: ["Project1", "Project2", "Project3", "Project4", "Project5"],
  }),
});
