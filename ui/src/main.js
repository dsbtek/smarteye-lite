import Vue from 'vue';
import App from './App.vue';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(ElementUI);
new Vue({
  render: (h) => h(App),
}).$mount('#app');
