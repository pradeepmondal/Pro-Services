<script>
import AdminSearch from "../components/AdminSearch.vue"
import Navbar from "../components/Navbar.vue"

import SRActionModal from "../components/service_category/service_request/SRActionModal.vue";

export default {
  name: "AdminSRs",
  components: {
    Navbar,
    AdminSearch,
    SRActionModal,
  },
  data() {
    return {
      email: this.$store.state.email,
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
            if(search_param === 'customer_name'){
              return regex.test(sr.customer_name )
            }
            else if(search_param === 'professional_name'){
              return regex.test(sr.professional_name)
            }
            else if(search_param === 'service_name'){
              return regex.test(sr.service_name)
            }
            else if(search_param === 'description'){
              return regex.test(sr.description)
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
            "/service_request/0/0",
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

    updateSearchQuery(search_input, search_param){
      this.search_mode = true
      this.search_query = search_input
      this.search_param = search_param
    },

    clearSearch(){
      this.search_mode = false
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

    openDeleteModal(sr) {
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
  },
};
</script>

<template>
  <Navbar :email="email" />

  <SRActionModal
    :modal_type="modal_type"
    :modal_heading="modal_heading"
    :action="action"
    :selected_sr="selected_sr"
  />
  <div class="parent-container">
    <h2 class="heading">Service Requests</h2>
    <AdminSearch search_placeholder="Search in Service Requests" :updateSearchQuery="updateSearchQuery" :clearSearch="clearSearch" :search_mode="search_mode" search_param_req="true" search_in="admin_srs" />

    <div class="container sr-table">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Service Name</th>
            <th scope="col">Customer Name</th>
            <th scope="col">Professional</th>
            <th scope="col">Price</th>
            <th scope="col">Status</th>
            <th scope="col">Ratings</th>
            <th scope="col">Description</th>
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
            <td>{{ sr.customer_name }}</td>
            <td>₹{{ sr.professional_price }}</td>
            <td > <div v-if="sr.status === 'Requested'" class="status requested">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'In Progress'" class="status progress">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'Completed'" class="status completed">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'Rejected'" class="status rejected-cancelled">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'Cancelled'" class="status rejected-cancelled">{{ sr.status }}</div>
              <div v-else-if="sr.status === 'Closed'" class="status closed">{{ sr.status }}</div>
            </td>
            <td>{{ sr.rating }}</td>

            <td>
              {{ sr.description }}
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

.parent-container {
  
  
  height: 92vh;
  width:100%;
  
  background-color: antiquewhite;

}

.heading {
  padding: 1rem;
}
</style>
