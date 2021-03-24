<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar class="bg-dark">
        <q-toolbar-title class="text-grey-5">
          AgroPredict
        </q-toolbar-title>
      </q-toolbar>
    </q-header>
    <q-page-container class="bg-dark">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>

export default {
  name: 'MainLayout',
  data () {
    return {
      leftDrawerOpen: false,
    }
  }
}
</script>
