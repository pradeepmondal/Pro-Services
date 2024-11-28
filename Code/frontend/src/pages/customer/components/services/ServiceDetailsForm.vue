<script>





export default {
  name: "ServiceDetailsForm",
  props: {
    selected_service : {
        type: Object 
    },
    service_professionals: {
        type: Object
    },
    showSPs: {
      type: Function
    }
  },
  components: {
    
    

  },

  data(){
    return {
      customer: this.$store.state.user_details,
      service: null,
      loading: true
      

        
        
    }
  },

  mounted() {
    this.loading = false

  },




  methods: {

  }

};
</script>

<template>
    <div v-if="!selected_service">Loading...</div>
<div class="details-container" v-else>
    <div class="service-heading">
        {{ selected_service.name }}


    </div>

    <div class="service-description">
        {{ selected_service.description }}

    </div>

    <div class="service-time-required">
        Average Time Required: <span>{{ selected_service.req_time }} hour</span>

    </div>

    <div class="service-time-required">
        Prices: Strating From: <span>₹{{ selected_service.base_price }} </span>

    </div>

    <button class="btn btn-outline-success" @click="showSPs(selected_service)">Book Now</button>


    


</div>
    
    
    
    
    

</template>


<style scoped>

.details-container {
    display: flex;
    flex-direction: column;

}

.service-heading {
    font-size: 1.5rem;
}

.service-description {
    padding: 1rem;
}



.service-time-required span{
    font-weight: 700
}

button {
    margin: 1rem 0;
}

</style>