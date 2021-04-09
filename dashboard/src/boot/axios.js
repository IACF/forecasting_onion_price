import axios from 'axios';

// "async" is optional;
// more info on params: https://quasar.dev/quasar-cli/boot-files
export default async ({ Vue }) => {
  Vue.prototype.$axios = axios;
}
