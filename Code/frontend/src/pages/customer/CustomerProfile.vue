<script>

import CustomerSearch from "./components/CustomerSearch.vue";
import Navbar from "./components/Navbar.vue";

import SRActionModal from "./components/SRActionModal.vue";

export default {
  name: "CustomerServiceHistory",
  components: {
    Navbar,
    CustomerSearch,
    SRActionModal,
  },
  data() {
    return {
      customer: this.$store.state.user_details,
      customer_to_update: null,
      message: null,
      loading: true
      
    };
  },

  async created() {
    try {
      await this.fetchCustomer()
    } catch (e) {
      console.error(e)

    } finally {
      this.loading = false
    }
  },


  methods: {

    async fetchCustomer() {
        try{
        const res = await fetch('http://localhost:5050' + '/customer', {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.customer_to_update = data
            
            
            
            localStorage.setItem('user-details', JSON.stringify(this.customer_to_update))
            this.$store.commit('setUserDetails')
            
            return data
            
            
        }
    }catch(e){
        console.error(e)
    }
        

    },

    async updateProfile() {
      try {
        const res = await fetch(
          "http://localhost:5050" + "/customer",
          {
            method: "PUT",
            headers: {
              "content-type": "application/json",
              "auth-token": this.$store.state.auth_token,
            },
            body: JSON.stringify(this.customer_to_update)
          }
        );
        if (res.ok) {
          const data = await res.json();
          this.message = data
          this.customer = await this.fetchCustomer()
          

        }
      } catch (e) {
        console.error(e);
      }
    }

  },
};
</script>

<template>
  <Navbar />

  <SRActionModal
    :modal_type="modal_type"
    :modal_heading="modal_heading"
    :action="action"
    :selected_sr="selected_sr"
  />
  <div class="parent-container">
    <h1 class="heading"> {{ customer.f_name }}'s Profile</h1>


    <div class="form-conatainer">
    <form class="edit-form" @submit.prevent="submitForm">
      <div class="form-content">
        <label class="form-label" :formData.s_id name="s_id" ><strong>Customer Id: </strong>{{ customer.c_id }}</label
        ><br />
        <br />

        <div class="n-container">
          <div class="fname-container">
            <label for="name" class="form-label">First Name</label>
            <input
              type="text"
              class="form-control"
              id="f_name"
              name="f_name"
              v-model="customer_to_update.f_name"
              
              
            />
          </div>

          <div class="lname-container">
            <label for="price" class="form-label">Last Name</label>
            <input
              type="text"
              class="form-control"
              id="l_name"
              name="l_name"
              v-model="customer_to_update.l_name"
              
            />
          </div>
        </div>
        <br />


        <div class="n-container">
          <div class="address-container">
            <label for="name" class="form-label">Address: </label>
            <input
              type="text"
              class="form-control"
              id="address"
              name="address"
              v-model="customer_to_update.address"
              
              
            />
          </div>

          <div class="pincode-container">
            <label for="price" class="form-label">Pincode:</label>
            <input
              type="text"
              class="form-control"
              id="pincode"
              name="pincode"
              v-model="customer_to_update.loc_pincode"
              
            />
          </div>
        </div>
        <br />

        
        <div class="n-container">
            <div>

          <label for="description" class="form-label"
            >Description: </label
          >

          



          
          <textarea
            class="form-control"
            id="description"
            rows="3"
            name="description"
            v-model="customer_to_update.description"
            
          ></textarea>

        </div>
        </div>
      </div>
      <div v-if="message" class="message-container">{{ message }}</div>

      <button type="submit" class="btn btn-success" @click="updateProfile">Update</button>
    </form>
  </div>
   

    
  </div>
</template>

<style scoped>
.n-container {
  display: flex;
}

.time-cat {
  display: flex;
}

.n-container div {
  margin: 0 0.5rem;
}

.time-cat div {
  margin: 0 0.5rem;
}

.edit-form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    border: 2px solid rgb(31, 161, 66);
    border-radius: 1rem;
    max-width: fit-content;
    margin: auto;
    padding: 2rem;
    margin-top: 4rem;
    background-color: rgb(241, 255, 245);
   
}

.form-content {
    justify-content: center;
    max-width: fit-content;
    margin: auto;
    padding: 1rem;
    
}

.parent-container {
  
  
  height: 92vh;
  width:100%;
  
  background-color: antiquewhite;

}

.heading {
  padding: 1rem;
  padding-top: 0.5rem;
  padding-bottom: 0rem;
}


  






</style>
















