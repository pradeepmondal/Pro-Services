<script>

import AdminServicesStats from './services/AdminServicesStats.vue';
import AdminSRsStats from './srs/AdminSRsStats.vue';
import AdminCustomersStats from './customers/AdminCustomersStats.vue';
import AdminProfessionalsStats from './professionals/AdminProfessionalsStats.vue';


export default {
  name: "AdminDisplayCategory",
  props: ['category'],
  components: {
    AdminServicesStats,
    AdminSRsStats,
    AdminCustomersStats,
    AdminProfessionalsStats

  },
  data(){
    return {
        
        
    }
  }
};
</script>

<template>
    <AdminServicesStats v-if="category === 'services'" />
    <AdminSRsStats v-if="category === 'srs'" />
    <AdminCustomersStats v-if="category === 'customers'" />
    <AdminProfessionalsStats v-if="category === 'professionals'" />


            

        
    


</template>


<style scoped>

</style>