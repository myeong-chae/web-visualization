var green = "rgba(52,191,158,1)";
var lightgreen = "rgba(45, 204, 170, 1)";
var blue = "rgba(0,147,214,1)";
var lightblue = "rgba(0, 157, 230, 1)";
var orange = "rgba(239,141,54,1)";
var yellow = "rgba(255,232,124,1)";
var red = "#FF4242";
var transparent = "rgba(0,0,0,0)";

Chart.defaults.global.defaultFontColor = '#888888';
Chart.defaults.global.defaultFontFamily = '"Open Sans"';
//Chart.defaults.global.legend = false;

var companyCtx = document.getElementById("company");
var company = new Chart(companyCtx, {
  type: 'doughnut',
  data: {
    labels: [
      "Män",
      "Kvinnor",
    ],
    datasets: [{
      data: [11, 6],
      backgroundColor: [
        orange,
        blue,
      ]
    }]
  }
});

var earningsCtx = document.getElementById("earnings");
var earnings = new Chart(earningsCtx, {
  type: 'line',
  data: {
    labels: ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"],
    datasets: [{
      label: 'Debitering Vunna Uppdrag, SEK',
      data: [4200000, 4100000, 3850000, 3425000, 2780000, 2500000, 2200000, 3000000, 2600000, 2400000, 1850000, 1500000],
      fill: false,
      backgroundColor: lightblue,
      borderColor: blue,
      borderWidth: 3
    }, {
      label: 'Debitering inkl Prospekt, SEK',
      data: [4300000, 4600000, 4200000, 3900000, 3000000, 2900000, 2300000, 3500000, 3400000, 3200000, 2500000, 2000000],
      fill: false,
      backgroundColor: orange,
      borderColor: orange,
      borderWidth: 3,
      cubicInterpolationMode: "monotone"
    }]
  },
  options: {
    maintainAspectRatio: false,
    layout: {padding: {right:10}},    
    legend: {
      display: false
    },
    scales: {
      display:false,
      xAxes: [{
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          display: false
        }
      }],
      yAxes: [{
        ticks: {
          display: false,
          beginAtZero: false
        },
        gridLines: {
          display: false,
          drawBorder: false
        }
      }]
    }
  }
});

var utilizationCtx = document.getElementById("utilization");
var utilization = new Chart(utilizationCtx, {
  type: 'line',
  data: {
    labels: ["Jan", "Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"],
    datasets: [{
      label: 'Beläggningsgrad Vunna Uppdrag, Procent',
      data: [85, 80, 75, 73, 76, 65, 60, 55, 40, 38, 20, 16],
      fill: true,
      backgroundColor: lightgreen,
      borderColor: green,
      borderWidth: 3
    }, {
      label: 'Beläggningsgrad inkl Prospekt, Procent',
      data: [105, 90, 85, 83, 80, 69, 62, 60, 50, 40, 38, 30],
      fill: true,
      backgroundColor: lightblue,
      borderColor: blue,
      borderWidth: 3,
      cubicInterpolationMode: "monotone"
    }]
  },
  options: {
    layout: {padding: {right:10}},
    maintainAspectRatio: false,
    legend: {
      display: false
    },
    scales: {
      display:false,
      xAxes: [{
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          display: false
        }
      }],
      yAxes: [{
        ticks: {
          display: false,
          beginAtZero: false
        },
        gridLines: {
          display: false,
          drawBorder: false
        }
      }]
    }
  }
});

var projectsCtx = document.getElementById("projects");
var projects = new Chart(projectsCtx, {
  type: 'bar',
  data: {
    labels: ["Öppna", "Vunna", "Förlorade"],
    datasets: [{
      label: 'Projekt',
      data: [11, 34, 7],
      fill: true,
      backgroundColor: [blue, green, red],

    }]
  },
  options: {
    layout: {padding: {right:0, left:-10}},
    maintainAspectRatio: false,
    legend: {
      display: false
    },
    scales: {
      display:false,
      xAxes: [{
        barPercentage: 1.2,
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          display: false
        }
      }],
      yAxes: [{
        ticks: {
          display: false,
          beginAtZero: false
        },
        gridLines: {
          display: false,
          drawBorder: false
        }
      }]
    }
  }
});

var competencesCtx = document.getElementById("competences");
var competences = new Chart(competencesCtx, {
  type: 'radar',
  data: {
    labels: ["Brancher", "Roller", "Verktyg", "Tekniker", "Metoder och processer", "Plattformar"],
    datasets: [{
      label: 'Projekt',
      data: [27, 43, 26, 30, 38, 37],
      fill: false,
      backgroundColor: blue,
      borderColor: blue,
      pointBorderColor: blue,
      pointBackgroundColor: lightblue,
      pointRadius: 3

    }]
  },
  options: {
    layout: {padding: {right:0, left:45}},
    maintainAspectRatio: false,
    legend: {
      display: false
    },
    scale: {   
      display:true,
      ticks: {
        beginAtZero: true,
        display: false
      },
      pointLabels : {
        fontSize: 2,
        callback: function(pointLabel){ return null}
      }
    }
  }
});