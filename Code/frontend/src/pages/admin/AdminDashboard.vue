<script>
import Navbar from './components/Navbar.vue';
import AdminSearch from './components/AdminSearch.vue';
import AdminTiles from './components/AdminTiles.vue';




export default {

  name: "AdminDashboard",
  components: {
    Navbar,
    AdminSearch,
    AdminTiles

  },
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
        const res = await fetch('http://localhost:5050' + '/admin', {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.email = data.email



        }
    }catch(e){
        console.error(e)
    }
        
        


    }


  }
}

</script>


<template>
  <Navbar :email />
    <div class="container-fluid">
      
      
      <AdminSearch />
      <AdminTiles />
    </div>
    

</template>