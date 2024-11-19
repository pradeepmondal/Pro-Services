<script>

import AddCategoryForm from './service_category/AddCategoryForm.vue';
import DeleteCategoryForm from './service_category/DeleteCategoryForm.vue';
import EditServiceForm from './service_category/EditServiceForm.vue'
import ViewForm from './service_category/ViewForm.vue';



export default {
  name: "AdminModal",
  components: {
    AddCategoryForm,
    DeleteCategoryForm,
    ViewForm,
    EditServiceForm

  },
  props: {
    modal_type: {
        type: String,
        required: true
    },
    heading: {
        type: String
    },
    d_category: {
        type: Object
    },
    obj: {
      type: Object
    },
    category_obj: {
      type: Object
    },

    afterAction: {
      type: Function
    }

  },


  data(){
    return {
      email: this.$store.state.email
        
        
    }
  }
};
</script>

<template>
  <Navbar :email />
    <div class="">
      <!-- Button trigger modal
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
  Launch static backdrop modal
</button> -->

<!-- Modal -->
<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="staticBackdropLabel">{{ heading }}</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <AddCategoryForm v-if="modal_type === 'add_category_form'" />
        <DeleteCategoryForm v-if="modal_type === 'delete_form'" :obj="obj"/>
        <EditServiceForm v-if="modal_type === 'edit_form'" :obj="obj" :afterAction="afterAction"/>
        <ViewForm v-if="modal_type === 'view_form'" :obj="obj" :category_obj="category_obj" />

        
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button v-if="modal_type === 'add_category_form'" type="button" class="btn btn-success">Create</button>
        <button v-if="modal_type === 'delete_form'" type="button" class="btn btn-danger">Delete</button>
        <button v-if="modal_type === 'edit_form'" type="button" class="btn btn-success">Confirm Edit</button>
      </div>
    </div>
  </div>
</div>


        
    </div>


</template>


<style scoped>


</style>