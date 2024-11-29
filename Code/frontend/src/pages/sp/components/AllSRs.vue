<script>

import SPSearch from "./SPSearch.vue";
import SRActionModal from "./SRActionModal.vue";

export default {
  name: "AllSRs",
  components: {

    SPSearch,
    SRActionModal,
  },
  data() {
    return {
      sp: this.$store.state.user_details,
      // loading: true,
      srs: null,
      modal_type: null,
      modal_heading: null,
      action: null,
      show_modal: false,
      selected_sr: null,
      search_mode: false,
      search_query: null,
      search_param: null
    };


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
            else if(search_param === 'customer_name'){
              return regex.test(sr.customer_name)
            }
            else if(search_param === 'address'){
              return regex.test(sr.customer.address + ', ' + sr.customer.loc_pincode)
            }
            else if(search_param === 'rating'){
              return regex.test(sr.rating)
            }
            
             
         
        })

      }
    },
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

  methods: {
    async fetchSR() {
      try {
        const res = await fetch(
          "http://localhost:5050" +
            "/service_request/0/" +
            this.sp.sp_id,
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
          
        }
      } catch (e) {
        console.error(e);
      }
    },

    async markClose(sr, remarks) {

        sr.status = "Closed";
        sr.remarks = remarks

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

    async acceptSR(sr, remarks) {
      sr.status = "Accepted";
      sr.remarks = remarks

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

    async rejectSR(sr, remarks) {
      sr.status = "Rejected";
      sr.remarks = remarks

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

    openAcceptModal(sr) {
      this.modal_type = "accept_sr";
      this.modal_heading = "Accept SR #" + sr.sr_id;
      this.action = this.acceptSR;
      this.show_modal = true;
      this.selected_sr = sr;
    },

    openRejectModal(sr) {
      this.modal_type = "reject_sr";
      this.modal_heading = "Reject SR #" + sr.sr_id;
      this.action = this.rejectSR;
      this.show_modal = true;
      this.selected_sr = sr;
    },

    openMarkCloseModal(sr) {
      this.modal_type = "mark_close_sr";
      this.modal_heading = "Mark Close SR #" + sr.sr_id;
      this.action = this.markClose;
      this.show_modal = true;
      this.selected_sr = sr;
    },

    updateSearchQuery(search_input, search_param){
      this.search_mode = true
      this.search_query = search_input
      this.search_param = search_param
    },

    clearSearch(){
      this.search_mode = false
    },

    handleDate(dateString){
      let date = new Date(dateString)
      return date.getFullYear()+'-'+(date.getMonth()+1)+'-' + date.getDate()
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
    
   
    
    <h2 class="heading">Service History</h2>
    <SPSearch search_placeholder="Search in Service Requests" :updateSearchQuery="updateSearchQuery" :clearSearch="clearSearch" :search_mode="search_mode" search_param_req="true" search_in="sp_all_srs" />
    <div class="container sr-table">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Request Date</th>
            <th scope="col">Customer Name</th>
            <th scope="col">Description</th>
            <th scope="col">Address</th>
            <th scope="col">Status</th>
            <th scope="col">Ratings</th>
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

            <td>{{ handleDate(sr.request_date) }}</td>
            <td>
              <div class="service_name">{{ sr.customer_name }}</div>
            </td>
            <td>{{ sr.description }}</td>
            <td>{{ sr.address }}</td>
            <td > <div v-if="sr.status === 'Requested'" class="status requested">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'In Progress'" class="status progress">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'Completed'" class="status completed">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'Rejected'" class="status rejected-cancelled">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'Cancelled'" class="status rejected-cancelled">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'Closed'" class="status closed">{{ sr.status }}</div>
            </td>
            <td>{{ sr.rating }}</td>

            <td>
              <div class="button-container">
                <button
                  v-if="sr.status === 'Completed'"
                  class="btn btn-outline-secondary"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="openMarkCloseModal(sr)"
                >
                  Mark Close
                </button>

                <button
                  v-if="sr.status ==='Requested'"
                  class="btn btn-outline-success"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="openAcceptModal(sr)"
                >
                  Accept
                </button>

                <button
                  v-if="sr.status ==='Requested'"
                  class="btn btn-outline-danger"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="openRejectModal(sr)"
                >
                  Reject
                </button>

                
              </div>
            </td>
            <td><label> {{ sr.remarks }}</label> </td>
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

.heading {
  padding-top: 1rem;
}
</style>
