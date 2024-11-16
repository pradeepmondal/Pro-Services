<script>
import Navbar from '.././components//Navbar.vue';
import AdminModal from '.././components/AdminModal.vue';
import AdminSearch from '.././components/AdminSearch.vue';

export default {
  name: "AdminServicesInCategory",
  props: ['cat_id'],
  components: {
    Navbar,
    AdminSearch,
    AdminModal

  },
  data(){
    return {
        email: this.$store.state.email,
        services: null,
        modal_type: null,
        obj: null,
        modal_heading: null
        
        
    }
  },
  async created() {
    await this.fetchServices()
  },

  methods: {
    async fetchServices() {
        try{
        const res = await fetch('http://localhost:5050' + '/services/' + this.cat_id , {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.services = data



        }
    }catch(e){
        console.error(e)
    }
        
        


    },
    deleteService(service){
        this.modal_type = "delete_form"
        this.obj = service
        this.modal_heading = "Delete " + service.name
    },

    editService(service){
        this.modal_type = "edit_form"
        this.obj = service
        this.modal_heading = "Edit " + service.name
    },

    viewService(service){
        this.modal_type = "view_form"
        this.obj = service
        this.modal_heading = service.name
    }


  }
};
</script>

<template>
    
    <Navbar :email/>
    <AdminModal :modal_type="modal_type" :obj="obj" :heading="modal_heading"/>
<div>
    <AdminSearch />
    
    
    
    <div>Services in category {{ cat_id }}</div>
    
    
    </div>

    <div class="container services-table">
        <table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Service Name</th>
      <th scope="col">Base Price</th>
      <th scope="col">Action</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="service in services">
      <td scope="row"><div class="service_id" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="viewService(service)">{{ service.s_id }}</div></td>
      <td>{{ service.name }}</td>
      <td>₹{{ service.price }}</td>
      <td><div class="button-container">
        <button class="btn btn-outline-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="editService(service)">
                    Edit

                </button>
        <button class="btn btn-outline-danger" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="deleteService(service)">
                    Delete

                </button>
      </div></td>
    </tr>

  </tbody>
</table>
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

.service_id {
    text-decoration: underline;
    cursor: pointer;

}



</style>