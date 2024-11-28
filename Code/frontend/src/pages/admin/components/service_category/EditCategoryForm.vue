<script>


export default {
  name: "EditCategoryForm",
  props: {
    category_obj: {
        type: Object
    },
    afterAction: {
      type: Function
    }
  },

  components: {

  },
  data(){
    return {
      email: this.$store.state.email,
      message: null,
      formData: {
        
        name: this.category_obj.name,
        description: this.category_obj.description,
        thumbnail: null
      }
        
        
    }
  },
  methods: {
    handleImageUpload(event) {
      this.formData.thumbnail = event.target.files[0]
    },

    async updateCategory() {
      const formData = new FormData()
      
      formData.append("name", this.formData.name)
      formData.append('description', this.formData.description)
      if (thumbnail){
      formData.append('thumbnail', this.formData.thumbnail)
      }

      
      try {
        const res = await fetch(
          "http://localhost:5050" + "/service_category/" + this.category_obj.cat_id,
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
    }


  }
};
</script>

<template>
  <Navbar :email />
    <div class="">
    

        <form class="edit-form" @submit.prevent="submitForm">
      <div class="mb-3">
        

        
          <div class="name-container">
            <label for="name" class="form-label">Name: </label>
            <input
              type="text"
              class="form-control"
              id="name"
              name="name"
              v-model="formData.name"
            />
          </div>
          <br />

          <div class="description-container">
            <label for="description" class="form-label">Description</label>
            <textarea
              type="text"
              class="form-control"
              id="description"
              name="description"
              v-model="formData.description"
              
            ></textarea>
          </div>
          <br />
        

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
        <br />
       
      </div>
      <div v-if="message">{{ message }}</div>

      <button type="submit" class="btn btn-success" @click="updateCategory">Update Category</button>
    </form>


        
    </div>


</template>


<style scoped>


.name-price div {
  margin: 0 0.5rem;
}

.time-cat div {
  margin: 0 0.5rem;
}


</style>