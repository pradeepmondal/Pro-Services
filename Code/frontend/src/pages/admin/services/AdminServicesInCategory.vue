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
        modal_heading: null,
        category_obj: null,
        search_mode: false,
        search_query: null
      
        
        
        
    }
  },
  async created() {
    await this.fetchServices()
    await this.fetchCategory()
  },

  computed: {
    final_services(){
      if(!this.search_mode){
        return this.services
      }
      else{
        let search_query = this.search_query.toLowerCase()
        let regex = new RegExp(search_query, 'i')
        return this.services.filter((service) => {
          return (
            regex.test(service.name) || regex.test(service.description) 
          )
        })

      }
    }
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


    updateSearchQuery(search_input){
      this.search_mode = true
      this.search_query = search_input
    },

    clearSearch(){
      this.search_mode = false
    },




    async fetchCategory() {
      try {
        const res = await fetch(
          "http://localhost:5050" + "/service_category/"+this.cat_id ,
          {
            method: "GET",
            headers: {
              "content-type": "application/json",
              "auth-token": this.$store.state.auth_token,
            },
          }
        );
        if (res.ok) {
          const data = await res.json();
          this.category_obj = data;
        }
        
      } catch (e) {
        console.log(e);
        
        
      }
    },

    deleteService(service){
        this.modal_type = "delete_service_form"
        this.obj = service
        this.modal_heading = "Delete " + service.name
    },

    editService(service){
        this.modal_type = "edit_form"
        this.obj = service
        this.modal_heading = "Edit " + service.name
    },

    editCategory(category_obj){
        this.modal_type = "edit_category_form"
        this.obj = category_obj
        this.modal_heading = "Edit " + category_obj.name
    },

     viewService(service){
        this.modal_type = "view_form"
        this.obj = service
        this.modal_heading = service.name
        
        
    },
    addService(){
        this.modal_type = "add_service_form"
        this.modal_heading = "Add a New Service"

        
    },


  }
};
</script>

<template>
    
    <Navbar :email/>
    <AdminModal :modal_type="modal_type" :obj="obj" :category_obj="category_obj" :heading="modal_heading" :afterAction="fetchServices" :afterAction2="fetchCategory"/>
<div>
  <div class="container">
    <AdminSearch search_placeholder="Search in Services" :updateSearchQuery="updateSearchQuery" :search_mode="search_mode" :clearSearch="clearSearch" />
    
    
    <div class="header-container">
    <div class="heading">Services in {{ category_obj.name }}
      <button class="btn btn-outline-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="editCategory(category_obj)">
                    Edit

                </button>


    </div>

    <button class="btn btn-outline-success" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="addService">
                    Add a Service

                </button>
  </div>
    
    
<div v-if="!services.length">
  No Services Found !
</div>
    <div v-else class="services-table">
        <table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Service Name</th>
      <th scope="col">Time Required</th>
      <th scope="col">Base Price</th>
      <th scope="col">Description</th>
      <th scope="col">Action</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="service in final_services">
      <td scope="row"><div class="service_id"  >{{ service.s_id }}</div></td>
      <td>{{ service.name }}</td>
      <td>{{ service.req_time }} hour</td>
      <td>₹{{ service.base_price }}</td>
      <td>{{ service.description }}</td>
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

.service_id {
    text-decoration: underline;
    cursor: pointer;

}

.heading {
  
  padding: 2rem;
  font-size: 1.5rem;
}

.heading button {
  font-size: 0.8rem;
  padding: 0.4rem;
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-container > button {
  max-height: fit-content;
}



</style>