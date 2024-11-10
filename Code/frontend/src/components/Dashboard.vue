<script>
import CustomerDashboard from './CustomerDashboard.vue'

export default {
  components : {
    CustomerDashboard
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
    <CustomerDashboard v-if="user_type === 'customer'" />

</template>