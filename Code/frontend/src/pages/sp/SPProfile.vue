<script>


import Navbar from "./components/Navbar.vue";



export default {
  name: "CustomerServiceHistory",
  components: {
    Navbar,
    
    
  },
  data() {
    return {
      sp: this.$store.state.user_details,
      sp_to_update: null,
      message: null,
      loading: true
      
    };
  },

  async created() {
    try {
      await this.fetchSP()
    } catch (e) {
      console.error(e)

    } finally {
      this.loading = false
    }
  },


  methods: {

    async fetchSP() {
        try{
        const res = await fetch('http://localhost:5050' + '/sp', {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.sp_to_update = data
            
            
            
            localStorage.setItem('user-details', JSON.stringify(this.sp_to_update))
            this.$store.commit('setUserDetails')
            
            return data
            
            
        }
    }catch(e){
        console.error(e)
    }
        

    },

    async updateProfile() {
      if(this.sp_to_update.price < this.sp_to_update.service.base_price ){
        this.message = "Price cannot be lower than the base price: " + this.sp_to_update.service.base_price
      }

      else {
      try {
        const res = await fetch(
          "http://localhost:5050" + "/sp",
          {
            method: "PUT",
            headers: {
              "content-type": "application/json",
              "auth-token": this.$store.state.auth_token,
            },
            body: JSON.stringify(this.sp_to_update)
          }
        );
        if (res.ok) {
          const data = await res.json();
          this.message = data
          this.sp = await this.fetchSP()
          

        }
      } catch (e) {
        console.error(e);
      }

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
  <div class="container-fluid">
    <h1> {{ sp.f_name }}'s Profile</h1>


    <div class="form-conatainer">
    <form class="edit-form" @submit.prevent="submitForm">
      <div class="form-content">
        <label class="form-label" :formData.s_id name="s_id" ><strong>Professional Id: </strong>{{ sp.sp_id }}</label
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
              v-model="sp_to_update.f_name"
              disabled
              
            />
          </div>

          <div class="lname-container">
            <label for="price" class="form-label">Last Name</label>
            <input
              type="text"
              class="form-control"
              id="l_name"
              name="l_name"
              v-model="sp_to_update.l_name"
              disabled
            />
          </div>
        </div>
        <br />


        <div class="n-container">
          <div class="service-name-container">
          <label for="service-name" class="form-label">Service Name:</label>
            <input
              type="text"
              class="form-control"
              id="service-name"
              name="service-name"
              v-model="sp_to_update.service.name"
              disabled
            />



            
          </div>

          <div class="price-container">
            <label for="price" class="form-label">Price:</label>
            <input
              type="text"
              class="form-control"
              id="price"
              name="price"
              v-model="sp_to_update.price"
             
            />
          </div>

        </div>

        <br />


        <div class="n-container">
          <div class="experience-container">
          <label for="service-name" class="form-label">Experience:</label>
            <input
              type="text"
              class="form-control"
              id="service-name"
              name="service-name"
              v-model="sp_to_update.experience"
              disabled
            />



            
          </div>

          <div class="rating-container">
            <label for="price" class="form-label">Current rating:</label>
            <input
              type="text"
              class="form-control"
              id="price"
              name="price"
              v-model="sp_to_update.rating"
              disabled
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
              v-model="sp_to_update.address"
              disabled
              
            />
          </div>

          <div class="pincode-container">
            <label for="pincode" class="form-label">Pincode:</label>
            <input
              type="text"
              class="form-control"
              id="pincode"
              name="pincode"
              v-model="sp_to_update.loc_pincode"
              disabled
            />
          </div>
        </div>
        <br />


        
        
        <div class="">
            <div>

          <label for="description" class="form-label"
            >Description: </label
          >

          



          
          <textarea
            class="form-control"
            id="description"
            rows="3"
            name="description"
            v-model="sp_to_update.description"
            
          ></textarea>

        </div>

        
        </div>
      </div>
      <div v-if="message">{{ message }}</div>

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
    border: 2px solid orange;
    max-width: fit-content;
    margin: auto;
    padding: 1rem;
    margin-top: 0rem;
   
}

.form-content {
    justify-content: center;
    max-width: fit-content;
    margin: auto;
    padding: 1rem;
    
}
</style>
















