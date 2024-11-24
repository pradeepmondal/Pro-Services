<script>
export default {
  name: "AdminSearch",
  props: {
    search_placeholder: {
      type: String
    },
    updateSearchQuery: {
      type: Function
    },

    clearSearch: {
      type: Function
    },

    search_mode: {
      type: Boolean
    }

    
  },
  data(){
    return {
        search_input: null,
    }
  },

  methods: {
    startClearSearch() {
      this.search_input = null;
      this.clearSearch()
    }
  },


  
};
</script>

<template>
    <div class="search-input">
      <div class="input-container">
        <i class="bi bi-search"></i>
        <input
                type="text"
                class="form-control"
                :placeholder="search_placeholder"
                
                aria-label="Search"
                aria-describedby="basic-addon1"
                v-model="search_input"
                @change="updateSearchQuery(search_input)"
              >

            </div>
              <button v-if="search_mode" class="btn btn-outline-secondary" @click="startClearSearch" >Clear</button>
        
    </div>


</template>


<style scoped>
.search-input {
    width: 28rem;
    margin: auto;
    margin-top: 2rem;
    display: flex;
    height: 3rem;
    justify-content: space-between;
}

.search-input .input-container {
  display: flex;
  width: 24rem;
}

.search-input button {
  max-width: 4rem;
  font-size: 1rem;
}

.search-input i {
    border: 1px solid black;
    padding: 0.3rem 0.8rem;
}

</style>