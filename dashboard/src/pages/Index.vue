<template>
	<q-page class="q-pa-xl text-grey-8">
		<div class="q-mb-xl">
			<h1 class="q-ma-none">Previsão de preço</h1>
			<p class="q-ma-none">Tenha informações do preço de cebola do ano de 2019</p>
		</div>
		<div>
			<q-form class="row justify-between">
				<div class="row q-gutter-md">
					<q-select
						class="width-select"
						outlined
						v-model="month"
						:options="options"
						label="Mês"
					/>
					<q-btn
						color="primary"
						outline
						icon="fas fa-chart-bar"
						label="Prever"
						no-caps
						:disable="!month.value"
						@click="getPricePredicted"
					/>

					<q-btn
						v-if="showPrice"
						color="primary"
						outline
						icon="fas fa-file-invoice-dollar"
						disable
						:label="predictPrice"
						no-caps
					/>
				</div>
				<div>
				</div>
			</q-form>
		</div>
		<planet-chart
			v-show="showChart"
			class="q-mt-xl"
		/>
	</q-page>
</template>

<script>
import PlanetChart from '../components/PlanetChart'
import planetChartData from './planet-data'

export default {
	name: 'PageIndex',
	components: {
		PlanetChart,
	},
	data() {
		return {
			options: [
				// {
				// 	label: '',
				// 	value: null
				// },
				{
					label: 'Janeiro',
					value: 1
				},
				{
					label: 'Fevereiro',
					value: 2
				},
				{
					label: 'Março',
					value: 3
				},
				{
					label: 'Abril',
					value: 4
				},
				{
					label: 'Maio',
					value: 5
				},
				{
					label: 'Junho',
					value: 6
				},
				{
					label: 'Julho',
					value: 7
				},
				{
					label: 'Agosto',
					value: 8
				},
				{
					label: 'Setembro',
					value: 9
				},
				{
					label: 'Outubro',
					value: 10
				},
				{
					label: 'Novembro',
					value: 11
				},
				{
					label: 'Dezembro',
					value: 12
				},
			],
			month: {
				label: '',
				value: null
			},
			planetChartData2: null,
			predictPrice: 0,
			showPrice: false,
			showChart: false,
			prices: null
		}
	},
	mounted() {
		this.getPrices();
	},
	methods: {
		getPrices () {
			this.$axios.post('http://localhost:4000/api/price',
				{
					month: this.month && this.month.value
				}
			)
			.then(({ data }) => {
				this.prices = data.prices

				const array_prices = Object.values(this.prices).map((element) => element.price);
				console.log(array_prices);
				this.planetChartData2 = planetChartData(array_prices);


				const ctx = document.getElementById('planet-chart');
				new Chart(ctx, this.planetChartData2);
			});
		},

		getPricePredicted() {
			console.log(planetChartData);
			this.predictPrice = this.prices[this.month.value].price;
			this.showPrice = true;
			this.showChart = true;

		}
	},
}
</script>
<style lang="scss">
	h1 {
		font-size: 2.5rem;
		line-height: 1.2;
	}

	h2 {
		font-size: 1.5rem;
	}

	.width-select {
		width: 18.75rem;
	}
</style>
