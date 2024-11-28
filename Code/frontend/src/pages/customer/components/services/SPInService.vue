<script>

import ModalSearch from './ModalSearch.vue'





export default {
  name: "SPInService",
  components: {
    ModalSearch
  },
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


  data(){
    return {
      customer: this.$store.state.user_details,
      search_mode: false,
      search_query: null,
      search_param: null,
      

        
        
    }
  },

  computed: {

final_sps(){
  if(!this.search_mode){
    return this.service_professionals
  }
  else{
    let search_query = this.search_query.toLowerCase()
    let search_param = this.search_param
    let regex = new RegExp(search_query, 'i')
    return this.service_professionals.filter((sp) => {
        if(search_param === 'professional_name'){
          return regex.test(sp.f_name + ' ' + sp.l_name )
        }
        else if(search_param === 'pincode'){
          return regex.test(sp.loc_pincode)
        }
      
        else if(search_param === 'rating'){
          return regex.test(sp.rating)
        }
         
     
    })

  }
},

},

  methods: {
    updateSearchQuery(search_input, search_param){
      this.search_mode = true
      this.search_query = search_input
      this.search_param = search_param
    },

    clearSearch(){
      this.search_mode = false
    },


  }

};
</script>

<template>
 
<div class="search-container">

  <ModalSearch search_placeholder="Search Professionals" :updateSearchQuery="updateSearchQuery" :clearSearch="clearSearch" :search_mode="search_mode" search_param_req="true" search_in="select_professionals" />
</div>
 
<div class="container services-table">
  
    <table class="table table-striped">
<thead>
<tr>
  <th scope="col">#</th>
  <th scope="col">Professional Name</th>
  <th scope="col">Pincode</th>
  <th scope="col">Price</th>
  <th scope="col">Rating</th>
  <th scope="col">Action</th>
</tr>
</thead>
<tbody>
<tr v-for="(sp, index) in final_sps">
  <td scope="row"><div class="sp_index" >{{ index+1 }}</div></td>
  <td>{{ sp.f_name + ' ' + sp.l_name }}</td>
  <td>{{ sp.loc_pincode }}</td>
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
.search-container {
  width: 4rem;
}


</style>