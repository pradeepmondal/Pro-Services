<script>
export default {
  name: "EditServiceForm",
  props: {
    obj: {
      type: Object,
    },

    afterAction: {
      type: Function
    }
  },

  components: {},
  data() {
    return {
      email: this.$store.state.email,
      service_categories: null,
      message: null,
      formData: {
        s_id: this.obj.s_id,
        name: this.obj.name,
        base_price: this.obj.base_price,
        req_time: this.obj.req_time,
        description: this.obj.description,
        cat_id: this.obj.cat_id,
        thumbnail: null
      }
    };
  },
  async created() {
    await this.fetchServiceCategories();
  },
  methods: {
    async fetchServiceCategories() {
      try {
        const res = await fetch(
          "http://localhost:5050" + "/service_categories",
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
          this.service_categories = data;
        }
      } catch (e) {
        console.error(e);
      }
    },

    async submitForm() {
      const formData = new FormData()
      formData.append("name", this.formData.name)
      formData.append("base_price", this.formData.base_price)
      formData.append("req_time", this.formData.req_time)
      formData.append("cat_id", this.formData.cat_id)
      formData.append('description', this.formData.description)
      formData.append('thumbnail', this.formData.thumbnail)

      
      try {
        const res = await fetch(
          "http://localhost:5050" + "/service/"+this.formData.s_id,
          {
            method: "PUT",
            headers: {

              "auth-token": this.$store.state.auth_token,
            },
            body: formData
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
    handleImageUpload(event) {
      this.formData.thumbnail = event.target.files[0]
    },
  },
};
</script>

<template>
  <Navbar :email />
  <div class="">
    <form class="edit-form" @submit.prevent="submitForm">
      <div class="mb-3">
        <label class="form-label" :formData.s_id name="s_id" >Service Id: {{ obj.s_id }}</label
        ><br />

        <div class="name-price">
          <div class="name-container">
            <label for="name" class="form-label">Name</label>
            <input
              type="text"
              class="form-control"
              id="name"
              name="name"
              v-model="formData.name"
              
              
            />
          </div>

          <div class="price-container">
            <label for="price" class="form-label">Base Price</label>
            <input
              type="text"
              class="form-control"
              id="price"
              name="base_price"
              v-model="formData.base_price"
              
            />
          </div>
        </div>

        <div class="time-cat">
          <div class="time-container">
            <label for="req_time" class="form-label">Time Required</label>
            <input
              type="text"
              class="form-control"
              id="req_time"
              name="req_time"
              v-model="formData.req_time"
              
            />
          </div>

          <div class="price-container">
            <label for="category" class="form-label">Category</label>
            <select class="form-select" aria-label="Default select example" name="cat_id" v-model="formData.cat_id" >
              <template v-for="cat in service_categories">
                <option
                  v-if="cat.cat_id === obj.cat_id"
                  :value="cat.cat_id"
                  selected
                >
                  {{ cat.name }}
                </option>
                <option v-else :value="cat.cat_id">{{ cat.name }}</option>
              </template>
            </select>
          </div>
        </div>
        <div class="mb-3">
          <label for="description" class="form-label"
            >Description</label
          >
          <textarea
            class="form-control"
            id="description"
            rows="3"
            name="description"
            v-model="formData.description"
            
          ></textarea>
        </div>

        <div class="thumbnail-container">
          <div class="time">
            <label for="thumbnail" class="form-label">Change Thumbnail</label>
            <input
              type="file"
              id="thumbnail"
              name="thumbnail"
              class="form-control"
              @change="handleImageUpload"
              
              
            >
          </div>
          </div>
      </div>
      <div v-if="message">{{ message }}</div>

      <button type="submit" class="btn btn-success">Confirm Edit</button>
    </form>
  </div>
</template>

<style scoped>
.name-price {
  display: flex;
}

.time-cat {
  display: flex;
}

.name-price div {
  margin: 0 0.5rem;
}

.time-cat div {
  margin: 0 0.5rem;
}
</style>
