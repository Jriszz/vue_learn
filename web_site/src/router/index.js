import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/pages/login'
import Main from '@/pages/main'
import ShoppingMail from '@/pages/ShoppingMail'
import Parents from '@/pages/Parents/parents'
import Child from '@/pages/Parents/Child/Child'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/main/:param?',
      name: 'main',
      component: Main,
      meta:["index","main"]
    },
    {
      path: '/ShoppingMail',
      name: 'ShoppingMail',
      component: ShoppingMail
    },
    {
      path: '/Parents',
      name: 'Parents',
      component: Parents,
      children: [{
        path: '/childs',
        component: Child,
        name: 'Child'
      }],
    }
  ]
})
