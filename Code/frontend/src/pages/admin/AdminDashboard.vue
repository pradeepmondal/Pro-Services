<script>
import Navbar from "./components/Navbar.vue";
import AdminSearch from "./components/AdminSearch.vue";
import AdminTiles from "./components/AdminTiles.vue";

export default {
  name: "AdminDashboard",
  components: {
    Navbar,
    AdminSearch,
    AdminTiles,
  },
  data() {
    return {
      email: null,
      task_created_message: null,
      pending_task: false,
      pending_task_id: null,
      task_completed: false,
    };
  },
  async created() {
    await this.fetchAdmin();
  },

  methods: {
    async fetchAdmin() {
      try {
        const res = await fetch("http://localhost:5050" + "/admin", {
          method: "GET",
          headers: {
            "content-type": "application/json",
            "auth-token": this.$store.state.auth_token,
          },
        });
        if (res.ok) {
          const data = await res.json();
          this.email = data.email;
        }
      } catch (e) {
        console.error(e);
      }
    },

    async exportSRCSV() {
      try {
        const res = await fetch(
          "http://localhost:5050" + "/celery/create_sr_export_request",
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
      <button class="btn btn-success" @click="downloadSRCSV" >Download SR Report</button>
    </div>
  </div>
  <h2 class="welcome-message">Admin Dashboard</h2>

  <div class="container-fluid dashboard-tiles">
    <AdminTiles :exportSRCSV="exportSRCSV" />
  </div>

</div>
</template>

<style scoped>
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
.dashboard-tiles {
  
  padding-top: 2rem;
}

.parent-container {
  
  
  height: 92vh;
  width:100%;
  
  background-color: antiquewhite;

}

.welcome-message {
  padding: 1rem;
  padding-top: 0.5rem;
  padding-bottom: 0rem;
}



</style>




