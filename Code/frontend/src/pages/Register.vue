<script>
export default {
  name: "Register",
  props: {
    setActiveSuccessMessage: {
        type: Function
    }
  },
  data() {
    return {
      form_type: "customer",
      loading: true,
      available_services: null,

      customerData: {
        accepted : false,
        email : null,
        password : null,
        confirm_password : null,
        f_name : null,
        l_name : null,

      },

      spData: {
        accepted: false,
        email: null,
        password: null,
        confirm_password: null,
        f_name: null,
        l_name: null,
        service_type: null,
        price: null,
        experience: null,
        submitted_doc: null,
        profile_image: null,
        address: null,
        loc_pincode: null

      },
      
      b_error_message: null,
      
    };
  },
  computed: {
    f_error_message() {
      this.b_error_message = null
      if (!this.customerData.f_name){
        return 'First name is missing'

      } 
      if (!this.customerData.email){
        return 'Email is missing'
      } 
      if (!this.customerData.password){
        return 'Password is missing'

      } 

      if (!this.customerData.confirm_password){
        return 'Confirm the password'

      } 

      if (this.customerData.password !== this.customerData.confirm_password){
        return "Passwords do not match"

      } 

      if (!this.customerData.accepted){
        return 'Accept T&C'

      } 
      
      if (this.password & this.email) {
        return null
      }

    },



    f_sp_error_message() {
      this.b_error_message = null
      if (!this.spData.f_name){
        return 'First name is missing'

      } 
      if (!this.spData.email){
        return 'Email is missing'
      } 
      if (!this.spData.password){
        return 'Password is missing'

      } 

      if (!this.spData.confirm_password){
        return 'Confirm the password'

      } 

      if (this.spData.password !== this.spData.confirm_password){
        return "Passwords do not match"

      } 

      if (!this.spData.service_type){
        return 'Select a service'

      } 

      if (!this.spData.experience){
        return 'Experience is missing'

      } 

      if (!this.spData.price){
        return 'Fill in price'

      } 

      if ((this.spData.price < this.selected_service_base_price)){
        return 'Price should be at least the service base price'

      } 

      if (!this.spData.address){
        return 'Address is missing'

      } 

      if (!this.spData.loc_pincode){
        return 'Pincode is missing'

      } 

      if (!this.spData.submitted_doc){
        return 'Document is missing'

      } 

      if (!this.spData.profile_image){
        return 'Profile image is missing'

      } 

      if (!this.spData.accepted){
        return 'Accept T&C'

      } 
      
      if (this.password & this.email) {
        return null
      }

    },

    error_message() {
      let error = this.f_error_message || this.b_error_message 
      return error
    },

    sp_error_message() {
      let error = this.f_sp_error_message || this.b_error_message 
      return error

    },

    selected_service_base_price() {
      if(!this.spData.service_type){
        return 0
      }
      else {
        return this.available_services.filter((s) => s.s_id === this.spData.service_type)[0].base_price
      }
    }

    


  },

  async created() {
    try {
      await this.fetchServices()
    } catch (e) {
      console.error(e)

    } finally {
      this.loading = false
    }
  },



  methods: {
    async fetchServices() {
        try{
        const res = await fetch('http://localhost:5050' + '/unauth_services' , {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.available_services = data



        }
    }catch(e){
        console.error(e)
    }
        
        


    },


    changeToSPForm() {
      this.form_type = "sp";
      
      this.f_error_message = null;
      this.b_error_message = null;
      
    },
    changeToCForm() {
      this.form_type = "customer";

      this.f_error_message = null;
      this.b_error_message = null;
    },
    async custRegister() {
        




      
      if(!this.f_error_message) {
        try {
      const res = await fetch('http://localhost:5050' + '/customer', {method: 'POST', headers: {"content-type" : "application/json"}, body: JSON.stringify(this.customerData)})
      if(res.ok){
        const data = await res.json();
        this.customerData.accepted = false
        this.customerData.email = null
        this.customerData.password = null
        this.customerData.confirm_password = null
        this.customerData.f_name = null
        this.customerData.l_name = null
        this.error_message = null
        this.setActiveSuccessMessage(data)

        
        
        
        
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
    async spRegister() {
      
      if(!this.f_sp_error_message) {
        try {
          const formData = new FormData()
          formData.append('email', this.spData.email)
          formData.append('password', this.spData.password)
          formData.append('confirm_password', this.spData.confirm_password)
          formData.append('f_name', this.spData.f_name)
          formData.append('l_name', this.spData.l_name)
          formData.append('price', this.spData.price)
          formData.append('service_type', this.spData.service_type)
          formData.append('experience', this.spData.experience)
          formData.append('submitted_doc', this.spData.submitted_doc)
          formData.append('profile_image', this.spData.profile_image)
          formData.append('address', this.spData.address)
          formData.append('loc_pincode', this.spData.loc_pincode)

          const res = await fetch('http://localhost:5050' + '/sp', {method: 'POST', body: formData})
      if(res.ok){
        const data = await res.json();
        this.spData.accepted = false
        this.spData.email = null
        this.spData.password = null
        this.spData.confirm_password = null
        this.spData.f_name = null
        this.spData.l_name = null
        this.spData.service_type = null
        this.spData.experience = null
        this.spData.submitted_doc = null
        this.spData.profile_image = null
        this.spData.address = null
        this.spData.loc_pincode = null
        this.error_message = null
        this.setActiveSuccessMessage(data)
        
        
        
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


    
    handleDocumentUpload(event) {
      this.spData.submitted_doc = event.target.files[0]
    },

    handleImageUpload(event) {
      this.spData.profile_image = event.target.files[0]
    },
    
  },
};
</script>


<template>
  <div v-if="loading">Loading...</div>
    <div v-else class="common-register">
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
          
          <div v-if="form_type === 'customer'" class="customer-register">
            <h5 class="card-title">Customer Registration</h5>
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">*</span>
              <input
                type="text"
                class="form-control"
                placeholder="First Name"
                aria-label="f_name"
                aria-describedby="basic-addon1"
                v-model="customerData.f_name"
              />
              <input
                type="text"
                class="form-control"
                placeholder="Last Name"
                aria-label="l_name"
                aria-describedby="basic-addon1"
                v-model="customerData.l_name"
              />
            </div>


            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">@</span>
              <input
                type="email"
                class="form-control"
                placeholder="Email"
                aria-label="email"
                aria-describedby="basic-addon1"
                v-model="customerData.email"
              />
            </div>
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">#</span>
              <input
                type="password"
                class="form-control"
                placeholder="Password"
                aria-label="password"
                aria-describedby="basic-addon1"
                v-model="customerData.password"
              />
              <input
                type="password"
                class="form-control"
                placeholder="Confirm Password"
                aria-label="confirm_password"
                aria-describedby="basic-addon1"
                v-model="customerData.confirm_password"
              />
            </div>
            <div :class="[error_message ? 'active-error': '']">{{ error_message }}</div>
            <div :class="[success_message ? 'active-success-message': '']">{{ success_message }}</div>
            <div class="form-check tc ">
              <input
                class="form-check-input"
                type="checkbox"
                value="accepted"
                id="t&c-checkbox"
                v-model="customerData.accepted"
              />
              <label class="form-check-label" for="t&c">
                Accept T&C
              </label>
            </div>
            
            <a href="#" class="btn btn-primary" @click="custRegister">Register</a>
          </div>

          <div v-if="form_type === 'sp'" class="sp-registration">
            
            <h5 class="card-title">SP Registration</h5>
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">*</span>
              <input
                type="text"
                class="form-control"
                placeholder="First Name"
                aria-label="f_name"
                aria-describedby="basic-addon1"
                v-model="spData.f_name"
              />
              <input
                type="text"
                class="form-control"
                placeholder="Last Name"
                aria-label="l_name"
                aria-describedby="basic-addon1"
                v-model="spData.l_name"
              />
            </div>


            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">@</span>
              <input
                type="email"
                class="form-control"
                placeholder="Email"
                aria-label="email"
                aria-describedby="basic-addon1"
                v-model="spData.email"
              />
            </div>
            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">#</span>
              <input
                type="password"
                class="form-control"
                placeholder="Password"
                aria-label="password"
                aria-describedby="basic-addon1"
                v-model="spData.password"
              />
              <input
                type="password"
                class="form-control"
                placeholder="Confirm Password"
                aria-label="confirm_password"
                aria-describedby="basic-addon1"
                v-model="spData.confirm_password"
              />
            </div>
            <div class="input-group mb-3 service-selector">
              <div class="selector">
            <label for="service" class="form-label">Select Service: &nbsp; </label>
            <select class="form-select" aria-label="Default select example" name="s_id" v-model="spData.service_type" >
              <template v-for="service in available_services">
                <option :value="service.s_id">{{ service.name }}</option>
              </template>
            </select>
          </div>

            <div v-for="service in available_services" class="service-base-price">
              <label v-if="service.s_id === spData.service_type" >Base Price: ₹{{ service.base_price }} </label>
            </div>
          </div>

          <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">E</span>
              <input
                type="text"
                class="form-control"
                placeholder="Experience"
                aria-label="experience"
                aria-describedby="basic-addon1"
                v-model="spData.experience"
              />


              <span class="input-group-text" id="basic-addon1">₹</span>
              <input
                type="text"
                class="form-control"
                placeholder="Price"
                aria-label="price"
                aria-describedby="basic-addon1"
                v-model="spData.price"
              />
             
            </div>

            <div class="input-group mb-3">
              <span class="input-group-text" id="basic-addon1">A</span>
              <input
                type="text"
                class="form-control"
                placeholder="Address"
                aria-label="experience"
                aria-describedby="basic-addon1"
                v-model="spData.address"
              />

              <span class="input-group-text" id="basic-addon1">P</span>
              <input
                type="text"
                class="form-control"
                placeholder="Pincode"
                aria-label="pincode"
                aria-describedby="basic-addon1"
                v-model="spData.loc_pincode"
              />
             
            </div>

            <div class="input-group  p-2 service-selector">
              <label for="doc" class="form-label">Attach Document: &nbsp; </label>
              <input
                type="file"
                class="form-control"
                placeholder="Experience"
                aria-label="experience"
                aria-describedby="basic-addon1"
                @change="handleDocumentUpload"
              />
             
            </div>

            <div class="input-group p-2 service-selector">
              <label for="doc" class="form-label">Profile Image: &nbsp; </label>
              <input
                type="file"
                class="form-control"
                placeholder="Experience"
                aria-label="experience"
                aria-describedby="basic-addon1"
                @change="handleImageUpload"
              />
             
            </div>





            <div :class="[error_message ? 'active-error': '']">{{ sp_error_message }}</div>
            <div class="form-check tc ">
              <input
                class="form-check-input"
                type="checkbox"
                value="accepted"
                id="t&c-checkbox"
                v-model="spData.accepted"
              />
              <label class="form-check-label" for="t&c">
                Accept T&C
              </label>
            </div>
            
            <a href="#" class="btn btn-primary" @click="spRegister">Register</a>
          
          
          </div>
        </div>
      </div>
    </div>
</template>





<style scoped>
.common-register-inner {
  width: auto;
  height: fit-content;
  
  border: 5px solid rgba(111, 36, 162, 0.611);
  border-radius: 2rem;
}

.common-register {
    width: auto;
  height: fit-content;
}

.n-item li {
  cursor: pointer;
}

.tc {
    /* border: 1px solid red; */
    display: flex;
    justify-items: flex-start;
    padding-bottom: 1rem;

}
.tc * {
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
  margin: 0.6rem 0;
}

.service-selector {
  display: flex;
  align-items: center;
  justify-content: space-around;
  
  
  
}

.service-selector .selector {
  display: flex;
  align-items: center;
  
  
  
  
}

.service-selector label {
  font-size: 1.1rem;
  
}

.service-selector select{
  
  max-width: fit-content;
  max-height: fit-content;
  
  
  
}

.base-price {
  max-width: 7rem;
}

</style>