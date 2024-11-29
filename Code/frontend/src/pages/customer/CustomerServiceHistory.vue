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
      // loading: true,
      srs: null,
      modal_type: null,
      modal_heading: null,
      action: null,
      show_modal: false,
      selected_sr: null,

      search_mode: false,
      search_query: null,
      search_param: null,
      
      
    };
  },
  async created() {
    try {
      await this.fetchSR();
    } catch (e) {
      console.error(e);
    } finally {
      this.loading = false;
    }
  },

  computed: {
    final_srs(){
      if(!this.search_mode){
        return this.srs
      }
      else{
        let search_query = this.search_query.toLowerCase()
        let search_param = this.search_param
        let regex = new RegExp(search_query, 'i')
        return this.srs.filter((sr) => {
            if(search_param === 'status'){
              return regex.test(sr.status )
            }
            else if(search_param === 'professional_name'){
              return regex.test(sr.professional_name)
            }
            else if(search_param === 'service_name'){
              return regex.test(sr.service_name)
            }
            
             
         
        })

      }
    }

  },

  methods: {
    async fetchSR() {
      try {
        const res = await fetch(
          "http://localhost:5050" +
            "/service_request/" +
            this.customer.c_id +
            "/0",
          {
            method: "GET",
            headers: {
              "content-type": "application/json",
              "auth-token": this.$store.state.auth_token,
            },
          }
        );
        if (res.ok) {
          const data = await res.json();
          this.srs = data;
          this.srs.forEach(sr => {
            sr.updated = false;
            sr.request_date = this.handleDate(sr.request_date)
            
          })
        
        
        }
      } catch (e) {
        console.error(e);
      }
    },

    async markComplete(sr, rating) {

        sr.status = "Completed";
        sr.rating = rating;


      {
        try {
          const res = await fetch(
            "http://localhost:5050" + "/service_request/" + sr.sr_id,
            {
              method: "PUT",
              headers: {
                "content-type": "application/json",
                "auth-token": this.$store.state.auth_token,
              },

              body: JSON.stringify(sr),
            }
          );
          if (res.ok) {
            const data = await res.json();
          }
        } catch (e) {
          console.error(e);
        }
      }



    },





    async cancelSR(sr) {
      sr.status = "Cancelled";

      {
        try {
          const res = await fetch(
            "http://localhost:5050" + "/service_request/" + sr.sr_id,
            {
              method: "PUT",
              headers: {
                "content-type": "application/json",
                "auth-token": this.$store.state.auth_token,
              },

              body: JSON.stringify(sr),
            }
          );
          if (res.ok) {
            const data = await res.json();
          }
        } catch (e) {
          console.error(e);
        }
      }
    },

    updateSearchQuery(search_input, search_param){
      this.search_mode = true
      this.search_query = search_input
      this.search_param = search_param
    },

    clearSearch(){
      this.search_mode = false
    },


    openCancelModal(sr) {
      this.modal_type = "cancel_sr";
      this.modal_heading = "Cancel " + sr.service_name;
      this.action = this.cancelSR;
      this.show_modal = true;
      this.selected_sr = sr;
    },

    openMarkCompleteModal(sr) {
      this.modal_type = "mark_complete_sr";
      this.modal_heading = "Mark Complete " + sr.service_name;
      this.action = this.markComplete;
      this.show_modal = true;
      this.selected_sr = sr;
    },

    handleDate(dateString){
      let date = new Date(dateString)
      return date.toISOString().split('T')[0]
    
    },

    handleDateChange(sr) {
      sr.updated = true
      


    },

    async updateDate(sr) {
      sr.date = sr.request_date
      sr.status = 'Requested'
      sr.remarks = 'Date changed'
      

      {
        try {
          const res = await fetch(
            "http://localhost:5050" + "/service_request/" + sr.sr_id,
            {
              method: "PUT",
              headers: {
                "content-type": "application/json",
                "auth-token": this.$store.state.auth_token,
              },

              body: JSON.stringify(sr),
            }
          );
          if (res.ok) {
            const data = await res.json();
            this.fetchSR()
          }
        } catch (e) {
          console.error(e);
        }
      }
    },

    
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
    <h1>Welcome {{ customer.f_name }} !!</h1>
    <CustomerSearch search_placeholder="Search in Service Requests" :updateSearchQuery="updateSearchQuery" :clearSearch="clearSearch" :search_mode="search_mode" search_param_req="true" search_in="customer_srs" />

    <div class="container sr-table">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Service Name</th>
            <th scope="col">Professional</th>
            <th scope="col">Price</th>
            <th scope="col">Status</th>
            <th scope="col">Request Date</th>
            <th scope="col">Action</th>
            <th scope="col">Remarks</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(sr, index) in final_srs">
            <td scope="row">
              <div>
                {{ sr.sr_id }}
              </div>
            </td>
            <td>
              <div class="service_name">{{ sr.service_name }}</div>
            </td>
            <td>{{ sr.professional_name }}</td>
            <td>₹{{ sr.professional_price }}</td>
            <td > <div v-if="sr.status === 'Requested'" class="status requested">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'In Progress'" class="status progress">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'Completed'" class="status completed">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'Rejected'" class="status rejected-cancelled">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'Cancelled'" class="status rejected-cancelled">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'Closed'" class="status closed">{{ sr.status }}</div>
            </td>
           
            <td>
              <input v-if="sr.status === 'Completed' || sr.status === 'Closed'" type="date"  v-model="sr.request_date" @change="handleDateChange(sr)" disabled />
              <input v-else type="date"  v-model="sr.request_date" @change="handleDateChange(sr)" />
            
            </td>

            <td>
              <div class="button-container">
                <button
                  v-if="sr.status === 'In Progress'"
                  class="btn btn-outline-success"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="openMarkCompleteModal(sr)"
                >
                  Mark Completed
                </button>

                <button
                  v-if="sr.status !== 'Closed' && sr.status !== 'Completed' && sr.status !== 'Cancelled'"
                  class="btn btn-outline-danger"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="openCancelModal(sr)"
                >
                  Cancel
                </button>

                <button
                  v-if="sr.updated"
                  class="btn btn-outline-primary"
                 
                  @click="updateDate(sr)"
                >
                  Update Date
                </button>
              </div>
            </td>

            <td>{{ sr.remarks }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
.sr-table {
  margin-top: 2rem;
}

.button-container {
    max-width: fit-content;

}

.button-container button {
    margin: 0 0.4rem;
    width: fit-content;
}

.parent-container {
  
  
  height: 92vh;
  width:100%;
  
  background-color: antiquewhite;

}

.requested {
  background-color: rgb(222, 188, 15);
  color: white;
}

.progress {
  background-color: rgb(112, 103, 212);
  color: white;
}


.completed {
  background-color: rgb(54, 171, 15);
  color: white;
}


.status {
  padding: 0.3rem;
  font-size:1rem;
  justify-content: center;
  height: fit-content;
  border: 1px solid rgba(0, 0, 0, 0);
  border-radius: 0.5rem;
  max-width: fit-content;
}

.rejected-cancelled {
  background-color: rgb(207, 44, 44);
  color: white;
}

.closed {
  background-color: gray;
  color: white;
}
</style>
