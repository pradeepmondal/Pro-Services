<script>
export default {
  name: "Navbar",
  props: {
    
  },

  data() {
    return {
      email: this.$store.state.email

    }
    
  },

  methods: {
    customerLogout() {
        this.$store.commit('logout')
        localStorage.removeItem('user-type')
        this.$router.push('/')
    },
    navigateServiceHistory() {
      this.$router.push('/customer/service_history')
    },
    navigateProfile() {
      this.$router.push('/customer/profile')
    },

    navigateSummary() {
      this.$router.push('/customer/summary')
    },

    navigateHome() {
      this.$router.push('/dashboard')
    }

  }
};
</script>

<template>
   <div class="nav-container">
   
   <ul class="menu-container">
     <li class="home-button"><button class="btn"><i class="bi bi-house-door-fill" @click="navigateHome"> Home</i></button></li>
   <li class="nav-item dropdown-center ">
          <button class="btn btn-dark dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
            {{ email }} 
          </button>
          <ul class="dropdown-menu dropdown-menu-dark d-menu">
            <li><a class="dropdown-item" @click="navigateProfile">View Profile</a></li>
            <li><a class="dropdown-item" @click="navigateServiceHistory">Service History</a></li>
            <li><a class="dropdown-item" @click="navigateSummary">Summary</a></li>
            <li><a class="dropdown-item" @click="customerLogout">Logout</a></li>
          </ul>
        </li>
      </ul>

      
   
  </div>

  
</template>

<style scoped>
.nav-container {
  display: flex;
  background-color: black;
  color: white;
  width: 100%;
  height: 4rem;
  justify-content: space-between;
  align-items:center;
}
.login-type {
  background-color: red;
  padding: 0.3rem;
  border: 1px solid red;
  border-radius: 0.5rem;
}


.d-container {
    display: flex;
    
    margin-left: auto;
}

.d-menu {
    width: max-content;
    margin-left: auto;

}

.d-menu li {
    cursor: pointer;
}

.menu-container {
  display: flex;
  justify-content: space-between;
  width: 100%;
  
}

.nav-container ul {
  list-style-type: none;
}

.home-button button {
  color: white;
}
</style>
