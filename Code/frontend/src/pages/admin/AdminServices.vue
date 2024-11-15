<script>

import AdminSearch from './components/AdminSearch.vue';
import CategoryTiles from './components/CategoryTiles.vue';
import Navbar from './components/Navbar.vue';

export default {
  name: "Services",
  components: {
    Navbar,
    AdminSearch,
    CategoryTiles
  },

  data(){
    return {
      email: this.$store.state.email
        
        
    }
  }
};
</script>

<template>
  <Navbar :email />
    <div class="">
      <AdminSearch />
        <div>Services</div>
        <CategoryTiles />


        
    </div>


</template>


<style scoped>


</style>