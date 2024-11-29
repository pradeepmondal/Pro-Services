<script>


export default {
  name: "AddServiceForm",
  props: {
    afterAction: {
      type: Function
    },
    category_obj: {
        type: Object
    }
  },

  components: {

  },
  data(){
    return {
      email: this.$store.state.email,
      message: null,
      formData: {
        
        name: null,
        base_price: null,
        req_time: null,
        cat_id: this.category_obj.cat_id,
        description: null,
        thumbnail: null
      }
        
        
    }
  },
  methods: {
    handleImageUpload(event) {
      this.formData.thumbnail = event.target.files[0]
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
          "http://localhost:5050" + "/service",
          {
            method: "POST",
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
    }


  }
};
</script>

<template>
    <Navbar :email />
    <div class="">
      <form class="edit-form" @submit.prevent="submitForm">
        <div class="category">
              <label for="category" class="form-label">Category: {{ category_obj.name }}</label>
             
            </div>
        
        <div class="mb-3">
          
  
          <div class="name-price mb-3">
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
  
          <div class="time-cat mb-3">
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
  
            
          </div>

          <div class="thumbnail-container mb-3">
          <div class="time">
            <label for="thumbnail" class="form-label">Thumbnail</label>
            <input
              type="file"
              class="form-control"
              id="thumbnail"
              name="thumbnail"
              @change="handleImageUpload"
              
              
            >
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
        </div>
        <div v-if="message">{{ message }}</div>
  
        <button type="submit" class="btn btn-success">Add Service</button>
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
  
  .category {
    padding: 0.5rem;
  }
  </style>