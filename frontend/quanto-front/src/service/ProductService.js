
// ProductServices.js
export const ProductService = {
  async getProductsMini() {
    try {
      const data = [
        {
          date: monthData,
          planed: [8, 15, 6, 18, 20],
          worked: [15, 20, 30, 20, 30, 40],
          // positions: [
          //   { label: "Project1", value: "Option A" },
          //   { label: "Project2", value: "Option B" },
          //   { label: "Project3", value: "Option C" },
          // ],
        },
      ];

      return data;
    } catch (error) {
      console.error("Fehler beim Abrufen der Produkte:", error);
      throw error;
    }
  },
};


const generateDatesForMonth = (year, month) => {
  const dates = [];
  const daysInMonth = new Date(year, month + 1, 0).getDate();

  for (let day = 1; day <= daysInMonth; day++) {
    const date = `${day.toString().padStart(2, "0")}.${(month + 1)
      .toString()
      .padStart(2, "0")}.${year}`;
    dates.push(date);
  }

  return dates;
};

// Example usage for November 2023
const monthData = generateDatesForMonth(2023, 10); // Note: Month is zero-based, so 10 represents November


