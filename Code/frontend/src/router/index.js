import { createWebHistory, createRouter } from 'vue-router'

import Landing from '../components/Landing.vue'
import Dashboard from '../components/Dashboard.vue'
import SignUp from '../components/SignUp.vue'
import AdminDisplayCategory from '../components/admin/AdminDisplayCategory.vue'

const routes = [
    { path: '/', component: Landing },
    { path: '/signup', component: SignUp },
    { path: '/dashboard', component: Dashboard },
    { path: '/admin/:category', component: AdminDisplayCategory, props: true },
    



    

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;