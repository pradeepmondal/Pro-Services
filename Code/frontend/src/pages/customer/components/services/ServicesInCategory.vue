<script>
import Navbar from '../Navbar.vue';
import CustomerSearch from '../CustomerSearch.vue';
import Tile from '../Tile.vue';
import ServiceBookingModal from './ServiceBookingModal.vue';


export default {
  name: "ServicesInCategory",
  props: ['cat_id'],
  components: {
    Navbar,
    CustomerSearch,
    Tile,
    ServiceBookingModal

  },
  data(){
    return {
        email: this.$store.state.email,
        services: null,
        modal_type: null,
        selected_service: null,
        modal_heading: null,
        loading: false,
        show_booking_modal: false,
        selected_service_sps: null
        
        
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

    async viewService(service){
        this.selected_service = service
        this.show_booking_modal = true
        await this.fetchSPs(service)


        
    },
    async fetchSPs(service) {
        try{
        const res = await fetch('http://localhost:5050' + '/sps/' + service.s_id, {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.selected_service_sps = data
            
            
        }
    }catch(e){
        console.error(e)
    }
        

    }


  }
};
</script>

<template>
    <Navbar />
    <ServiceBookingModal  :selected_service="selected_service" :service_professionals="selected_service_sps" />
    <div v-if="loading" class="loading">Loading...</div> 
    <div v-else class="container-fluid">
    
    
    
    <CustomerSearch />
    
    
    
    <div>Services in category {{ cat_id }}</div>
    <div class="tiles-container row">
        
        <div v-for="service in services" class="col-lg-3 col-md-6 col-12 services-container">
            <Tile :tile_heading="service.name" :viewService="viewService" :service="service"  :openModal="true" @click="viewService(service)"/>
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