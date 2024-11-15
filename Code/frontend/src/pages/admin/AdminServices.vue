<script>

import AdminModal from './components/AdminModal.vue';

import AdminSearch from './components/AdminSearch.vue';
import CategoryTiles from './components/CategoryTiles.vue';
import Navbar from './components/Navbar.vue';

export default {
  name: "Services",
  components: {
    Navbar,
    AdminSearch,
    CategoryTiles,
    AdminModal
  },

  data(){
    return {
      email: this.$store.state.email,
      categories: null,
      modal_form: null,
      modal_heading: null,
      d_category: null
        
        
    }
  },
  async created() {
    await this.fetchServices()
  },

  methods: {

    async fetchServices(){
        try{
        const res = await fetch('http://localhost:5050' + '/service_categories', {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            console.log(data);
            
            this.categories = data



        }
    }catch(e){
        console.error(e)
    }
        
        


    },

    addCategory() {
      this.modal_form = 'add_category_form'
      this.modal_heading = 'Add a New Category'


    },
    deleteCategory(category) {
      this.modal_form = 'delete_category_form'
      this.modal_heading = 'Delete'
      this.d_category = category
    }
  }
};
</script>

<template>
  <Navbar :email />
  <AdminModal :modal_type="modal_form" :heading="modal_heading" :d_category="d_category" />
    <div class="">
      <AdminSearch />
        <div>Services</div>
        <CategoryTiles :addCategory="addCategory" :deleteCategory="deleteCategory" :categories="categories" :d_category="d_category"/>


        
    </div>


</template>


<style scoped>


</style>