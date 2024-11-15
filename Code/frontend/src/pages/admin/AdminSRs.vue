<script>

import AdminSearch from './components/AdminSearch.vue';
import Navbar from './components/Navbar.vue';

export default {
  name: "SRs",

  components: {
    Navbar,
    AdminSearch
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
        <div>Srs</div>


        
    </div>


</template>


<style scoped>


</style>