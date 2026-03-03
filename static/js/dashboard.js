new Chart(document.getElementById('incomeChart'), {
    type: 'line',
    data: {
        labels: ['T1', 'T2', 'T3', 'T4', 'T5', 'T6'],
        datasets: [{
            data: [400, 700, 550, 900, 1100, 850],
            borderColor: '#0d6efd',
            fill: true
        }]
    }
});