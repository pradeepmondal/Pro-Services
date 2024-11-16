<script>


export default {
  name: "VueForm",
  props: {
    obj: {
      type: Object
    }
  },

  components: {

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
      
        <div>{{ obj.name }}</div>


        
    </div>


</template>


<style scoped>


</style>