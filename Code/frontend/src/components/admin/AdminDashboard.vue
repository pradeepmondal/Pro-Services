<script>

export default {

  name: "AdminDashboard",
  data() {
    return {
        email: null,
    }
  },
  async created() {
    await this.fetchAdmin()
  },

  methods: {
    async fetchAdmin() {
        try{
        const res = await fetch('http://localhost:5050' + '/admin', {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': localStorage.getItem('auth-token')}})
        if(res.ok){

            const data = await res.json()
            this.email = data.email



        }
    }catch(e){
        console.error(e)
    }
        
        


    },
    adminLogout() {
        localStorage.removeItem('auth-token')
        localStorage.removeItem('user-type')
        this.$router.push('/')
    }

  }
}

</script>


<template>
    <h1>Welcome {{ email }} !!</h1>
    <button @click="adminLogout">Logout</button>

</template>