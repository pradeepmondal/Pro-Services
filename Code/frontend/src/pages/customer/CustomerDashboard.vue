<script>
import AddAddressForm from "./components/AddAddressForm.vue";
import CustomerNotification from "./components/CustomerNotification.vue";
import CustomerSearch from "./components/CustomerSearch.vue";
import Navbar from "./components/Navbar.vue";
import ServiceCategories from "./components/services/ServiceCategories.vue";

export default {
  name: "CustomerDashboard",
  components: {
    Navbar,
    CustomerSearch,
    CustomerNotification,
    ServiceCategories,
    AddAddressForm,
  },
  data() {
    return {
      customer: null,
      loading: true,
      show_add_address: false,
      show_notification: true,
      block_status: 'unblocked',
    };
  },
  async created() {
    try {
      await this.fetchCustomer();
    } catch (e) {
      console.error(e);
    } finally {
      this.loading = false;
    }
  },

  methods: {
    async fetchCustomer() {
      try {
        const res = await fetch("http://localhost:5050" + "/customer", {
          method: "GET",
          headers: {
            "content-type": "application/json",
            "auth-token": this.$store.state.auth_token,
          },
        });
        if (res.ok) {
          const data = await res.json();
          this.customer = data;
          

          localStorage.setItem("user-details", JSON.stringify(this.customer));
          this.$store.commit("setUserDetails");
          console.log("User details stored");
          this.show_add_address = false;
        } else if (res.status === 401) {
          this.block_status = 'blocked';
          
        }
      } catch (e) {
        console.error(e);
      }
    },
    addAddress() {
      this.show_notification = false;
      this.show_add_address = true;
    },
  },
};
</script>

<template>
  <div v-if="block_status === 'blocked'">You have been blocked</div>

  <div v-if="loading">Loading...</div>
  
  <div v-else>
    <Navbar />
    <div class="container-fluid">
      <CustomerNotification
        v-if="show_notification"
        :customer="customer"
        :addAddress="addAddress"
      />
      <AddAddressForm v-if="show_add_address" :afterAction="fetchCustomer" />

      <h1>Welcome {{ customer.f_name }} !!</h1>
      <CustomerSearch />
      <ServiceCategories />
    </div>
  </div>
</template>
