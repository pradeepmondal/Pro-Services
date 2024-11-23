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
    <h1>Welcome {{ customer.f_name }} !!</h1>
    <CustomerSearch />

    <div class="container sr-table">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Service Name</th>
            <th scope="col">Professional</th>
            <th scope="col">Price</th>
            <th scope="col">Status</th>
            <th scope="col">Ratings</th>
            <th scope="col">Action</th>
            <th scope="col">Remarks</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(sr, index) in srs">
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
            <td>{{ sr.status }}</td>
            <td>{{ sr.rating }}</td>

            <td>
              <div class="button-container">
                <button
                  v-if="sr.status === 'Accepted'"
                  class="btn btn-outline-success"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="openMarkCompleteModal(sr)"
                >
                  Mark Completed
                </button>

                <button
                  v-if="sr.status !== 'Completed' && sr.status !== 'Cancelled'"
                  class="btn btn-outline-danger"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="openCancelModal(sr)"
                >
                  Cancel
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
</style>
