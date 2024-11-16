<script>
import AdminServices from './services/AdminServices.vue';
import AdminSRs from './srs/AdminSRs.vue';
import AdminCustomers from './customers/AdminCustomers.vue';
import AdminProfessionals from './professionals/AdminProfessionals.vue';


export default {
  name: "AdminDisplayCategory",
  props: ['category'],
  components: {
    AdminServices,
    AdminSRs,
    AdminCustomers,
    AdminProfessionals

  },
  data(){
    return {
        
        
    }
  }
};
</script>

<template>
    <AdminServices v-if="category === 'services'" />
    <AdminSRs v-if="category === 'srs'" />
    <AdminCustomers v-if="category === 'customers'" />
    <AdminProfessionals v-if="category === 'professionals'" />


            

        
    


</template>


<style scoped>

</style>