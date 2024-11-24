<script>







export default {
  name: "SRActionModal",
  components: {

    

  },
  props: {
    selected_sr : {
        type: Object
    },
    action: {
      type: Function
    },

    modal_type: {
        type: String
    },
    modal_heading: {
        type: String
    }


  },


 data(){
    return {
      customer: this.$store.state.user_details,

      remarks: null
      
      
      

        
        
    }
  },
  
//   async created() {
//     try {
//       await this.fetchSPs()
//     } catch (e) {
//       console.error(e)

//     } finally {
//       this.loading = false
//     }
//   },

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
        
         <div v-if="modal_type === 'accept_sr'">Accept SR #{{ selected_sr.sr_id }} by {{ selected_sr.customer_name }} </div>
         <div v-if="modal_type === 'reject_sr'">Reject SR #{{ selected_sr.sr_id }} by {{ selected_sr.customer_name }} </div>
         <div v-if="modal_type === 'mark_close_sr'">Mark SR #{{ selected_sr.sr_id }} by {{ selected_sr.customer_name }} as closed</div>
         <div class="remarks-container" >
            <label>Remarks:</label>
            <input type="text" v-model="remarks" />
         </div>
        
      </div>
      <div class="modal-footer">
        <button v-if="modal_type === 'accept_sr'" type="button" class="btn btn-success" @click="action(selected_sr, remarks)" data-bs-dismiss="modal">Accept</button>
        <button v-if="modal_type === 'reject_sr'" type="button" class="btn btn-danger" @click="action(selected_sr, remarks)" data-bs-dismiss="modal">Reject</button>
        <button v-if="modal_type === 'mark_close_sr'" type="button" class="btn btn-secondary" @click="action(selected_sr, remarks)" data-bs-dismiss="modal">Mark Close</button>
        
      </div>
    </div>
  </div>
</div>


        
    </div>


</template>


<style scoped>

.remarks-container {
    padding: 1rem;
    display: flex;
    flex-direction: column;
    
}

.remarks-container input {
  
  margin-top: 1rem;
  max-width: max-content;
}


</style>