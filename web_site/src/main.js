// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
//  eslint-disable-next-line
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import {Button,Row,Col} from 'vant'
//import 'element-ui/lib/theme-chalk/index.css'
import '../theme/index.css'
Vue.use(ElementUI,{size:'small',zIndex:3000})
Vue.use(Button).use(Row).use(Col)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})