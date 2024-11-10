<script>
export default {
  name: "Landing",
  data() {
    return {
      form_type: "customer",
    };
  },
  methods: {
    changeToSPForm() {
      this.form_type = "sp";
    },
    changeToCForm() {
      this.form_type = "customer";
    },
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

    <div class="common-login">
      <div class="card text-center common-login-inner">
        <div class="card-header">
          <ul class="nav nav-tabs card-header-tabs n-item">
            <li class="nav-item">
              <a
                v-if="form_type === 'customer'"
                aria-current="true"
                class="nav-link active"
                >For Customers</a
              >
              <a v-else class="nav-link" @click="changeToCForm"
                >For Customers</a
              >
            </li>
            <li class="nav-item">
              <a v-if="form_type === 'sp'" class="nav-link active"
                >For Service Professionals</a
              >
              <a v-else class="nav-link" @click="changeToSPForm"
                >For Service Professionals</a
              >
            </li>
          </ul>
        </div>
        <div class="card-body">
          <div v-if="form_type === 'customer'" class="customer-login">
            <h5 class="card-title">Customer Login</h5>
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">@</span>
              <input
                type="text"
                class="form-control"
                placeholder="Email"
                aria-label="Username"
                aria-describedby="basic-addon1"
              />
            </div>
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">#</span>
              <input
                type="password"
                class="form-control"
                placeholder="Password"
                aria-label="Password"
                aria-describedby="basic-addon1"
              />
            </div>
            <div class="form-check stay-loggedin">
              <input
                class="form-check-input"
                type="checkbox"
                value=""
                id="login-checkbox"
              />
              <label class="form-check-label" for="stayLoggedIn">
                Stay logged in
              </label>
            </div>
            
            <a href="#" class="btn btn-primary">Login</a>
          </div>

          <div v-if="form_type === 'sp'" class="sp-login">
            <h5 class="card-title">SP Login</h5>
            <p class="card-text">Login form for Service Professionals.</p>
            <a href="#" class="btn btn-primary">Login</a>
          </div>
        </div>
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
.common-login-inner {
  width: auto;
  height: fit-content;
  
  border: 5px solid rgba(111, 36, 162, 0.611);
  border-radius: 2rem;
}

.common-login {
    width: auto;
  height: fit-content;
}

.n-item li {
  cursor: pointer;
}

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

.stay-loggedin {
    /* border: 1px solid red; */
    display: flex;
    justify-items: flex-start;
    padding-bottom: 1rem;

}
.stay-loggedin * {
    padding-left:  0.5rem;
}

#login-checkbox {
    margin-left: 0.1rem;
    cursor: pointer;
}
</style>
