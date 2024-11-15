<script>

export default {

  name: "SPDashboard",
  data() {
    return {
        name: null,
    }
  },
  async created() {
    await this.fetchSP()
  },

  methods: {
    async fetchSP() {
        try{
        const res = await fetch('http://localhost:5050' + '/sp', {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.name = data.f_name + ' ' + data.l_name



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
    <h1>Welcome {{ name }} !!</h1>
    <button @click="spLogout">Logout</button>

</template>