<script>
export default {
  name: "AddAddressForm",
  props: {
    customer: {
      type: Object,
    },
    afterAction: {
        type: Function
    },
    
  },
  data() {
    return {
        formData: {
            address: null,
            pincode: null
        },
        message: null
    }
  },
  methods: {
    async addAddress(){
      try {
        const formData = new FormData()
        formData.append('address', this.formData.address)
        formData.append('pincode', this.formData.pincode)

        const res = await fetch(
          "http://localhost:5050" + "/customer_address",
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
          await new Promise((res, rej) => {
            setTimeout(() => {
            console.log('waiting...');
            res('Done')
            
          }, 2000)
          })
          
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
  <div class="address-form">
    <form class="edit-form" @submit.prevent="submitForm">
      <div class="full-address">
        <div class="address">
          <label for="name" class="form-label">Address</label>
          <input
            type="text"
            class="form-control"
            id="name"
            name="name"
            v-model="formData.address"
            required
          />
        </div>

        <div class="pincode">
          <label for="pincode" class="form-label">Pincode</label>
          <input
            type="text"
            class="form-control"
            id="pincode"
            name="base_price"
            v-model="formData.pincode"
            required
          />
        </div>
      </div>

      <div v-if="message">{{ message }}</div>

      <button type="submit" class="btn btn-success" @click="addAddress">Add Address</button>
    </form>
  </div>
</template>

<style scoped>
.address-form {
  width: max-content;
  right: 0;
  margin-top: 1rem;
  margin-right: 1rem;
  display: flex;
  background-color: rgb(242, 207, 143);
  padding: 0.5rem;
  border: 1px solid orange;
  border-radius: 0.75rem;
  position: absolute;
}

.address-form i {
  color: red;
  font-size: 1.1rem;
  padding: 0.3rem 0.8rem;
}

.full-address div {
    padding: 0.7rem;
}

form {
    display: flex;
    flex-wrap: nowrap;
    flex-direction: column;
}

button {
    margin-top: 1rem;
}
</style>
