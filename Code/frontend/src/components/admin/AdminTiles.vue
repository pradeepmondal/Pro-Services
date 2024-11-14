<script>
export default {
  name: "AdminTiles",
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
            <div class=" tile-heading">
                Services 
            </div>
        </div>


        <div class="col-lg-3 col-md-6 col-12 requests-container">
            <div class="tile-heading">
                SRs 
            </div>
        </div>


        <div class="col-lg-3 col-md-6 col-12 customers-container">
            <div class="tile-heading">
                Customers 
            </div>
        </div>


        <div class="col-lg-3 col-md-6 col-12 professionals-container">
            <div class="tile-heading">
                Professionals 
            </div>
        </div>
        
    </div>


</template>


<style scoped>
.tiles-container {
    margin: 5rem 1rem;
    
    justify-content: space-evenly;

}

.tiles-container > div {
    display: flex;
    border: 1px solid black;
    width: 15rem;
    height: 12rem;
}

.tile-heading {
    justify-content: center;
    padding: 0.5rem 0.5rem;
}

</style>