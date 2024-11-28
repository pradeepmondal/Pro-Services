<script>

import AddCategoryForm from './service_category/AddCategoryForm.vue';
import DeleteCategoryForm from './service_category/DeleteCategoryForm.vue';
import AddServiceForm from './service_category/service/AddServiceForm.vue';
import DeleteServiceForm from './service_category/service/DeleteServiceForm.vue';
import EditServiceForm from './service_category/service/EditServiceForm.vue'
import ViewForm from './service_category/service/ViewForm.vue';
import ViewCustomer from './customer_category/ViewCustomer.vue';
import DeleteCustomer from './customer_category/DeleteCustomer.vue';
import BlockCustomer from './customer_category/BlockCustomer.vue';
import UnblockCustomer from './customer_category/UnblockCustomer.vue';
import ViewProfessional from './sp_category/ViewProfessional.vue';
import VerifyProfessional from './sp_category/VerifyProfessional.vue';
import BlockProfessional from './sp_category/BlockProfessional.vue';
import UnblockProfessional from './sp_category/UnblockProfessional.vue';
import DeleteProfessional from './sp_category/DeleteProfessional.vue';
import EditCategoryForm from './service_category/EditCategoryForm.vue';



export default {
  name: "AdminModal",
  components: {
    AddCategoryForm,
    EditCategoryForm,
    DeleteCategoryForm,
    ViewForm,
    EditServiceForm,
    AddServiceForm,
    DeleteServiceForm,
    ViewCustomer,
    DeleteCustomer,
    BlockCustomer,
    UnblockCustomer,
    ViewProfessional,
    VerifyProfessional,
    BlockProfessional,
    UnblockProfessional,
    DeleteProfessional

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
    },
    afterAction2: {
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
        <AddCategoryForm v-if="modal_type === 'add_category_form'" :afterAction="afterAction" />
        <EditCategoryForm v-if="modal_type === 'edit_category_form'" :afterAction="afterAction2" :category_obj="category_obj" />
        <DeleteCategoryForm v-if="modal_type === 'delete_form'" :obj="obj" :afterAction="afterAction" />
        <EditServiceForm v-if="modal_type === 'edit_form'" :obj="obj" :afterAction="afterAction"/>
        <ViewForm v-if="modal_type === 'view_form'" :obj="obj" :category_obj="category_obj" />
        <AddServiceForm v-if="modal_type === 'add_service_form'" :afterAction="afterAction" :category_obj="category_obj" />
        <DeleteServiceForm v-if="modal_type === 'delete_service_form'" :obj="obj" :afterAction="afterAction" />
        <ViewCustomer v-if="modal_type === 'view_customer_form'" :customer="obj" />
        <DeleteCustomer v-if="modal_type === 'delete_customer_form'" :obj="obj" :afterAction="afterAction" />
        <BlockCustomer v-if="modal_type === 'block_customer_form'" :obj="obj" :afterAction="afterAction" />
        <UnblockCustomer v-if="modal_type === 'unblock_customer_form'" :obj="obj" :afterAction="afterAction" />
        <ViewProfessional v-if="modal_type === 'view_sp_form'" :sp="obj" :afterAction="afterAction" />
        <VerifyProfessional v-if="modal_type === 'verify_sp_form'" :sp="obj" :afterAction="afterAction" />
        <BlockProfessional v-if="modal_type === 'block_sp_form'" :obj="obj" :afterAction="afterAction" />
        <UnblockProfessional v-if="modal_type === 'unblock_sp_form'" :obj="obj" :afterAction="afterAction" />
        <DeleteProfessional v-if="modal_type === 'delete_sp_form'" :obj="obj" :afterAction="afterAction" />
      </div>
      <div class="modal-footer">
        
        
      
        
      </div>
    </div>
  </div>
</div>


        
    </div>


</template>


<style scoped>


</style>