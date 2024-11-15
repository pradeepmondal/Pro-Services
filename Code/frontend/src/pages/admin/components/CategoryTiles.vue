<script>
import Tile from './Tile.vue';

export default {
  name: "CategoryTiles",
  components: {
    Tile
  },
  props: {
    addCategory : {
        type: Function,
    },
    categories: {
        type: Array,
        required: true
    },
    deleteCategory: {
        type: Function
    }

    
  },
  data(){
    return {
        email: this.$store.state.email,
        

        
    }
  },

  methods: {
    
  }
};
</script>

<template>
    <div class="tiles-container row">
        
        <div v-for="cat in categories" class="col-lg-3 col-md-6 col-12 services-container">
            <Tile :tile_heading="cat.name" :goto="true" :stats="false" :category="String(cat.cat_id)" :delete="true" :deleteCategory="deleteCategory" :obj="cat" />
        </div>

        <div class="col-lg-3 col-md-6 col-12 services-container">
            <Tile tile_heading="Add Category" :goto="false" :stats="false" category="add_category" :create="true" :addCategory="addCategory" />
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