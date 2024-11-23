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
    spLogout() {
        this.$store.commit('logout')
        localStorage.removeItem('user-type')
        this.$router.push('/')
    },
    navigateServiceHistory() {
      this.$router.push('/sp/service_history')
    }
  }
};
</script>

<template>
  <div class="nav-container">
    <div class="user-label">
        <ul class="navbar-nav">
        <li class="nav-item dropdown-center d-container">
          <button class="btn btn-dark dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
            {{ email }} 
          </button>
          <ul class="dropdown-menu dropdown-menu-dark d-menu">
            <li><a class="dropdown-item" href="#">View Profile</a></li>
            <li><a class="dropdown-item" @click="navigateServiceHistory">Service History</a></li>
            <li><a class="dropdown-item" href="#">Summary</a></li>
            <li><a class="dropdown-item" @click="spLogout">Logout</a></li>
          </ul>
        </li>
      </ul>

      
    </div>
  </div>

  
</template>

<style scoped>
.nav-container {
  display: flex;
  background-color: black;
  color: white;
  width: 100%;
  height: 5rem;
  justify-content: space-between;
}
.login-type {
  background-color: red;
  padding: 0.3rem;
  border: 1px solid red;
  border-radius: 0.5rem;
}

.user-label {
  align-self: center;
  margin-left: auto;
}
.d-container {
    display: flex;
    justify-content: flex-end;
    margin-left: auto;
}

.d-menu {
    width: max-content;
    margin-left: auto;

}

.d-menu li {
    cursor: pointer;
}
</style>
