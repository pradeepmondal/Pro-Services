<script>
import CustomerDashboard from './customer/CustomerDashboard.vue'
import AdminDashboard from './admin/AdminDashboard.vue'

export default {
  components : {
    CustomerDashboard,
    AdminDashboard
  },
  name: "Dashboard",
  data() {
    return {
        user_type: localStorage.getItem('user-type')
    }
  },
  methods: {

  }
}

</script>


<template>
    <AdminDashboard v-if="user_type === 'admin'" />
    <CustomerDashboard v-if="user_type === 'customer'" />

</template>