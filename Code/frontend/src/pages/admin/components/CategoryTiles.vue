<script>
import Tile from './Tile.vue';

export default {
  name: "CategoryTiles",
  components: {
    Tile
  },
  props: {
    
  },
  data(){
    return {
        email: this.$store.state.email,
        categories: null

        
    }
  },
  async created() {
    await this.fetchServices()
  },

  methods: {
    async fetchServices(){
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
        
        


    }
  }
};
</script>

<template>
    <div class="tiles-container row">
        
        <div v-for="cat in categories" class="col-lg-3 col-md-6 col-12 services-container">
            <Tile :tile_heading="cat.name" :stats="false" :category="String(cat.cat_id)" />
        </div>



        
    </div>


</template>


<style scoped>
.tiles-container {
    margin: 5rem 1rem;
    
    justify-content: space-evenly;

}

.tiles-container > div {
    
}



</style>