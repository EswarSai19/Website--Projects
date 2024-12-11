// Sample Chart.js integration for Workforce Stats
const ctx = document.getElementById("skillsChart").getContext("2d");
new Chart(ctx, {
  type: "bar",
  data: {
    labels: ["JavaScript", "Python", "React", "Node.js", "Design"],
    datasets: [
      {
        label: "Professionals with skills",
        data: [120, 150, 180, 200, 100],
        backgroundColor: [
          "#0288d1",
          "#03a9f4",
          "#ff4081",
          "#ffd600",
          "#9c27b0",
        ],
      },
    ],
  },
});
