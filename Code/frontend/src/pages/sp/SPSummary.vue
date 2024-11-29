<script>
import Navbar from './components/Navbar.vue';
import Chart from 'chart.js/auto'


export default {
  name: "Pie",
  components: {
    Navbar
  },

  props: {

  },
  data(){
    return {
        email : this.$store.state.email,
        sp: this.$store.state.user_details,
        service_requests: null,

        request_dist_chart: {

          chart_data: [],
        chart_labels: [],

        },

        rating_dist_chart: {
          chart_data: [],
          chart_labels: []
        },
        
        loading: true
        
    }
  },



  async created() {
    try {
      await this.fetchData();
      this.renderChart()
    } catch (e) {
      console.error(e);
    } finally {
      this.loading = false;
    }
  },




  methods: {
    async fetchData() {
        try{
        const res = await fetch('http://localhost:5050' + '/service_request/0/' + this.sp.sp_id , {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.service_requests = data

            let month_wise_req_obj = { 
              January: 0,
              February: 0,
              March: 0,
              April: 0,
              May: 0, 
              June: 0, 
              July: 0, 
              August: 0, 
              September: 0, 
              October: 0, 
              November: 0, 
              December: 0 
            }

            let month_num_to_name = {
              0: 'January',
              1: 'February',
              2: 'March',
              3: 'April',
              4: 'May',
              5: 'June',
              6: 'July',
              7: 'August',
              8: 'September',
              9: 'October',
              10: 'November',
              11: 'December',

            }

            this.service_requests.forEach(sr => {
              let request_date = new Date(sr.request_date)
              let request_month = month_num_to_name[request_date.getMonth()]

              if (request_month in month_wise_req_obj) {
                month_wise_req_obj[request_month] += 1
              }
              else {
                month_wise_req_obj[request_month] = 1

              }
              
            });

            for (const request_month in month_wise_req_obj) {
              this.request_dist_chart.chart_labels.push(request_month)
              this.request_dist_chart.chart_data.push(month_wise_req_obj[request_month])

            }



            let rating_sr_obj = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

            this.service_requests.forEach(sr => {
              if (sr.rating > 0) {
              if (sr.rating in rating_sr_obj) {
                rating_sr_obj[sr.rating] += 1
              }
              else {
                rating_sr_obj[sr.rating] = 1

              }
            }
              
            });

            for (const rating_label in rating_sr_obj) {
              this.rating_dist_chart.chart_labels.push(rating_label)
              this.rating_dist_chart.chart_data.push(rating_sr_obj[rating_label])

            }



            


            

            



        }
    }catch(e){
        console.error(e)
    }
        
        


    },


    renderChart() {
      new Chart(this.$refs.line,
        {
          type: 'line',
          data: {
            
            labels: this.request_dist_chart.chart_labels,
            datasets: [{
              label: 'No. of Requests Created',
              data: this.request_dist_chart.chart_data,
              
            }]
          },

          options: { scales: {
            y: {
              ticks: {
                stepSize: 1
              }
            }

          }, responsive: true, maintainAspectRatio: false, plugins: { colorschemes: { scheme: 'brewer.Paired12' } } }
        }
      )


      new Chart(this.$refs.bar,
        {
          type: 'bar',
          data: {
          
            labels: this.rating_dist_chart.chart_labels,
            datasets: [{
              label: 'SR Count',
              data: this.rating_dist_chart.chart_data,
              
            }]
          },

          options: { responsive: true, maintainAspectRatio: false,

            scales: {
              x: {
                title: {
                  display: true,
                  text: 'SR count'
                },
                
                ticks: {
                  stepSize: 1
                },
              },

              y: {
                title: {
                  display: true,
                  text: 'Ratings'
                },
                ticks: {
                  stepSize: 1
                },
              },
            },
            
            
            indexAxis: 'y',
            skipNull: true,
            
            
            
            
            plugins: {
              legend: {
        position: 'right',
      },
      title: {
        display: false,
        text: 'Ratings distribution across SRs'
      },
              
              
              colorschemes: { scheme: 'brewer.Paired12' } } }
        }
      )
    }
  }
};
</script>

<template>
<Navbar :email="email"/>
<div class="parent-container">

<label class="services-stats-label">{{ sp.f_name }}'s Stats</label>

<div class="chart-container">

  <div class="chart1">

<div class="category-wise-service-distribution">
<canvas id="pie_chart" width="600" ref="bar"></canvas>

</div>

<label class="pie-label">Ratings distribution across SRs</label>


</div>


  <div class="chart2">

    <div class="category-wise-service-distribution">
  <canvas id="pie_chart" width="600" ref="line"></canvas>
  
</div>

<label class="pie-label">Month-wise Request Distribution</label>



  </div>







</div>
</div>

</template>


<style scoped>

.category-wise-service-distribution {
  margin-top: 2rem;
}


.pie-label {
  padding: 2rem;
  display: flex;
  max-width: fit-content;
  margin: auto;
}

.services-stats-label {
  font-size: 2rem;
  padding: 1rem;

}

.chart-container {
  display: flex;
 
  justify-content: space-around;
}

.parent-container {
  
  
  height: 92vh;
  width:100%;
  
  background-color: antiquewhite;

}

</style>