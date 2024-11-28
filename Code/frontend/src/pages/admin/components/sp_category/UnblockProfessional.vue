<script>


export default {
  name: "UnblockProfessionalForm",
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
      sp: this.obj
        
        
    }
  },
  methods : {
    async unblockSP(obj) {
        this.sp.active = 'unblock'
      try {
        const res = await fetch(
          "http://localhost:5050" + "/sp/" + obj.sp_id,
          {
            method: "PUT",
            headers: {
              "content-type": "application/json",
              "auth-token": this.$store.state.auth_token,
            },
            body: JSON.stringify(this.sp)
            
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
      
        <div>Unblock {{ obj.f_name }}</div> <br />
        <p><strong>Warning:</strong> This will unblock access to all the services.</p>
        <div v-if="message">{{ message }}</div>
        <button type="button" class="btn btn-success" @click="unblockSP(obj)">Unblock</button>
        
    </div>


</template>


<style scoped>


</style>