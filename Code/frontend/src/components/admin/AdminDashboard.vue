<script>
import Navbar from './Navbar.vue';
import AdminSearch from './AdminSearch.vue';
import AdminTiles from './AdminTiles.vue';




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
  <Navbar :email  :adminLogout="adminLogout"/>
    <div class="container-fluid">
      
      
      <AdminSearch />
      <AdminTiles />
    </div>
    

</template>