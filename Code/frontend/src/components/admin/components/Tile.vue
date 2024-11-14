<script>
export default {
  name: "Tile",
  props: {
    tile_heading: {
        type: String,
        required: true
    }
    
  },
  data(){
    return {
        
        
    }
  }
};
</script>

<template>
    <div class="tile">

            <div class="tile-heading">
                {{ tile_heading }}
            </div>

            <div class="tile-buttons">
                <button class="goto btn btn-outline-primary">
                    Go to {{ tile_heading }}

                </button>

                <button class="stats btn btn-outline-primary">
                    View Stats

                </button>
            </div>

        
    </div>


</template>


<style scoped>
.tile {
    display: flex;
    flex-direction: column;
    border: 1px solid black;
    width: 18rem;
    height: 15rem;

    justify-content: space-around;
    align-items: center;

}

.tile-heading {

    padding: 0.5rem 0.5rem;
    max-height: max-content;
    max-width: max-content;
    font-size: 1.5rem;
}

.tile-buttons {
    display: flex;
    justify-content: space-between;
    flex-direction: column;

}

.tile-buttons button {
    margin: 0.2rem;
}

</style>