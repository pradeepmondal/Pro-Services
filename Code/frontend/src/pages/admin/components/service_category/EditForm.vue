<script>


export default {
  name: "EditForm",
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
      
        <div>Edit {{ obj.name }}</div>


        
    </div>


</template>


<style scoped>


</style>