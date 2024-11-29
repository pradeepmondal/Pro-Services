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
        show_service_modal: false,
        selected_service_sps: null,
        search_mode: false,
        search_query: null,
        category: null
        
        
    }
  },

  computed: {
    final_services(){
      if(!this.search_mode){
        return this.services
      }
      else{
        let search_query = this.search_query.toLowerCase()
        let regex = new RegExp(search_query, 'i')
        return this.services.filter((service) => {
          return (
            regex.test(service.name)
          )
        })

      }
    }
  },

  async created() {
    try {
      await this.fetchCategory()
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

    async fetchCategory() {
        try{
        const res = await fetch('http://localhost:5050' + '//service_category/' + this.cat_id , {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.category = data



        }
    }catch(e){
        console.error(e)
    }
        
        


    },






    async selectProfessional(service){

        this.show_booking_modal = true
        await this.fetchSPs(service)
        await this.fetchSelectedService(service)


        
    },

    async viewService(service){
        
        this.show_booking_modal = true

        await this.fetchSPs(service)
        await this.fetchSelectedService(service)
        


        
    },



    async fetchSPs(service) {
        try{
        const res = await fetch('http://localhost:5050' + '/sps/' + service.s_id, {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.selected_service_sps = data
            this.selected_service_sps.filter((sp) => sp.verification_status === 'Approved')
            
            
        }
    }catch(e){
        console.error(e)
    }
        

    },

    async fetchSelectedService(service) {
        try{
        const res = await fetch('http://localhost:5050' + '/service/' + service.s_id , {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.selected_service = data





        }
    }catch(e){
        console.error(e)
    }
        
        


    },

    updateSearchQuery(search_input){
      this.search_mode = true
      this.search_query = search_input
    },

    clearSearch(){
      this.search_mode = false
    },



  }
};
</script>

<template>
    <Navbar />
    <ServiceBookingModal  :selected_service="selected_service" :service_professionals="selected_service_sps" />
    <div v-if="loading" class="loading">Loading...</div> 
    <div v-else class=" parent-container">
    
    
    
   
    
    
    
    <div class="heading">Services in {{ category.name }}</div>
    <p class="description">{{ category.description }}</p>

    <CustomerSearch search_placeholder="Search in Services" :updateSearchQuery="updateSearchQuery" :search_mode="search_mode" :clearSearch="clearSearch" />
    <div class="tiles-container row">
        
        <div v-for="service in final_services" class="col-lg-3 col-md-6 col-12 services-container">
            <Tile :tile_heading="service.name" :viewService="viewService" :service="service"   :openModal="true" :obj="service" />
        </div>
        </div>


</div>
</template>


<style scoped>
.tiles-container {
    margin: 5rem 1rem;
    
    justify-content: space-evenly;

}

.heading {
  font-size: 1.5rem;
  padding: 1rem;
  padding-bottom: 0.5rem;
}

.description {
  padding-left: 1rem;
}

.parent-container {
  
  margin-top: 0;
  height: 92vh;
  
  background-color: antiquewhite;

}


</style>