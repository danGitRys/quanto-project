// ProductServices.js
export const ProductService = {
  async getProductsMini() {
    try {
      let datum = new Date();
      const data = [
        {
          date: `${datum.getFullYear()}-${(datum.getMonth() + 1)
            .toString()
            .padStart(2, "0")}-${datum.getDate().toString().padStart(2, "0")}`,
          planed: "du 1",
          worked: 10,
          position: 25,
        },
      ];

      return data;
    } catch (error) {
      console.error("Fehler beim Abrufen der Produkte:", error);
      throw error;
    }
  },
};
