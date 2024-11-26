<script>
import Navbar from '.././components//Navbar.vue';
import AdminModal from '.././components/AdminModal.vue';
import AdminSearch from '.././components/AdminSearch.vue';

export default {
  name: "AdminSPs",

  components: {
    Navbar,
    AdminSearch,
    AdminModal
  },
  data() {
    return {
      email: this.$store.state.email,
      sps: null,
      modal_type: null,
      obj: null,
      modal_heading: null,
      s_no: 0
    };
  },

  async created() {
    await this.fetchSPs()
  },

  methods: {
    async fetchSPs() {
        try{
        const res = await fetch('http://localhost:5050' + '/sps/0' , {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.sps = data



        }
    }catch(e){
        console.error(e)
    }
        
        


    },
    blockSP(customer){
        this.modal_type = "block_form"
        this.obj = customer
        this.modal_heading = "Block " + customer.f_name
    },

    unblockSP(customer){
        this.modal_type = "unblock_form"
        this.obj = customer
        this.modal_heading = "Edit " + customer.f_name
    },

    viewSP(customer){
        this.modal_type = "view_sp_form"
        this.obj = sp
        this.modal_heading = sp.f_name
    },

    deleteSP(customer){
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
    <div>Service Professionals</div>

    <div class="container services-table">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Email</th>
            <th scope="col">Professional Name</th>
            <th scope="col">Service Name</th>
            <th scope="col">Rating</th>
            <th scope="col">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(sp, index) in sps">
            <td scope="row">
              <div>
                {{ index+1 }}
              </div>
            </td>
            <td><div class="sp_email" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="viewSP(sp)">{{ sp.email }}</div></td>
            <td>{{ sp.f_name + ' ' + sp.l_name }}</td>
            <td>{{ sp.service.name }}</td>
            <td>{{ sp.rating }}</td>
            <td>
              <div class="button-container">
                <button
                  v-if="sp.active"
                  class="btn btn-outline-danger"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="blockSP(sp)"
                >
                  Block
                </button>

                <button
                  v-if="!sp.active"
                  class="btn btn-outline-success"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="unblockSP(sp)"
                >
                  Unblock
                </button>

                <button
                  class="btn btn-outline-danger"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="deleteSP(sp)"
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

.sp_email {
    text-decoration: underline;
    cursor: pointer;

}



</style>
