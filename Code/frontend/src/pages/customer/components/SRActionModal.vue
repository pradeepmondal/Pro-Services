<script>
export default {
  name: "SRActionModal",
  components: {},
  props: {
    selected_sr: {
      type: Object,
    },
    action: {
      type: Function,
    },

    modal_type: {
      type: String,
    },
    modal_heading: {
      type: String,
    },
  },

  data() {
    return {
      customer: this.$store.state.user_details,
      rating: null
    };
  },

  //   async created() {
  //     try {
  //       await this.fetchSPs()
  //     } catch (e) {
  //       console.error(e)

  //     } finally {
  //       this.loading = false
  //     }
  //   },

  methods: {},
};
</script>

<template>
  <Navbar :email />
  <div class="">
    <!-- Button trigger modal
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
  Launch static backdrop modal
</button> -->

    <!-- Modal -->
    <div
      class="modal fade"
      id="staticBackdrop"
      data-bs-backdrop="static"
      data-bs-keyboard="false"
      tabindex="-1"
      aria-labelledby="staticBackdropLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="staticBackdropLabel">
              {{ modal_heading }}
            </h1>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <div v-if="modal_type === 'cancel_sr'">
              Cancel {{ selected_sr.service_name }} by
              {{ selected_sr.professional_name }}
            </div>
            <div v-if="modal_type === 'mark_complete_sr'">
              Mark {{ selected_sr.service_name }} by
              {{ selected_sr.professional_name }} as completed
            </div>
            <div
              v-if="modal_type === 'mark_complete_sr'"
              class="rating-container"
            >
              <label>Give Rating:</label>
              <div class="form-check">
                <input
                  class="form-check-input"
                  type="radio"
                  name="flexRadioDefault"
                  id="flexRadioDefault1"
                  v-model="rating"
                  value=1
                />
                <label class="form-check-label" for="flexRadioDefault1">
                  1
                </label>

                
              </div>

              <div class="form-check">
                <input
                  class="form-check-input"
                  type="radio"
                  name="flexRadioDefault"
                  id="flexRadioDefault1"
                  v-model="rating"
                  value=2
                />
                <label class="form-check-label" for="flexRadioDefault1">
                  2
                </label>

                
              </div>

              <div class="form-check">
                <input
                  class="form-check-input"
                  type="radio"
                  name="flexRadioDefault"
                  id="flexRadioDefault1"
                  v-model="rating"
                  value=3
                />
                <label class="form-check-label" for="flexRadioDefault1">
                  3
                </label>

                
              </div>

              <div class="form-check">
                <input
                  class="form-check-input"
                  type="radio"
                  name="flexRadioDefault"
                  id="flexRadioDefault1"
                  v-model="rating"
                  value=4
                />
                <label class="form-check-label" for="flexRadioDefault1">
                  4
                </label>

                
              </div>
              

              <div class="form-check">
                <input
                  class="form-check-input"
                  type="radio"
                  name="flexRadioDefault"
                  id="flexRadioDefault1"
                  v-model="rating"
                  value=5
                />
                <label class="form-check-label" for="flexRadioDefault1">
                  5
                </label>

                
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button
              v-if="modal_type === 'cancel_sr'"
              type="button"
              class="btn btn-danger"
              @click="action(selected_sr)"
              data-bs-dismiss="modal"
            >
              Cancel
            </button>
            <button
              v-if="modal_type === 'mark_complete_sr'"
              type="button"
              class="btn btn-success"
              @click="action(selected_sr, rating)"
              data-bs-dismiss="modal"
            >
              Mark Complete
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

.rating-container {
  display: flex;
  padding: 1rem;
}

.rating-container div {
  padding: 1.5rem;
}

</style>
