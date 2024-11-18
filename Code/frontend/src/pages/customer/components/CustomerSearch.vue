<script>
export default {
  name: "CustomerSearch",
  data(){
    return {
        search_input: null
    }
  }
};
</script>

<template>
    <div class="search-input">
        <i class="bi bi-search"></i>
        <input
                type="text"
                class="form-control"
                placeholder="Search"
                
                aria-label="Search"
                aria-describedby="basic-addon1"
                v-model="search_input"
              >
        
    </div>


</template>


<style scoped>
.search-input {
    width: max-content;
    margin: auto;
    margin-top: 2rem;
    display: flex;
}

.search-input i {
    border: 1px solid black;
    padding: 0.3rem 0.8rem;
}

</style>