<script>

export default {

  name: "CustomerDashboard",
  data() {
    return {
        name: null,
    }
  },
  async created() {
    await this.fetchCustomer()
  },

  methods: {
    async fetchCustomer() {
        try{
        const res = await fetch('http://localhost:5050' + '/customer', {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.name = data.f_name + ' ' + data.l_name



        }
    }catch(e){
        console.error(e)
    }
        
        


    },
    customerLogout() {
        this.$store.commit('logout')
        localStorage.removeItem('user-type')
        this.$router.push('/')
    }

  }
}

</script>


<template>
    <h1>Welcome {{ name }} !!</h1>
    <button @click="customerLogout">Logout</button>

</template>