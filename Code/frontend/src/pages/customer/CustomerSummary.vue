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
        customer: this.$store.state.user_details,
        service_requests: null,

        category_wise_chart: {

          chart_data: [],
        chart_labels: [],

        },

        request_dist_chart: {
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
        const res = await fetch('http://localhost:5050' + '/service_request/'+ this.customer.c_id + '/0', {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.service_requests = data

            let cat_sr_obj = {}

            this.service_requests.forEach(sr => {
              if (sr.service.category.name in cat_sr_obj) {
                cat_sr_obj[sr.service.category.name] += 1
              }
              else {
                cat_sr_obj[sr.service.category.name] = 1

              }
              
            });

            for (const cat in cat_sr_obj) {
              this.category_wise_chart.chart_labels.push(cat)
              this.category_wise_chart.chart_data.push(cat_sr_obj[cat])

            }

            


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



            


            

            



        }
    }catch(e){
        console.error(e)
    }
        
        


    },


    renderChart() {
      new Chart(this.$refs.pie,
        {
          type: 'pie',
          data: {
            
            labels: this.category_wise_chart.chart_labels,
            datasets: [{
              data: this.category_wise_chart.chart_data,
              
            }]
          },

          options: { responsive: true, maintainAspectRatio: false, plugins: { colorschemes: { scheme: 'brewer.Paired12' } } }
        }
      )


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
    }
  }
};
</script>

<template>
<Navbar :email="email"/>

<label class="services-stats-label">{{ customer.f_name }}'s Summary</label>

<div class="chart-container">

  <div class="chart1">

    <div class="category-wise-service-distribution">
  <canvas id="pie_chart" width="400" ref="pie"></canvas>
  
</div>

<label class="pie-label">Category wise SR distribution</label>



  </div>

  <div class="chart2">

    <div class="category-wise-service-distribution">
  <canvas id="pie_chart" width="800" ref="line"></canvas>
  
</div>

<label class="pie-label">Month-wise request distribution</label>


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



</style>