<script>
export default {
  name: "CustomerNotification",
  props: {
    customer: {
        type: Object
    },
    addAddress: {
      type: Function
    }
    
  },
  data(){
    return {
        
    }
  }
};
</script>

<template>
    <div v-if="!this.customer.address" class="notification">
        <i class="bi bi-exclamation-octagon-fill"></i>
        <div v-if="!this.customer.address">No address found !! 
            <button class="btn btn-primary add-address" @click="addAddress">Add Address</button>
        </div>
        
    </div>


</template>


<style scoped>
.notification {
    width: max-content;
    right: 0;
    margin-top: 1rem;
    margin-right: 1rem;
    display: flex;
    background-color: rgb(242, 207, 143);
    padding: 0.5rem;
    border: 1px solid orange;
    border-radius: 0.75rem;
    position: absolute;
}

.notification i {
    color: red;
    font-size: 1.1rem;
    padding: 0.3rem 0.8rem;
}

</style>