<script>

import CustomerNotification from './components/CustomerNotification.vue';
import CustomerSearch from './components/CustomerSearch.vue';
import Navbar from './components/Navbar.vue'
import ServiceCategories from './components/services/ServiceCategories.vue';


export default {

  name: "CustomerDashboard",
  components: {
    Navbar,
    CustomerSearch,
    CustomerNotification,
    ServiceCategories
    
  },
  data() {
    return {
        customer: null,
        loading: true
    }
  },
  async created() {
    try {
      await this.fetchCustomer()
    } catch (e) {
      console.error(e)

    } finally {
      this.loading = false
    }
  },

  methods: {
    async fetchCustomer() {
        try{
        const res = await fetch('http://localhost:5050' + '/customer', {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.customer = data
            localStorage.setItem('user-details', JSON.stringify(this.customer))
            this.$store.commit('setUserDetails')
            
        }
    }catch(e){
        console.error(e)
    }
        

    }

  }
}

</script>


<template>
  <div v-if="loading">Loading...</div>
  <div v-else>
  <Navbar />
  <div class="container-fluid">
  <CustomerNotification :customer="customer" />
    <h1>Welcome {{ customer.f_name }} !!</h1>
    <CustomerSearch />
    <ServiceCategories />
  </div>
  </div>

</template>