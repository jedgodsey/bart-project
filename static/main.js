var ctx = document.getElementById('myChart').getContext('2d');

let trainData = {
  type: 'line',
  data: {
      labels: [],
      // labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
          label: 'Average System-wide Delay in minutes',
          data: new Array(500),
          // data: [1, 1, 1, 1, 1, 1],
          backgroundColor: [
              // 'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              // 'rgba(255, 206, 86, 0.2)',
              // 'rgba(75, 192, 192, 0.2)',
              // 'rgba(153, 102, 255, 0.2)',
              // 'rgba(255, 159, 64, 0.2)'
          ],
          borderColor: [
              // 'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)'
          ],
          borderWidth: 1
      }]
  },
  options: {
      scales: {
          yAxes: [{
              ticks: {
                  beginAtZero: false
              }
          }],
          xAxes: [
            {
              ticks: {
                display: true
              },
              gridLines: {
                display: false
              }
            }
          ]
      }
  }
}

var myChart = new Chart(ctx, trainData);

let socket = new WebSocket('ws://localhost:8000/ws/trains/')
socket.onmessage = (event) => {
    let trains = JSON.parse(event.data)
    // let trains = event.data

    let finalTrains = trains.map(item => item.fields.amount)
    let times = trains.map(item => item.fields.time)

    // let marks = finalTrains.map(item => 'x')

    let divisor = Math.floor(finalTrains.length / 15)

    let marks = []

    for (let i = 0; i < times.length; i++) {
      if (i % divisor == 0) {
        let moment = new Date(times[i])
        marks.push(`${moment.getHours()}:${moment.getMinutes()}`)
      } else {
        marks.push('')
      }
    }

    trainData.data.datasets[0].data = finalTrains

    trainData.data.labels = marks
    // document.querySelector('#trains').innerText = trains;
    myChart.update()
}

/////////////////////////

// socket.onmessage = (event) => {
//   let djangoData = JSON.parse(event.data);
//   console.log(djangoData)
//   document.querySelector('#app').innerText...djangoData.. 18min
// }
