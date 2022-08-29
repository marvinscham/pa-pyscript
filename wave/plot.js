const chart = new Chart("chart", {
    type: "line",
    data: {
        datasets: [{
            label: "Auslenkung",
            borderColor: "teal",
            backgroundColor: "teal",
        }
        ]
    },
    options: {
        scales: {
            x: {
                display: false
            }
        }
    }
})

function update(x, y) {
    chart.data.labels = x
    chart.data.datasets[0].data = y
    chart.update()
}