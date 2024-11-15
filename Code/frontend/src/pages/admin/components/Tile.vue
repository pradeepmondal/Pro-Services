<script>
export default {
  name: "Tile",
  props: {
    tile_heading: {
        type: String,
        required: true
    },
    goto: {
        type: Boolean,
        required: true
    },
    category: {
        type: String,
        required: true
    },
    stats: {
        type: Boolean,
        required: true

    },
    delete: {
        type: Boolean,
    },
    create: {
        type: Boolean
    },
    addCategory : {
        type: Function,
    },
    deleteCategory : {
        type: Function
    },
    obj: {
        type: Object
    }
    
  },
  data(){
    return {
        
        
    }
  },
  methods: {
    gotoNavigate() {
        this.$router.push('/admin/' + this.category)
    },
    statNavigate() {
        this.$router.push('/admin/stat/' + this.category)
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
                <button v-if="goto" class="goto btn btn-outline-primary" @click="gotoNavigate">
                    Go to {{ tile_heading }}

                </button>

                <button v-if="stats" class="stats btn btn-outline-primary" @click="statNavigate">
                    View Stats

                </button>

                <button v-if="delete" class="stats btn btn-outline-danger" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="deleteCategory(obj)">
                    Delete

                </button>

                <button v-if="create" class="stats btn btn-outline-success" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="addCategory">
                    Add

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