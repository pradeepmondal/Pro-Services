<script>
import Navbar from '../Navbar.vue';
import CustomerSearch from '../CustomerSearch.vue';
import Tile from '../Tile.vue';


export default {
  name: "ServicesInCategory",
  props: ['cat_id'],
  components: {
    Navbar,
    CustomerSearch,
    Tile

  },
  data(){
    return {
        email: this.$store.state.email,
        services: null,
        modal_type: null,
        obj: null,
        modal_heading: null,
        loading: false
        
        
    }
  },
  async created() {
    try {
      await this.fetchServices()
    } catch (e) {
      console.error(e)

    } finally {
      this.loading = false
    }
  },

  methods: {
    async fetchServices() {
        try{
        const res = await fetch('http://localhost:5050' + '/services/' + this.cat_id , {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.services = data



        }
    }catch(e){
        console.error(e)
    }
        
        


    },
    deleteService(service){
        this.modal_type = "delete_form"
        this.obj = service
        this.modal_heading = "Delete " + service.name
    },

    editService(service){
        this.modal_type = "edit_form"
        this.obj = service
        this.modal_heading = "Edit " + service.name
    },

    viewService(service){
        this.modal_type = "view_form"
        this.obj = service
        this.modal_heading = service.name
    }


  }
};
</script>

<template>
    <Navbar />
    <div v-if="loading" class="loading">Loading...</div> 
    <div v-else class="container-fluid">
    
    
    
    <CustomerSearch />
    
    
    
    <div>Services in category {{ cat_id }}</div>
    <div class="tiles-container row">
        
        <div v-for="service in services" class="col-lg-3 col-md-6 col-12 services-container">
            <Tile :tile_heading="service.name" :navlink="'/customer/service/'+service.s_id " />
        </div>
        </div>


</div>
</template>


<style scoped>
.tiles-container {
    margin: 5rem 1rem;
    
    justify-content: space-evenly;

}



</style>