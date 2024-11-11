<script>
export default {
  name: "Login",
  data() {
    return {
      email: null,
      password: null,
    };
  },
  methods: {
    async adminLogin() {
        try {
      const res = await fetch('http://localhost:5050' + '/login', {method: 'POST', headers: {"content-type" : "application/json"}, body: JSON.stringify({email: this.email, password: this.password})})
      if(res.ok){
        const data = await res.json();
        // console.log('success', data.roles[0].rid)
        const roles = data.roles.map((role) => role.name)
        if (roles.includes('admin')){
            localStorage.setItem('auth-token', data.token)
            localStorage.setItem('user-type', 'admin')
            this.$router.push('/dashboard')

        }
        
        
      }
    } catch(e) {
        console.error(e);
        
    }


    }
  },
};
</script>


<template>
    
      <div class="card text-center common-login-inner">
        
        <div class="card-body">
          
            <h5 class="card-title">Admin Login</h5>
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">@</span>
              <input
                type="text"
                class="form-control"
                placeholder="Email"
                aria-label="Username"
                aria-describedby="basic-addon1"
                v-model="email"
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
                v-model="password"
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
            
            <a href="#" class="btn btn-primary" @click="adminLogin">Login</a>
          
        </div>
      </div>
    
</template>





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