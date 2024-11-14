<script>
import Tile from './Tile.vue';

export default {
  name: "AdminTiles",
  components: {
    Tile
  },
  props: {
    
  },
  data(){
    return {
        
    }
  }
};
</script>

<template>
    <div class="tiles-container row">
        
        <div class="col-lg-3 col-md-6 col-12 services-container">
            <Tile tile_heading="Services" category="services" />
        </div>


        <div class="col-lg-3 col-md-6 col-12 requests-container">
            <Tile tile_heading="SRs" category="srs" />
        </div>


        <div class="col-lg-3 col-md-6 col-12 customers-container">
            <Tile tile_heading="Customers" category="customers" />
        </div>


        <div class="col-lg-3 col-md-6 col-12 professionals-container">
            <Tile tile_heading="Professionals" category="professionals" />
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