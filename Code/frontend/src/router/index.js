import { createWebHistory, createRouter } from 'vue-router'

import Landing from '../components/Landing.vue'
import Dashboard from '../components/Dashboard.vue'
import SignUp from '../components/SignUp.vue'

const routes = [
    { path: '/', component: Landing },
    { path: '/dashboard', component: Dashboard },

    { path: '/signup', component: SignUp },

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;