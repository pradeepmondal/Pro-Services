import { createApp } from 'vue'
import { createStore } from 'vuex'
import './style.css'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import 'bootstrap-icons/font/bootstrap-icons.css'



const store = createStore({
    state() {
        return {
            auth_token: null,
            email: null,
            user_type: null,
            user_details: null

        }
    },

    mutations: {
        setUser(state) {
            try{
                if(JSON.parse(localStorage.getItem('user'))){
                    const user = JSON.parse(localStorage.getItem('user'))
                    state.auth_token = user.token
                    state.email = user.email
                    state.user_type = localStorage.getItem('user-type')
                }
            } catch {
                console.log('user not logged in');
                
            }



        },
        setUserDetails(state) {
            try{
                if(JSON.parse(localStorage.getItem('user-details'))){
                    state.userDetails = JSON.parse(localStorage.getItem('user-details'))
                }
                
            } catch {
                console.log('user not logged in');
                
            }



        },
        logout(state) {
            state.auth_token = null
            state.email = null
            state.user_type = null
            state.userDetails = null
            localStorage.removeItem('user')
            localStorage.removeItem('user-type')
            localStorage.removeItem('user-details')
        }
    }
})

store.commit('setUser')


createApp(App).use(router).use(store).mount('#app')
