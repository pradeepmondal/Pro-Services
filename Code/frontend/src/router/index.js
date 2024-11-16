import { createWebHistory, createRouter } from 'vue-router'

import Landing from '../pages/Landing.vue'
import Dashboard from '../pages/Dashboard.vue'
import SignUp from '../pages/SignUp.vue'
import AdminDisplayCategory from '../pages/admin/AdminDisplayCategory.vue'
import AdminServicesInCategory from '../pages/admin/services/AdminServicesInCategory.vue'


const routes = [
    { path: '/', name:'Home', component: Landing },
    { path: '/signup', component: SignUp },
    { path: '/dashboard', component: Dashboard },
    { path: '/admin/:category', component: AdminDisplayCategory, props: true , meta: {roles: ['admin']}},
    { path: '/admin/service/:cat_id', component: AdminServicesInCategory, props: true , meta: {roles: ['admin']}},
    



    

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