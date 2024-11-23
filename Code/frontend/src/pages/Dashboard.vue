<script>
import CustomerDashboard from './customer/CustomerDashboard.vue'
import AdminDashboard from './admin/AdminDashboard.vue'
import SPDashboard from './sp/SPDashboard.vue'



export default {
  components : {
    CustomerDashboard,
    AdminDashboard,
    SPDashboard
  },
  name: "Dashboard",
  data() {
    return {
        user_type: this.$store.state.user_type
    }
  },
  methods: {

  }
}

</script>


<template>
    <AdminDashboard v-if="user_type === 'admin'" />
    <CustomerDashboard v-if="user_type === 'customer'" />
    <SPDashboard v-if="user_type === 'sp'" />

</template>