import { defineStore } from "pinia";

export const projectPosition = defineStore("projectPosition", {
  state: () => ({
    names: ["10A Senior Developer Remote", "10B Senior Developer On-Site"],
  }),
});
