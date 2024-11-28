<script>
export default {
  name: "Tile",
  props: {
    tile_heading: {
      type: String,
      required: true,
    },

    navlink: {
      type: String,
    },

    openModal: {
      type: String,
    },

    viewService: {
        type: Function
    },
    service: {
        type: Object
    }
  },
  data() {
    return {};
  },
  methods: {
    gotoNavigate() {
      this.$router.push(this.navlink);
    },
  },
};
</script>

<template>
  <div v-if="openModal" class="tile" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="viewService(service)">
    <div class="tile-heading">
      {{ tile_heading }}
    </div>
  </div>

  <div v-if="!openModal" class="tile" @click="gotoNavigate">
    <div class="tile-heading">
      {{ tile_heading }}

      
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
  cursor: pointer;

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
