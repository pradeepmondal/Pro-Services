import { createWebHistory, createRouter } from 'vue-router'

import Landing from '../pages/Landing.vue'
import Dashboard from '../pages/Dashboard.vue'
import SignUp from '../pages/SignUp.vue'
import AdminDisplayCategory from '../pages/admin/AdminDisplayCategory.vue'
import AdminServicesInCategory from '../pages/admin/services/AdminServicesInCategory.vue'
import ServicesInCategory from '../pages/customer/components/services/ServicesInCategory.vue'
import CustomerServiceHistory from '../pages/customer/CustomerServiceHistory.vue'
import SPServiceHistory from '../pages/sp/SPServiceHistory.vue'
import CustomerProfile from '../pages/customer/CustomerProfile.vue'
import SPProfile from '../pages/sp/SPProfile.vue'


const routes = [
    { path: '/', name:'Home', component: Landing },
    { path: '/signup', component: SignUp },
    { path: '/dashboard', component: Dashboard },
    { path: '/admin/:category', component: AdminDisplayCategory, props: true , meta: {roles: ['admin']}},
    { path: '/admin/service_category/:cat_id', component: AdminServicesInCategory, props: true , meta: {roles: ['admin']}},
    { path: '/customer/service_category/:cat_id', component: ServicesInCategory, props: true , meta: {roles: ['customer']}},
    { path: '/customer/service_history', component: CustomerServiceHistory, props: true , meta: {roles: ['customer']}},
    { path: '/sp/service_history', component: SPServiceHistory, props: true , meta: {roles: ['sp']}},
    { path: '/customer/profile', component: CustomerProfile, props: true , meta: {roles: ['customer']}},
    { path: '/sp/profile', component: SPProfile, props: true , meta: {roles: ['sp']}},



    

]

const router = createRouter({
    history: createWebHistory(),
    routes
})


router.beforeEach((to, from, next) => {
    const user_type = localStorage.getItem('user-type');
    const allowed_roles = to.meta.roles;

    if(allowed_roles && !allowed_roles.includes(user_type)){
        alert("Unauthorized access")
        next({name: 'Home'});

    } else {
        next();
    }

})

export default router;