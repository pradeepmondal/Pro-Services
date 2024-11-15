<script>
import AdminServices from './AdminServices.vue';
import AdminSRs from './AdminSRs.vue';
import AdminCustomers from './AdminCustomers.vue';
import AdminProfessionals from './AdminProfessionals.vue';


export default {
  name: "Tile",
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