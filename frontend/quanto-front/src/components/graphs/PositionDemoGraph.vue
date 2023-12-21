<template>
    <h1>Hello</h1>
    <canvas id="my-chart" width="500" height="300"></canvas>
</template>
<script>

import Chart from 'chart.js';

new Chart(document.getElementById('my-chart'), {
  type: 'line',
  data: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    datasets: [
      {
        label: '2018 Sales',
        data: [300, 700, 450, 750, 450]
      }
    ]
  }
});

</script>