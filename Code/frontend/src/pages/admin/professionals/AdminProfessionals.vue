<script>
import Navbar from '.././components//Navbar.vue';
import AdminModal from '.././components/AdminModal.vue';
import AdminSearch from '.././components/AdminSearch.vue';

export default {
  name: "AdminSPs",

  components: {
    Navbar,
    AdminSearch,
    AdminModal
  },
  data() {
    return {
      email: this.$store.state.email,
      sps: null,
      modal_type: null,
      obj: null,
      modal_heading: null,
      s_no: 0,
      search_mode: false,
      search_query: null,
      search_param: null,

      task_created_message: null,
      pending_task: false,
      pending_task_id: null,
      task_completed: false,
      pending_task_sp: null
    };
  },

  async created() {
    await this.fetchSPs()
  },

  computed: {

    final_sps(){
      if(!this.search_mode){
        return this.sps
      }
      else{
        let search_query = this.search_query.toLowerCase()
        let search_param = this.search_param
        let regex = new RegExp(search_query, 'i')
        return this.sps.filter((sp) => {
            if(search_param === 'professional_name'){
              return regex.test(sp.f_name + ' ' + sp.l_name )
            }
            else if(search_param === 'email'){
              return regex.test(sp.email)
            }
            else if(search_param === 'service_name'){
              return regex.test(sp.service.name)
            }
            else if(search_param === 'pincode'){
              return regex.test(sp.loc_pincode)
            }
             
         
        })

      }
    },

  },

  methods: {
    async fetchSPs() {
        try{
        const res = await fetch('http://localhost:5050' + '/sps/0' , {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.sps = data



        }
    }catch(e){
        console.error(e)
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




    blockSP(sp){
        this.modal_type = "block_sp_form"
        this.obj = sp
        this.modal_heading = "Block " + sp.f_name
    },

    unblockSP(sp){
        this.modal_type = "unblock_sp_form"
        this.obj = sp
        this.modal_heading = "Unblock " + sp.f_name
    },

    viewSP(sp){
        this.modal_type = "view_sp_form"
        this.obj = sp
        this.modal_heading = sp.f_name
    },

    deleteSP(sp){
      this.modal_type = "delete_sp_form"
      this.obj = sp
      this.modal_heading = "Delete " + sp.f_name

    },

    verifySP(sp){
      this.modal_type = "verify_sp_form"
      this.obj = sp
      this.modal_heading = "Verify " + sp.f_name

    },




    async exportSRCSV(sp) {
      try {
        const res = await fetch(
          "http://localhost:5050" + "/celery/create_sp_sr_export_request/" + sp.sp_id,
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
          this.pending_task = true;
          this.pending_task_id = data.task_id;
          this.pending_task_sp = sp;
          this.task_created_message = "Export Request Created";
          setTimeout(() => {
            this.task_created_message = null;
          }, 2000);

          const interval = setInterval(async () => {
            try {
              const res = await fetch(
                "http://localhost:5050" +
                  "/celery/check_sr_export/" +
                  this.pending_task_id,
                {
                  method: "GET",
                  headers: {
                    "content-type": "application/json",
                    "auth-token": this.$store.state.auth_token,
                  },
                }
              );
              if (res.ok) {
                this.task_completed = true;
                
                clearInterval(interval);
              }
            } catch (e) {
              console.error(e);
            }
          }, 1000);
        }
      } catch (e) {
        console.error(e);
      }
    },


    async downloadSRCSV() {
      try {
        const res = await fetch(
          "http://localhost:5050" + "/celery/get_sr_export/" + this.pending_task_id,
          {
            method: "GET",
            headers: {
              "content-type": "application/json",
              "auth-token": this.$store.state.auth_token,
            },
          }
        );
        if (res.ok) {
          const blob = await res.blob()
          const download_url = window.URL.createObjectURL(blob)
          window.open(download_url)

          this.pending_task = false
          this.pending_task_id = null
          this.task_completed = false
          this.pending_task_sp = null


          



        }
      } catch (e) {
        console.error(e);
      }
    },


  },
};
</script>

<template>
  <Navbar :email />
<div class="parent-container">
  <div class="notification">
    <div v-if="task_created_message" class="task-created-message">
      {{ task_created_message }}
    </div>
    <div v-if="task_completed" class="task-completed-message">
      <button class="btn btn-success" @click="downloadSRCSV" >Download {{ pending_task_sp.f_name }}'s' Report</button>
    </div>
  </div>
  <AdminModal :modal_type="modal_type" :obj="obj" :heading="modal_heading" :afterAction="fetchSPs" />
  <div class="">
    <h2 class="heading">Service Professionals</h2>
    <AdminSearch search_placeholder="Search in Professionals" :updateSearchQuery="updateSearchQuery" :clearSearch="clearSearch" :search_mode="search_mode" search_param_req="true" search_in="admin_professionals"/>
    

    <div class="container professional-table">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Email</th>
            <th scope="col">Professional Name</th>
            <th scope="col">Service Name</th>
            <th scope="col">Pincode</th>
            <th scope="col">Rating</th>
            <th scope="col">Verification Status</th>
            <th scope="col">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(sp, index) in final_sps">
            <td scope="row">
              <div>
                {{ index+1 }}
              </div>
            </td>
            <td><div class="sp_email" data-bs-toggle="modal" data-bs-target="#staticBackdrop" @click="viewSP(sp)">{{ sp.email }}</div></td>
            <td>{{ sp.f_name + ' ' + sp.l_name }}</td>
            <td>{{ sp.service.name }}</td>
            <td>{{ sp.loc_pincode }}</td>
            <td>{{ sp.rating }}</td>
            <td>{{ sp.verification_status }}</td>
            <td>
              <div class="button-container">
                <button
                  v-if="sp.active"
                  class="btn btn-outline-danger"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="blockSP(sp)"
                >
                  Block
                </button>

                <button
                  v-if="!sp.active"
                  class="btn btn-outline-success"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="unblockSP(sp)"
                >
                  Unblock
                </button>

                <button
                  class="btn btn-outline-danger"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="deleteSP(sp)"
                >
                  Delete
                </button>

                <button
                  v-if="!(sp.verified) && (sp.verification_status === 'Pending')"
                  class="btn btn-outline-success"
                  data-bs-toggle="modal"
                  data-bs-target="#staticBackdrop"
                  @click="verifySP(sp)"
                >
                  Verify
                </button>

                <button
                  v-if="(sp.verification_status === 'Approved') && (sp.service_requests)"
                  class="btn btn-outline-success"
                  
                  @click="exportSRCSV(sp)"
                >
                  Download SR Report
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</template>

<style scoped>

.button-container {
    max-width: fit-content;

}

.button-container button {
    margin: 0 0.4rem;
    width: fit-content;
}

.sp_email {
    text-decoration: underline;
    cursor: pointer;

}

.task-created-message {
  display: flex;
  background-color: rgba(178, 201, 51, 0.432);
  color: black;
  max-width: fit-content;

  padding: 0.5rem;
  border: 1px solid rgba(178, 201, 51, 0.432);
  border-radius: 1rem;
}

.task-completed-message button {
  border: 1px solid rgba(217, 170, 100, 0.637);
  border-radius: 1rem;
}

.notification {
  display: flex;
  position: absolute;
  right: 2rem;
  margin-right: 1rem;
  margin-top: 0.8rem;
}

.parent-container {
  
  
  height: 92vh;
  width:100%;
  
  background-color: antiquewhite;

}

.heading {
  padding: 1rem;
}

.professional-table {
  margin-top: 2rem;
}

</style>
