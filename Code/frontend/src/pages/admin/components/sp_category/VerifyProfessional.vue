<script>






export default {
  name: "VerifyProfessional",
  components: {


  },

  props: {
    sp: {
        type: Object
    },

    afterAction: {
      type: Function
    }

  },


  data() {
    return {

      sp_obj: null,
      message: null,
      loading: true,
      
    };
  },

  async created() {
    await this.fetchSP()
    try {
      
    } catch (e) {
      console.error(e)

    } finally {
      this.loading = false
    }
  },


  methods: {

    async fetchSP() {
        try{
        const res = await fetch('http://localhost:5050' + '/sps/0' , {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.sp_obj = data.filter((sp) => sp.sp_id === this.sp.sp_id)[0]



        }
    }catch(e){
        console.error(e)
    }
        
        


    },




    async approveSP() {
      this.sp_obj.verified = 'verified'
      this.sp_obj.verification_status = 'Approved'

      try {
        const res = await fetch(
          "http://localhost:5050" + "/sp/"+this.sp.sp_id,
          {
            method: "PUT",
            headers: {
              "content-type": "application/json",
              "auth-token": this.$store.state.auth_token,
            },
            body: JSON.stringify(this.sp_obj)
          }
        );
        if (res.ok) {
          const data = await res.json();
          this.message = data
          this.afterAction()
          

        }
      } catch (e) {
        console.error(e);
      }

    
    },


    async rejectSP() {
      this.sp_obj.verified = 'rejected'
      this.sp_obj.verification_status = 'Rejected'

      try {
        const res = await fetch(
          "http://localhost:5050" + "/sp/"+this.sp.sp_id,
          {
            method: "PUT",
            headers: {
              "content-type": "application/json",
              "auth-token": this.$store.state.auth_token,
            },
            body: JSON.stringify(this.sp_obj)
          }
        );
        if (res.ok) {
          const data = await res.json();
          this.message = data
          this.afterAction()
          

        }
      } catch (e) {
        console.error(e);
      }

    
    },

    async downloadDoc() {
 
      try {
        const res = await fetch(
          "http://localhost:5050" + "/admin/download",
          {
            method: "POST",
            headers: {
              "content-type": "application/json",
              "auth-token": this.$store.state.auth_token,
            },

            body: JSON.stringify(this.sp_obj)
          }
        );
        if (res.ok) {
          const blob = await res.blob()
          const download_url = window.URL.createObjectURL(blob)
          window.open(download_url)

          

        }
      } catch (e) {
        console.error(e);
      }

    
    }





  },
};
</script>

<template>

<div v-if="loading">Loading...</div>

<div v-else>
<div class="form-conatainer">
    <form class="edit-form" @submit.prevent="submitForm">
      <div class="form-content">
        <label class="form-label" :formData.s_id name="s_id" ><strong>Professional Id: </strong>{{ sp_obj.sp_id }}</label
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
              v-model="sp_obj.f_name"
             
              
            />
          </div>

          <div class="lname-container">
            <label for="price" class="form-label">Last Name</label>
            <input
              type="text"
              class="form-control"
              id="l_name"
              name="l_name"
              v-model="sp_obj.l_name"
          
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
              v-model="sp_obj.service.name"
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
              v-model="sp_obj.price"
             
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
              v-model="sp_obj.experience"
           
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
              v-model="sp_obj.address"
              
              
            />
          </div>

          <div class="pincode-container">
            <label for="pincode" class="form-label">Pincode:</label>
            <input
              type="text"
              class="form-control"
              id="pincode"
              name="pincode"
              v-model="sp_obj.loc_pincode"
              
            />
          </div>
        </div>
        <br />


        
        
        <div v-if="sp_obj.submitted_doc_path" class="doc-container">
            <div>
              <button class="btn btn-outline-primary" @click="downloadDoc">Download Submitted Document</button>


          

        </div>

        
        </div>
      </div>
      <div v-if="message">{{ message }}</div>
      <div class="button-container">
      <button type="submit" class="btn btn-outline-success" @click="approveSP">Approve</button>
      <button type="submit" class="btn btn-outline-danger" @click="rejectSP">Reject</button>
    </div>
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
    
    max-width: 40rem;
    margin: auto;
    
    margin-top: 0rem;
   
}

.form-content {
    justify-content: center;
    max-width: fit-content;
    margin: auto;
    padding: 1rem;
    
}
.button-container {
  display: flex;
  width: 100%;
  justify-content: center;
}

.button-container * {
  margin: 0.7rem;
}
</style>
















