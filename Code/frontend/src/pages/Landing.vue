<script>
import Login from "./Login.vue";
import AdminLogin from "./admin/AdminLogin.vue";
import Register from "./Register.vue";


export default {
  components: {
    Login,
    AdminLogin,
    Register
  },
  name: "Landing",
  data() {
    return {
      show_login_form: false,
      show_admin_login_form: false,
      show_register_form: false,
      active_success_message: false
    };
  },
  methods: {
    showLoginForm() {
      this.show_admin_login_form = false;
      this.show_login_form = true;
      this.show_register_form = false;
      this.active_success_message = false;
    },
    showAdminLoginForm() {
      this.show_login_form = false;
      this.show_admin_login_form = true;
      this.show_register_form = false;
      this.active_success_message = false;
    },
    showRegisterForm() {
      this.show_admin_login_form = false;
      this.show_login_form = false;
      this.show_register_form = true;
      this.active_success_message = false;
    },
    setActiveSuccessMessage(message) {
      this.active_success_message = message
      this.show_admin_login_form = false;
      this.show_login_form = false;
      this.show_register_form = false;
    }
  },
};
</script>

<template>
  <div class="custom-container">
    <h1 id="heading"></h1>
    <div class="hovering-img-container">
      <img class="graphics-1" src="../assets/graphic-1.png" />
      <img class="graphics-2" src="../assets/graphic-2.png" />
    </div>
    <div class="login-container">
      <div class="login-container">
        <Login v-if="show_login_form" :setActiveSuccessMessage="setActiveSuccessMessage" />
        <AdminLogin v-if="show_admin_login_form" :setActiveSuccessMessage="setActiveSuccessMessage" />
        <Register v-if="show_register_form" :setActiveSuccessMessage="setActiveSuccessMessage" />
        <div class=" card card-body" v-if="active_success_message"> 
          <div class="active_success_message"> {{ active_success_message }}  </div>
        </div>
      </div>
      <div class="login-button-container">
        <a
          v-if="!(show_login_form) & !(show_admin_login_form) & !(show_register_form)"
          
          class="btn btn-primary"
          @click="showLoginForm"
          >Let's Login</a
        >
        

        <a
          v-if="!(show_login_form) & (show_admin_login_form)"
          class="btn btn-primary"
          @click="showLoginForm"
          >Customer/SP Login</a
        >

        <a
          v-if="!(show_login_form) & (show_register_form)"
          class="btn btn-primary"
          @click="showLoginForm"
          >Go to Login</a
        >

        <a
          v-if="!(show_admin_login_form) & show_login_form"
          class="btn btn-primary"
          @click="showAdminLoginForm"
          >Admin Login</a
        >

        <a
          v-if="!(show_login_form) & !(show_admin_login_form) & !(show_register_form) "
          class="btn btn-primary"
          @click="showRegisterForm"
          >New? Register Here !</a
        >

        <a
          v-if="(show_login_form) & !(show_register_form) "
          class="btn btn-primary"
          @click="showRegisterForm"
          >New? Register Here !</a
        >

        <a
          v-if="(show_admin_login_form) & !(show_register_form) "
          class="btn btn-primary"
          @click="showRegisterForm"
          >New? Register Here !</a
        >
      </div>
    </div>
  </div>

  <!-- <ul>
        <li><router-link to='/login'>Login</router-link></li>
        <li><router-link to='/signup'>Sign Up</router-link></li>
    </ul> -->
</template>

<style>
body {
  background-color: black;
}
</style>

<style scoped>
.custom-container {
  display: flex;
  justify-content: space-between;
  padding: 5rem;
  border: 2px solid green;
  height: 100vh;
  background-color: hsl(268, 48%, 71%);
}

.hovering-img-container {
  padding: 2rem 1rem;
  display: flex;
  flex-direction: column;
  border: 2px solid hsl(279, 72%, 39%);
  width: fit-content;
  height: fit-content;
  background-color: hsl(279, 43%, 55%);
  border-radius: 2rem;
}

.graphics-1 {
  background-color: rgb(215, 237, 245);
}
.graphics-2 {
  background-color: rgb(255, 179, 0);
}

.hovering-img-container img {
  width: 22rem;
  padding: 2rem;
}

.login-button-container {
  
  display: flex;
  flex-direction: column;
  padding: 1em ;
}

.login-button-container a {
  padding: 0.5rem 1rem;
  margin: 0.5em 1rem;

}

.active-success-message {
  background-color: green;
}
</style>
