import { createWebHistory, createRouter } from 'vue-router'

import Landing from '../components/Landing.vue'
import Login from '../components/Login.vue'
import SignUp from '../components/SignUp.vue'

const routes = [
    { path: '/', component: Landing },
    { path: '/login', component: Login },
    { path: '/signup', component: SignUp },

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;