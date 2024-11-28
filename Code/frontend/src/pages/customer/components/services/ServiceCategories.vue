<script>

import Tile from '../Tile.vue';
import CustomerSearch from '../CustomerSearch.vue';


export default {
  name: "Services",
  components: {
    Tile,
    CustomerSearch
  },

  data(){
    return {
      loading: false,
      categories: null,
      search_mode: false,
      search_query: null
      
        
        
    }
  },

  computed: {
    final_categories(){
      if(!this.search_mode){
        return this.categories
      }
      else{
        let search_query = this.search_query.toLowerCase()
        let regex = new RegExp(search_query, 'i')
        return this.categories.filter((cat) => {
          return (
            regex.test(cat.name) || regex.test(cat.description)
          )
        })

      }
    }

  },

  async created() {
    try {
      await this.fetchCategories()
    } catch (e) {
      console.error(e)

    } finally {
      this.loading = false
    }
  },

  methods: {

    async fetchCategories(){
        try{
        const res = await fetch('http://localhost:5050' + '/service_categories', {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            console.log(data);
            
            this.categories = data



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
  
    <div class="">
        <div v-if="loading">Loading...</div>
        <div v-else>
        <div>Explore service categories</div>
        <CustomerSearch search_placeholder="Search in Service Categories" :updateSearchQuery="updateSearchQuery" :clearSearch="clearSearch" :search_mode="search_mode" />
        <div class="tiles-container row">
        
        <div v-for="cat in final_categories" class="col-lg-3 col-md-6 col-12 services-container">
            <Tile :tile_heading="cat.name" :navlink="'/customer/service_category/'+cat.cat_id " />
        </div>
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