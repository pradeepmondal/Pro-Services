<script>






export default {
  name: "ViewCustomer",
  components: {


  },

  props: {
    customer: {
        type: Object
    },

  },


  data() {
    return {

      message: null,
      loading: true
      
    };
  },

  async created() {
    try {
      
    } catch (e) {
      console.error(e)

    } finally {
      this.loading = false
    }
  },


  methods: {





  },
};
</script>

<template>

  <div class="container-fluid">
   


    <div class="form-conatainer">
    <form class="edit-form">
      <div class="form-content">
        <label class="form-label"   ><strong>Customer Id: </strong>{{ customer.c_id }}</label
        ><br />
       

        <div class="name-container">
          <div class="fname-container">
            <label for="name" class="form-label">First Name</label>
            <label
              type="text"
              class="form-control"
              id="f_name"
              name="f_name">{{ customer.f_name }}</label>
          </div>

          <div class="lname-container">
            <label for="price" class="form-label">Last Name</label>
            <label
              type="text"
              class="form-control"
              id="l_name"
              name="l_name"
              
              
            >{{ customer.l_name }}</label>
          </div>
        </div>
        <br />


        <div class="name-container">
          <div class="address-container">
            <label for="name" class="form-label">Address: </label>
            <label
              type="text"
              class="form-control"
              id="address"
              name="address"
              
              
              
            >{{ customer.address }}</label>
          </div>

          <div class="pincode-container">
            <label for="price" class="form-label">Pincode:</label>
            <label
              type="text"
              class="form-control"
              id="pincode"
              name="pincode"
              
              
            >{{ customer.loc_pincode }}</label>
          </div>
        </div>
        <br />

        
        <div class="name-container">
            <div>

          <label for="description" class="form-label"
            >Description: </label
          >

          



          
          <label
            class="form-control"
            id="description"
            
            name="description"
            
            
          >{{ customer.description }}</label>

        </div>
        </div>
      </div>
      <div v-if="message">{{ message }}</div>

      
    </form>
  </div>
   

    
  </div>
</template>

<style scoped>
.name-container {
  display: flex;
  justify-content: space-between;

}



.name-container * {
  margin: 0 1rem;
 
}





.form-content {
    display: flex;
    flex-direction: column;
    max-width: fit-content;
    margin: 0;
    
   
    
    
}
</style>
















