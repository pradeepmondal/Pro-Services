<script>


import ActiveSRs from './components/ActiveSRs.vue';
import Navbar from './components/Navbar.vue'
import PendingSRs from './components/AllSRs.vue';

export default {

  name: "SPDashboard",
  components: {
    Navbar,
    ActiveSRs,
    PendingSRs
    
    
  },
  data() {
    return {
        loading: true,
        sp: null,
    }
  },
  async created() {
    try {
      await this.fetchSP()
    } catch (e) {
      console.error(e)

    } finally {
      this.loading = false
    }
  },

  methods: {
    async fetchSP() {
        try{
        const res = await fetch('http://localhost:5050' + '/sp', {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.sp = data
            localStorage.setItem('user-details', JSON.stringify(this.sp))
            this.$store.commit('setUserDetails')



        }
    }catch(e){
        console.error(e)
    }
        
        


    },
    spLogout() {
        this.$store.commit('logout')
        localStorage.removeItem('user-type')
        this.$router.push('/')
    }

  }
}

</script>


<template>
  <div v-if="loading">Loading...</div>
  <div v-else>
    <Navbar />

    <div class="parent-container">

      <h1 class="welcome-message">Welcome {{ sp.f_name }} !!</h1>
    
    <ActiveSRs />



    </div>
    
   

    



  </div>

    

</template>

<style scoped>
.parent-container {
  
  
  height: 92vh;
  width:100%;
  
  background-color: antiquewhite;

}

.welcome-message {
  font-size: 2rem;
  padding: 1rem;
  padding-top: 0.5rem;
  padding-bottom: 0rem;
}






</style>