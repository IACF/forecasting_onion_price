<template>
  <div>
    <canvas id="planet-chart" ref="planet"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'

export default {
  name: 'PlanetChart',
  mounted() {
    // this.$refs.planet.parentNode.style.height = '500px';
    this.$refs.planet.parentNode.style.width = '900px';
  }
}


</script>

<style lang="scss">
    .bg {
        background-color: rgb(72, 73, 72);
    }
</style>
