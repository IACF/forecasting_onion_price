<template>
	<q-page class="q-pa-xl text-grey-5">
		<div class="q-mb-xl">
			<h1 class="q-ma-none">Previsão de preço</h1>
			<p class="q-ma-none">Tenha informações do preço de cebola do ano de 2019</p>
		</div>
		<div>
			<q-form class="row q-gutter-md">
				<q-select
					class="width-select"
					dark
					outlined
					v-model="form.month"
					:options="options"
					label="Mês"
				/>
				<q-btn color="primary" outline icon="fas fa-chart-bar" label="Prever" no-caps/>
			</q-form>
		</div>
		<planet-chart class="q-mt-xl"/>
	</q-page>
</template>

<script>
import PlanetChart from '../components/PlanetChart'
import planetChartData from './planet-data'

export default {
	name: 'PageIndex',
	components: {
		PlanetChart
	},
	data() {
		return {
			options: [
				{
					label: 'Janeiro',
					value: '01/2019'
				},
				{
					label: 'Fevereiro',
					value: '02/2019'
				},
				{
					label: 'Março',
					value: '03/2019'
				},
				{
					label: 'Abril',
					value: '04/2019'
				},
				{
					label: 'Maio',
					value: '05/2019'
				},
				{
					label: 'Junho',
					value: '06/2019'
				},
				{
					label: 'Julho',
					value: '07/2019'
				},
				{
					label: 'Agosto',
					value: '08/2019'
				},
				{
					label: 'Setembro',
					value: '09/2019'
				},
				{
					label: 'Outubro',
					value: '10/2019'
				},
				{
					label: 'Novembro',
					value: '11/2019'
				},
				{
					label: 'Dezembro',
					value: '12/2019'
				},
			],
			form: {
				month: null,
			},
			planetChartData
		}
	},
	mounted() {
		const ctx = document.getElementById('planet-chart');
		new Chart(ctx, this.planetChartData);
	}
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
