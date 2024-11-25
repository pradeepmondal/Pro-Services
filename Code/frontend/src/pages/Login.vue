<script>
export default {
  name: "Login",
  props: {
    setActiveSuccessMessage: {
        type: Function
    }
  },
  data() {
    return {
      form_type: "customer",
      email: null,
      password: null,
      
      b_error_message: null,
      
    };
  },
  computed: {
    f_error_message() {
      this.b_error_message = null
      if (!this.email){
        return 'Email is missing'
      } 
      if (!this.password){
        return 'Password is missing'

      } 
      if (this.password & this.email) {
        return null
      }

    },

    error_message() {
      let error = this.f_error_message || this.b_error_message
      return error
    }

  },

  methods: {

    async Login() {

      
      if(!this.f_error_message) {
        try {
      const res = await fetch('http://localhost:5050' + '/login', {method: 'POST', headers: {"content-type" : "application/json"}, body: JSON.stringify({email: this.email, password: this.password})})
      if(res.ok){
        const data = await res.json();
        // console.log('success', data.roles[0].rid)
        const roles = data.roles.map((role) => role.name)
        if (roles.includes('customer')){
            localStorage.setItem('user', JSON.stringify(data))
            localStorage.setItem('user-type', 'customer')
            this.$store.commit('setUser')
            this.$router.push('/dashboard')

        }

        else if (roles.includes('service_professional')){
            localStorage.setItem('user', JSON.stringify(data))
            localStorage.setItem('user-type', 'sp')
            this.$store.commit('setUser')
            this.$router.push('/dashboard')

        }

        else if (roles.includes('admin')){
            localStorage.setItem('user', JSON.stringify(data))
            localStorage.setItem('user-type', 'admin')
            this.$store.commit('setUser')
            this.$router.push('/dashboard')

        }
        
        
      }

      if(!res.ok){
          const data = await res.json()
          throw new Error(data.message || 'Error occurred')
        }
    } catch(e) {
        console.error(e.message);
        this.b_error_message = e.message

    }

        
    }


    },
    
  },
};
</script>


<template>
    <div class="common-login">
      <div class="card text-center common-login-inner">
        
        <div class="card-body">
          
          <div  class="login">
            <h5 class="card-title">Login</h5>
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
            <div :class="[error_message ? 'active-error': '']">{{ error_message }}</div>
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
            
            <a href="#" class="btn btn-primary" @click="Login">Login</a>
          </div>

          
        </div>
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

.active-error {
  background-color: red;
  color: white;
  height: fit-content;
}

</style>