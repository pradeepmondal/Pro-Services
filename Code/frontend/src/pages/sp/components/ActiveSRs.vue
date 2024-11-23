<script>

import SPSearch from "./SPSearch.vue";
import SRActionModal from "./SRActionModal.vue";

export default {
  name: "ActiveSRs",
  components: {

    SPSearch,
    SRActionModal,
  },
  data() {
    return {
      sp: this.$store.state.user_details,
      // loading: true,
      srs: null,
      srs_active: null,
      srs_pending: null,
      modal_type: null,
      modal_heading: null,
      action: null,
      show_modal: false,
      selected_sr: null,
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
          this.srs_active = this.srs.filter((sr) => ((sr.status === 'Accepted') || (sr.status === 'Completed')))
          this.srs_pending = this.srs.filter((sr) => (sr.status === 'Requested'))
          
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
            await this.fetchSR();
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
            await this.fetchSR();
          }
        } catch (e) {
          console.error(e);
        }
      }
    },

    async rejectSR(sr, remarks) {
      sr.status = "Reject";
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
            await this.fetchSR();
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
  },
};
</script>

<template>
  <Navbar />

  <SRActionModal :modal_type="modal_type"
    :modal_heading="modal_heading"
    :action="action"
    :selected_sr="selected_sr"
  />
  <div class="container-fluid">
    
    <SPSearch />
    
    <h2>Active Requests</h2>
    <div class="container sr-table">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Customer Name</th>
            <th scope="col">Description</th>
            
            <th scope="col">Status</th>
            <th scope="col">Ratings</th>
            <th scope="col">Action</th>
            <th scope="col">Remarks</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(sr, index) in srs_active">
            <td scope="row">
              <div>
                {{ sr.sr_id }}
              </div>
            </td>
            <td>
              <div class="service_name">{{ sr.customer_name }}</div>
            </td>
            <td>{{ sr.description }}</td>
            
            <td>{{ sr.status }}</td>
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

    <h2>Pending Requests</h2>
    <div class="container sr-table">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Customer Name</th>
            <th scope="col">Description</th>
            
            <th scope="col">Status</th>
            <th scope="col">Ratings</th>
            <th scope="col">Action</th>
            <th scope="col">Remarks</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(sr, index) in srs_pending">
            <td scope="row">
              <div>
                {{ sr.sr_id }}
              </div>
            </td>
            <td>
              <div class="service_name">{{ sr.customer_name }}</div>
            </td>
            <td>{{ sr.description }}</td>
            
            <td>{{ sr.status }}</td>
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
</style>
