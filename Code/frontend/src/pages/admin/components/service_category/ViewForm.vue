<script>


export default {
  name: "VueForm",
  props: {
    obj: {
      type: Object
    },
    category_obj: {
      type: Object
    }
  },

  components: {

  },
  data(){
    return {
      email: this.$store.state.email,
      loading: true
        
        
    }
  },

  
};
</script>

<template>
  <Navbar :email />
  <div class="">
    <form class="edit-form">
      <div class="mb-3">
        <label class="form-label"  name="s_id" >Service Id: {{ obj.s_id }}</label
        ><br />

        <div class="name-price">
          <div class="name-container">
            <label for="name" class="form-label">Name: </label>
            <label
              
              class="form-label"
              id="name">{{ obj.name }}</label>
          </div>

          <div class="price-container">
            <label for="price" class="form-label">Price: </label>
            <label
              
              class="form-label"
              id="price"
              name="base_price">₹{{ obj.base_price }}</label>
          </div>
        </div>

        <div class="time-cat">
          <div class="time-container">
            <label for="req_time" class="form-label">Time Required: </label>
            <label
              
              class="form-label"
              id="req_time"
              name="req_time">{{ obj.req_time }} hrs</label>
          </div>

          <div class="price-container">
            <label for="category" class="form-label">Category: </label>
            <label
              
              class="form-label"
              id="category"
              name="category">{{ category_obj.name }} </label>
            
          </div>
        </div>
        <div class="mb-3">
          <label for="description" class="form-label"
            >Description: </label
          >
          <label
            class="form-label"
            id="description"
            rows="3"
            name="description"
            
            
          > {{ obj.description }}</label>
        </div>
      </div>
      

      
    </form>
  </div>


</template>


<style scoped>
.name-price {
  display: flex;
}

.time-cat {
  display: flex;
}

.name-price div {
  margin: 0 0.5rem;
}

.time-cat div {
  margin: 0 0.5rem;
}


</style>