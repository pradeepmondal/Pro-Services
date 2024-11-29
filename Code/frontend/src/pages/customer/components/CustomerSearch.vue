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

              <div v-if="search_param_req" class="select-container" > <label>Search By:</label> 
              <select v-if="search_in === 'admin_srs'"  class="form-select " v-model="search_param" @change="updateSearchQuery(search_input, search_param)" >

                <option value="customer_name" selected>Customer Name</option>
                <option value="professional_name" >Professional Name</option>
                <option value="service_name" >Service Name</option>
                <option value="description" >Description</option>
              </select>

              <select v-if="search_in === 'customer_srs'"  class="form-select " v-model="search_param" @change="updateSearchQuery(search_input, search_param)" >

              
              <option value="professional_name" selected>Professional Name</option>
              <option value="service_name" >Service Name</option>
              <option value="status" >Status</option>
              </select>




              <select v-if="search_in === 'admin_customers'"  class="form-select " v-model="search_param" @change="updateSearchQuery(search_input, search_param)" >
              <option value="email" selected>Email</option>
              <option value="customer_name" >Customer Name</option>
              <option value="address" >Address</option>
              <option value="pincode" >Pincode</option>
              </select>


              <select v-if="search_in === 'admin_professionals'"  class="form-select " v-model="search_param" @change="updateSearchQuery(search_input, search_param)" >
              <option value="email" selected>Email</option>
              <option value="professional_name">Professional Name</option>
              <option value="service_name">Service Name</option>
              <option value="pincode">Pincode</option>
              </select>
            </div>
        
    </div>

    


</template>


<style scoped>
.search-input {
    width: 40rem;
    margin: auto;
    margin-top: 2rem;
    display: flex;
    height: 3rem;
    justify-content: space-evenly;
    
}

.search-input .input-container {
  display: flex;
  width: 24rem;
  
}

.search-input button {
  max-width: 4rem;
  font-size: 1rem;
}

.search-input input {
  
  background-color: rgb(253, 243, 229);
  border: 1px solid black;
}

.search-input i {
    border: 1px solid black;
    padding: 0.3rem 0.8rem;
}

.select-container {
  max-width: max-content;
  display: flex;
  
  
  
}

.select-container select {
  background-color: rgb(253, 243, 229);
  
  
}
  
  


.select-container label {
  width: 12rem;
  margin: 1rem 0rem;
  margin-left: 1rem;

  
}

.search-container {
  display: flex;
  max-width: fit-content;

}



</style>