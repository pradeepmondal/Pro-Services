<script>


export default {
  name: "DeleteCategoryForm",
  props: {
    d_category: {
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
      
        <div>Delete {{ d_category.name }}</div>


        
    </div>


</template>


<style scoped>


</style>