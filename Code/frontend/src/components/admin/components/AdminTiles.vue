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
            <Tile tile_heading="Services" />
        </div>


        <div class="col-lg-3 col-md-6 col-12 requests-container">
            <Tile tile_heading="SRs" />
        </div>


        <div class="col-lg-3 col-md-6 col-12 customers-container">
            <Tile tile_heading="Customers" />
        </div>


        <div class="col-lg-3 col-md-6 col-12 professionals-container">
            <Tile tile_heading="Professionals" />
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