<script>

import Tile from '../Tile.vue';


export default {
  name: "Services",
  components: {
    Tile
  },

  data(){
    return {
      loading: false,
      categories: null,
      
        
        
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
  }
};
</script>

<template>
  
    <div class="">
        <div v-if="loading">Loading...</div>
        <div v-else>
        <div>Explore service categories</div>
        <div class="tiles-container row">
        
        <div v-for="cat in categories" class="col-lg-3 col-md-6 col-12 services-container">
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