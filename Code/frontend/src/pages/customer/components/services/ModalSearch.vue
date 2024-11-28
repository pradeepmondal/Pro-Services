<script>
export default {
  name: "CustomerSearch",
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
    },

    search_param_req: {
      type: Boolean
    },
    search_in: {
      type: String
    }

    
  },
  data(){
    return {
        search_input: null,
        search_param: null
    }
  },

  methods: {
    startClearSearch() {
      this.search_input = null;
      this.search_param = null;
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
                @change="updateSearchQuery(search_input, search_param)"
              >

            </div class="search-container" >
            
              <button v-if="search_mode" class="btn btn-outline-secondary" @click="startClearSearch" >Clear</button>

              <div v-if="search_param_req" class="select-container" > <label> By:</label> 
              


              <select v-if="search_in === 'select_professionals'"  class="form-select " v-model="search_param" @change="updateSearchQuery(search_input, search_param)" >
              
              <option value="professional_name">Professional Name</option>
              <option value="rating">Rating</option>
              <option value="pincode">Pincode</option>
              </select>
            </div>
        
    </div>

    


</template>


<style scoped>
.search-input {
    width: 27rem;
    margin: auto;
    margin-top: 2rem;
    margin-bottom: 2rem;
    display: flex;
    height: 2.5rem;
    justify-content: space-evenly;
}

.search-input .input-container {
  display: flex;
  width: 18rem;
}

.search-input button {
  max-width: 3rem;
  font-size: 1rem;
}

.search-input i {
    border: 1px solid black;
    padding: 0.3rem 0.8rem;
}

.select-container {
  max-width: max-content;
  display: flex;
  
  
}

.select-container label {
  width: max-content;
  
  margin: 0 1rem ;
  margin-top: 0.5rem;

  
}

.search-container {
  display: flex;
  max-width: fit-content;

}



</style>