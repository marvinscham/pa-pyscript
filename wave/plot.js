const chart = new Chart("chart", {
    type: "line",
    data: {
        datasets: [{
            label: "Auslenkung",
            borderColor: "teal",
            backgroundColor: "teal",
            tension: 0.5
        }
        ]
    },
    options: {
        scales: {
            x: {
                display: false
            }
        },
        elements: {
            point: {
                radius: 0
            }
        },
        plugins: {
            legend: {
                display: false
            }
        }
    }
})

function update(x, y) {
    chart.data.labels = x;
    chart.data.datasets[0].data = y;
    chart.update();
}

function checkScrollDirection(event) {
    if (checkScrollDirectionIsUp(event)) {
        document.querySelector("#freq").value =
            parseFloat(document.querySelector("#freq").value) +
            parseFloat(0.1);
    } else {
        document.querySelector("#freq").value -= parseFloat(0.1);
    }
}

function checkScrollDirectionIsUp(event) {
    if (event.wheelDelta) {
        return event.wheelDelta > 0;
    }
    return event.deltaY < 0;
}