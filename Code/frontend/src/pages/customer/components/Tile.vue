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
    },

    obj: {
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
    
    <div
    v-if="service"
    class="tile background-image"
    :style="{ backgroundImage: `url(data:image/png;base64,${service.thumbnail})` }"
  ><div class="overlay_for_services">
    <div class="tile-heading">
      {{ tile_heading }}
    </div>
  </div>

  
  </div>
  </div>

  <div v-if="!openModal" class="tile" @click="gotoNavigate">
    <div
    v-if="obj"
    class="tile background-image"
    :style="{ backgroundImage: `url(data:image/png;base64,${obj.thumbnail})` }"
  ><div class="overlay">
    <div class="tile-heading">
      {{ tile_heading }}
</div>
</div>
      
    </div>
  </div>
</template>

<style scoped>
.tile {
  display: flex;
  flex-direction: column;
  border: 1px solid black;
  width: 10rem;


  justify-content: space-around;
  align-items: center;

  width: 100%;
  height: 15rem;
  background-size: cover;
  background-position: center;
  cursor: pointer;

  border-radius: 1rem;

  

  
  
}

.overlay {
    background: rgba(255, 255, 255, 0.517);
    z-index: 1;
    position: relative;
    padding: 2rem 3rem;
    backdrop-filter: blur(0.8rem);
    border: 1px solid rgba(255, 255, 255, 0.412);
    border-radius: 1rem;
    
    

}
.overlay_for_services {
    background: rgba(255, 255, 255, 0.517);
    z-index: 1;
    position: relative;
    padding: 1rem 1rem;
    backdrop-filter: blur(0.8rem);
    border: 1px solid rgba(255, 255, 255, 0.412);
    border-radius: 1rem;
    
    

}


.tile-heading {
  padding: 0.5rem 0.5rem;
  max-height: max-content;
  max-width: max-content;
  font-size: 1.8rem;
  margin: auto;
  margin-bottom: 1rem;
  color: rgba(40, 40, 40, 0.772);
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
