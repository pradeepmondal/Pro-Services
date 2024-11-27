<script>


export default {
  name: "BlockCustomerForm",
  props: {
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
      customer: this.obj
        
        
    }
  },
  methods : {
    async blockCustomer(obj) {
        this.customer.active = 'block'
      try {
        const res = await fetch(
          "http://localhost:5050" + "/customer/" + obj.c_id,
          {
            method: "PUT",
            headers: {
              "content-type": "application/json",
              "auth-token": this.$store.state.auth_token,
            },
            body: JSON.stringify(this.customer)
            
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
      
        <div>Block {{ obj.f_name }}</div> <br />
        <p><strong>Warning:</strong> This will block access to all the services.</p>
        <div v-if="message">{{ message }}</div>
        <button type="button" class="btn btn-danger" @click="blockCustomer(obj)">Block</button>
        
    </div>


</template>


<style scoped>


</style>