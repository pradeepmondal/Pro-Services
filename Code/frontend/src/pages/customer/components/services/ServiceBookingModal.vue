<script>

import BookingConfirmationForm from './BookingConfirmationForm.vue';
import SPInService from './SPInService.vue';





export default {
  name: "ServiceBookingModal",
  components: {
    SPInService,
    BookingConfirmationForm
    
    

  },
  props: {
    selected_service : {
        type: Object
    },
    afterAction: {
      type: Function
    },
    service_id : {
        type: String
    },
    service_professionals : {
        type: Object
    }

  },


 data(){
    return {
      customer: this.$store.state.user_details,
      show_sps: true,
      modal_heading: 'Select Professional',
      show_confirm_form: false,
      selected_sp: null

        
        
    }
  },
  
  async created() {
    try {
      await this.fetchSPs()
    } catch (e) {
      console.error(e)

    } finally {
      this.loading = false
    }
  },

  methods: {
    bookService(sp){
      this.show_sps = false
      this.selected_sp = sp
      this.modal_heading = "Confirm Booking"
      this.show_confirm_form = true

      
      
    }
  }
};
</script>

<template>
  <Navbar :email />
    <div class="">
      <!-- Button trigger modal
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
  Launch static backdrop modal
</button> -->

<!-- Modal -->
<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="staticBackdropLabel">{{ modal_heading }}</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <SPInService v-if="show_sps" :selected_service="selected_service" :service_professionals="service_professionals" :bookService="bookService" />
        <BookingConfirmationForm v-if="show_confirm_form" :selected_sp :selected_service="selected_service" :customer="customer" />
        

        
      </div>
      <!-- <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        
      </div> -->
    </div>
  </div>
</div>


        
    </div>


</template>


<style scoped>


</style>