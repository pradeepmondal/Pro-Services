<script>

import SPInService from './SPInService.vue';





export default {
  name: "ServiceBookingModal",
  components: {
    SPInService
    
    

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
      customer: this.$store.state.userDetails,
      show_sps: true,
      modal_heading: 'Select Professional'

        
        
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
        <SPInService v-if="show_sps" :selected_service="selected_service" :service_professionals="service_professionals" />
        

        
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        
      </div>
    </div>
  </div>
</div>


        
    </div>


</template>


<style scoped>


</style>