<script>
import Navbar from '.././components//Navbar.vue';
import AdminModal from '.././components/AdminModal.vue';
import AdminSearch from '.././components/AdminSearch.vue';

export default {
  name: "Customers",

  components: {
    Navbar,
    AdminSearch,
    AdminModal
  },
  data() {
    return {
      email: this.$store.state.email,
      customers: null,
      modal_type: null,
      obj: null,
      modal_heading: null,
      s_no: 0,
      search_mode: false,
      search_query: null,
      search_param: null
    };
  },

  computed: {
    final_customers(){
      if(!this.search_mode){
        return this.customers
      }
      else{
        let search_query = this.search_query.toLowerCase()
        let search_param = this.search_param
        let regex = new RegExp(search_query, 'i')
        return this.customers.filter((customer) => {
            if(search_param === 'customer_name'){
              return regex.test(customer.f_name + ' ' + customer.l_name )
            }
            else if(search_param === 'email'){
              return regex.test(customer.email)
            }
            else if(search_param === 'address'){
              return regex.test(customer.address)
            }
            else if(search_param === 'pincode'){
              return regex.test(customer.loc_pincode)
            }
             
         
        })

      }
    },

    incrementedSno(){
      this.s_no++
      return this.s_no
    }

  },

  async created() {
    await this.fetchCustomers()
  },

  methods: {
    async fetchCustomers() {
        try{
        const res = await fetch('http://localhost:5050' + '/customers' , {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.customers = data



        }
    }catch(e){
        console.error(e)
    }
        
        


    },

    updateSearchQuery(search_input, search_param){
      this.search_mode = true
      this.search_query = search_input
      this.search_param = search_param
    },

    clearSearch(){
      this.search_mode = false
    },




    blockCustomer(customer){
        this.modal_type = "block_customer_form"
        this.obj = customer
        this.modal_heading = "Block " + customer.f_name
    },

    unblockCustomer(customer){
        this.modal_type = "unblock_customer_form"
        this.obj = customer
        this.modal_heading = "Edit " + customer.f_name
    },

    viewCustomer(customer){
        this.modal_type = "view_customer_form"
        this.obj = customer
        this.modal_heading = customer.f_name
    },

    deleteCustomer(customer){
      this.modal_type = "delete_customer_form"
      this.obj = customer
      this.modal_heading = "Delete " + customer.f_name

    }


  },

};
</script>

<template>
  <Navbar :email />
  <AdminModal :modal_type="modal_type" :obj="obj" :heading="modal_heading" :afterAction="fetchCustomers" />
  <div class="parent-container">
    <h2 class="heading">Customers</h2>
    <AdminSearch search_placeholder="Search in Customers" :updateSearchQuery="updateSearchQuery" :clearSearch="clearSearch" :search_mode="search_mode" search_param_req="true" search_in="admin_customers"/>
    

    <div class="container customer-table">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Email</th>
            <th scope="col">Customer Name</th>
            <th scope="col">Address</th>
            <th scope="col">Pincode</th>
            
            <th scope="col">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(customer, index) in final_customers">
            <td scope="row">
              <div>
                {{ index+1 }}
              </div>
            </td>
            <td><div class="customer_email" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="viewCustomer(customer)">{{ customer.email }}</div></td>
            <td>{{ customer.f_name + ' ' + customer.l_name }}</td>
            <td>{{ customer.address }}</td>
            <td>{{ customer.loc_pincode }}</td>
            <td>
              <div class="button-container">
                <button
                  v-if="customer.active"
                  class="btn btn-outline-danger"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="blockCustomer(customer)"
                >
                  Block
                </button>

                <button
                  v-if="!customer.active"
                  class="btn btn-outline-success"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="unblockCustomer(customer)"
                >
                  Unblock
                </button>

                <button
                  class="btn btn-outline-danger"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="deleteCustomer(customer)"
                >
                  Delete
                </button>
              </div>
            </td>
            
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>

.button-container {
    max-width: fit-content;

}

.button-container button {
    margin: 0 0.4rem;
    width: fit-content;
}

.customer_email {
    text-decoration: underline;
    cursor: pointer;

}

.parent-container {
  
  
  height: 92vh;
  width:100%;
  
  background-color: antiquewhite;

}

.customer-table {
  margin-top: 2rem;
}

.heading {
  padding: 1rem;
}



</style>
