export const planetChartData = (dataset) => {
	const chart = {
		type: "line",
		data: {
			labels: ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"],
			datasets: [
				// {
				// 	label: "Preço Previsto",
				// 	data: [0, 0, 1, 2, 79, 82, 27, 14],
				// 	// data: [0.166, 2.081, 3.003, 0.323, 954.792, 285.886, 43.662, 51.514],
				// 	backgroundColor: "rgba(54,73,93,.5)",
				// 	borderColor: "#36495d",
				// 	borderWidth: 3
				// },
				{
					label: "Preço Previsto",
					data: dataset,
					backgroundColor: "rgba(168, 212, 179)",
					borderColor: "#47b784",
					borderWidth: 3
				}
			]
		},
		options: {
			responsive: true,
			lineTension: 1,
			scales: {
				yAxes: [
					{
						ticks: {
							beginAtZero: true,
							padding: 25
						}
					}
				]
			}
		}
	};

	return chart;
}

export default planetChartData;
