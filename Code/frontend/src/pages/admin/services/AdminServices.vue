<script>

import AdminModal from '.././components/AdminModal.vue';

import AdminSearch from '.././components/AdminSearch.vue';
import CategoryTiles from '.././components/CategoryTiles.vue';
import Navbar from '.././components//Navbar.vue';

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
      d_category: null,
      obj: null,
      search_mode: false,
      search_query: null
        
        
    }
  },
  async created() {
    await this.fetchServices()
  },

  computed: {
    final_categories(){
      if(!this.search_mode){
        return this.categories
      }
      else{
        let search_query = this.search_query.toLowerCase()
        let regex = new RegExp(search_query, 'i')
        return this.categories.filter((cat) => {
          return (
            regex.test(cat.name) || regex.test(cat.description)
          )
        })

      }
    }

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

    updateSearchQuery(search_input){
      this.search_mode = true
      this.search_query = search_input
    },

    clearSearch(){
      this.search_mode = false
    },

    addCategory() {
      this.modal_form = 'add_category_form'
      this.modal_heading = 'Add a New Category'


    },
    deleteCategory(category) {
      this.modal_form = 'delete_form'
      this.modal_heading = 'Delete'
      this.obj = category
    }
  }
};
</script>

<template>
  <Navbar :email />
  <AdminModal :modal_type="modal_form" :heading="modal_heading" :obj="obj" :afterAction="fetchServices" />
    <div class="">
      <AdminSearch search_placeholder="Search in Service Categories" :updateSearchQuery="updateSearchQuery" :clearSearch="clearSearch" :search_mode="search_mode"/>
        <div>Services</div>
        <CategoryTiles :addCategory="addCategory" :deleteCategory="deleteCategory" :categories="final_categories" :d_category="d_category"/>


        
    </div>


</template>


<style scoped>


</style>