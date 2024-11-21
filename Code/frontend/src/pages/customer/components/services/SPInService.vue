<script>





export default {
  name: "SPInService",
  props: {
    selected_service : {
        type: Object 
    },
    service_professionals: {
        type: Object
    },
    bookService: {
      type: Function
    }
  },
  components: {
    
    

  },

  data(){
    return {
      customer: this.$store.state.user_details,
      

        
        
    }
  },

};
</script>

<template>
 
        
   <div>

    
    
</div>

<div class="container services-table">
    <table class="table table-striped">
<thead>
<tr>
  <th scope="col">#</th>
  <th scope="col">Professional Name</th>
  <th scope="col">Price</th>
  <th scope="col">Rating</th>
  <th scope="col">Action</th>
</tr>
</thead>
<tbody>
<tr v-for="(sp, index) in service_professionals">
  <td scope="row"><div class="sp_index" >{{ index+1 }}</div></td>
  <td>{{ sp.f_name + ' ' + sp.l_name }}</td>
  <td>₹{{ sp.price }}</td>
  <td>{{ sp.rating }}</td>
  <td><div class="button-container">
    <button class="btn btn-outline-success" @click="bookService(sp)">
                Book
            </button>
    
  </div></td>
</tr>

</tbody>
</table>
</div>
    


</template>


<style scoped>


</style>