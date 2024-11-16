<script>

import AdminSearch from '.././components/AdminSearch.vue';
import Navbar from '.././components/Navbar.vue';

export default {
  name: "Customers",

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
        <div>Customers</div>


        
    </div>


</template>


<style scoped>


</style>