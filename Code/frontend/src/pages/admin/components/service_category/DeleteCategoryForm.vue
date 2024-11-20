<script>


export default {
  name: "DeleteCategoryForm",
  props: {
    d_category: {
        type: Object
    },
    obj: {
      type: Object
    },
    afterAction: {
      type: Function
    }
  },

  components: {

  },
  data(){
    return {
      email: this.$store.state.email,
      message: null,
        
        
    }
  },
  methods : {
    async deleteCategory(obj) {
      try {
        const res = await fetch(
          "http://localhost:5050" + "/service_category/" + obj.cat_id,
          {
            method: "DELETE",
            headers: {
              "content-type": "application/json",
              "auth-token": this.$store.state.auth_token,
            },
            
          }
        );
        if (res.ok) {
          const data = await res.json();
          this.message = data
          this.afterAction()

        }
      } catch (e) {
        console.error(e);
      }
    }
  }
};
</script>

<template>
  <Navbar :email />
    <div class="">
      
        <div>Delete {{ obj.name }}</div> <br />
        <p><strong>Warning:</strong> This will delete all the related service, service_requests and SPs</p>
        <div v-if="message">{{ message }}</div>
        <button type="button" class="btn btn-danger" @click="deleteCategory(obj)">Delete</button>
        
    </div>


</template>


<style scoped>


</style>