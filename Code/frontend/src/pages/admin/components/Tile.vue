<script>
export default {
  name: "Tile",
  props: {
    tile_heading: {
      type: String,
      required: true,
    },
    goto: {
      type: Boolean,
      required: true,
    },
    navlink: {
      type: String,
    },

    statlink: {
      type: String,
    },
    stats: {
      type: Boolean,
      required: true,
    },
    delete: {
      type: Boolean,
    },
    create: {
      type: Boolean,
    },
    addCategory: {
      type: Function,
    },
    deleteCategory: {
      type: Function,
    },
    obj: {
      type: Object,
    },
    export_csv: {
      type: Boolean,
    },
    exportSRCSV: {
      type: Function,
    },
  },
  data() {
    return {

      
    };
  },
  methods: {
    gotoNavigate() {
      this.$router.push(this.navlink);
    },
    statNavigate() {
      this.$router.push(this.statlink);
    },
  },
};
</script>

<template>
  <div
    v-if="obj"
    class="tile background-image"
    :style="{ backgroundImage: `url(data:image/png;base64,${obj.thumbnail})` }"
  ><div class="overlay">
    <div class="tile-heading">
      {{ tile_heading }}
    </div>

    <div class="tile-buttons">
      <button
        v-if="goto"
        class="goto btn btn-outline-primary"
        @click="gotoNavigate"
      >
        Go to {{ tile_heading }}
      </button>

      <button
        v-if="stats"
        class="stats btn btn-outline-primary"
        @click="statNavigate"
      >
        View Stats
      </button>

      <button
        v-if="export_csv"
        class="stats btn btn-outline-success"
        @click="exportSRCSV"
      >
        Export SR Report
      </button>

      <button
        v-if="delete"
        class="stats btn btn-outline-danger"
        data-bs-toggle="modal"
        data-bs-target="#staticBackdrop"
        @click="deleteCategory(obj)"
      >
        Delete
      </button>

      <button
        v-if="create"
        class="stats btn btn-outline-success"
        data-bs-toggle="modal"
        data-bs-target="#staticBackdrop"
        @click="addCategory"
      >
        Add
      </button>
    </div>
</div>
  </div>

  <div
    v-else
    class="tile background-image"
    :style="{ backgroundImage: `url(src/pages/admin/assets/${tile_heading}.png)` }"
  ><div class="overlay">
    <div class="tile-heading">
      {{ tile_heading }}
    </div>

    <div class="tile-buttons">
      <button
        v-if="goto"
        class="goto btn btn-outline-primary"
        @click="gotoNavigate"
      >
        Go to {{ tile_heading }}
      </button>

      <button
        v-if="stats"
        class="stats btn btn-outline-primary"
        @click="statNavigate"
      >
        View Stats
      </button>

      <button
        v-if="export_csv"
        class="stats btn btn-outline-success"
        @click="exportSRCSV"
      >
        Export SR Report
      </button>

      <button
        v-if="delete"
        class="stats btn btn-outline-danger"
        data-bs-toggle="modal"
        data-bs-target="#staticBackdrop"
        @click="deleteCategory(obj)"
      >
        Delete
      </button>

      <button
        v-if="create"
        class="stats btn btn-outline-success"
        data-bs-toggle="modal"
        data-bs-target="#staticBackdrop"
        @click="addCategory"
      >
        Add
      </button>
    </div>
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

  width: 100%;
  height: 20rem;
  background-size: cover;
  background-position: center;
  

  border-radius: 1rem;

  

  
  
}

.overlay {
    background: rgba(255, 255, 255, 0.517);
    z-index: 1;
    position: relative;
    padding: 1.5rem 3.5rem;
    backdrop-filter: blur(0.8rem);
    border: 1px solid rgba(255, 255, 255, 0.412);
    border-radius: 1rem;
    
    

}

.tile-heading {
  padding: 0.5rem 0.5rem;
  max-height: max-content;
  max-width: max-content;
  font-size: 1.5rem;
  margin: auto;
  margin-bottom: 1rem;
  color: rgb(46, 46, 46);
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
