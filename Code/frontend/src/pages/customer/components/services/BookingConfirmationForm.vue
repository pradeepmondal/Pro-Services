<script>





export default {
  name: "BookingConfirmationForm",
  props: {
    selected_service : {
        type: Object 
    },
    selected_sp: {
        type: Object
    },
    customer: {
        type: Object
    },
  },
  components: {
    
    

  },

  data(){
    return {
      
      payment_status: true, // should be initially false if payment gateway implemented
      formData: {
        s_id: this.selected_service.s_id,
        c_id: this.customer.c_id,
        sp_id: this.selected_sp.sp_id,
        description: null,
        status: 'Requested',
        
    

      },
      message: null
      

        
        
    }
  },


  methods: {


    async confirmBooking() {
      

      
      try {
        const res = await fetch(
          "http://localhost:5050" + "/service_request",
          {
            method: "POST",
            headers: {
              "content-type": "application/json",
              "auth-token": this.$store.state.auth_token,
            },
            body: JSON.stringify(this.formData)
          }
        );
        if (res.ok) {
          const data = await res.json();
          this.message = data
          

        }
      } catch (e) {
        console.error(e);
      }
    }
  }
};
</script>

<template>
 
        
   
<div>
    
    <div class="mb-3">
    {{ selected_service.name }} by {{ selected_sp.f_name }}
</div>
<div class="mb-3">
    Rating: {{ selected_sp.rating }}
</div>

<div class="mb-3">
    My Address: {{ customer.address }}, {{ customer.loc_pincode }}
</div>
    <div class="mb-3">
          <label for="description" class="form-label"
            >Add Description</label
          >
          <textarea
            class="form-control"
            id="description"
            rows="3"
            name="description"
            v-model="formData.description"
          ></textarea>
        </div>
        <div class="message-container">
            {{ this.message }}
        </div>

        <div class="pay_button">
            <button class="btn btn-outline-success" @click="confirmBooking()">
                Pay ₹{{ selected_sp.price }}
            </button>
        </div>


</div>
    


</template>


<style scoped>
.pay_button {
    display: flex;
    flex-direction: row-reverse;
}

.message-container {
    background-color: green;
    color: aliceblue;
    max-width: fit-content;
}

</style>