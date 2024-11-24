<script>
import Navbar from '../components/Navbar.vue';

export default {
  name: "AdminServicesStats",
  components: {
    Navbar
  },

  props: {

  },
  data(){
    return {
        email : this.$store.state.email
        
    }
  },
  methods: {

  }
};
</script>

<template>
<Navbar :email="email"/>


</template>


<style scoped>


</style>