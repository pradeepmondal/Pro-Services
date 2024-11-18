<script>

export default {

  name: "SPDashboard",
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
    <h1>Welcome {{ sp.f_name }} !!</h1>
    <button @click="spLogout">Logout</button>

</template>