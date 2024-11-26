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
      s_no: 0
    };
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
    blockCustomer(customer){
        this.modal_type = "block_form"
        this.obj = customer
        this.modal_heading = "Block " + customer.f_name
    },

    unblockCustomer(customer){
        this.modal_type = "unblock_form"
        this.obj = customer
        this.modal_heading = "Edit " + customer.f_name
    },

    viewCustomer(customer){
        this.modal_type = "view_customer_form"
        this.obj = customer
        this.modal_heading = customer.f_name
    },

    deleteCustomer(customer){
      this.modal_type = "delete_form"
      this.obj = customer
      this.modal_heading = "Delete " + customer.f_name

    }


  },
  computed: {
    incrementedSno(){
      this.s_no++
      return this.s_no
    }
  }
};
</script>

<template>
  <Navbar :email />
  <AdminModal :modal_type="modal_type" :obj="obj" :heading="modal_heading" />
  <div class="">
    <AdminSearch />
    <div>Customers</div>

    <div class="container services-table">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Email</th>
            <th scope="col">Customer Name</th>
            <th scope="col">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(customer, index) in customers">
            <td scope="row">
              <div>
                {{ index+1 }}
              </div>
            </td>
            <td><div class="customer_email" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="viewCustomer(customer)">{{ customer.email }}</div></td>
            <td>{{ customer.f_name + ' ' + customer.l_name }}</td>
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



</style>
