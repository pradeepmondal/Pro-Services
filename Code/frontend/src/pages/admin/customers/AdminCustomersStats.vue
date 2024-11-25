<script>
import Navbar from '../components/Navbar.vue';
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
        customers: null,
        chart_data: [],
        chart_labels: [],
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
        const res = await fetch('http://localhost:5050' + '/customers', {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.customers = data

            let month_wise_cust_obj = { 
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

            this.customers.forEach(c => {
              let join_date = new Date(c.date_created)
              let join_month = month_num_to_name[join_date.getMonth()]

              if (join_month in month_wise_cust_obj) {
                month_wise_cust_obj[join_month] += 1
              }
              else {
                month_wise_cust_obj[join_month] = 1

              }
              
            });

            for (const join_month in month_wise_cust_obj) {
              this.chart_labels.push(join_month)
              this.chart_data.push(month_wise_cust_obj[join_month])

            }

            


            

            



        }
    }catch(e){
        console.error(e)
    }
        
        


    },


    renderChart() {
      new Chart(this.$refs.pie,
        {
          type: 'line',
          data: {
            
            labels: this.chart_labels,
            datasets: [{
              label: 'No. of Customers Joined',
              data: this.chart_data,
              
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
<div class="container">
<label class="services-stats-label">Customer Stats</label>
<div class="category-wise-service-distribution">
  <canvas id="pie_chart" width="600" ref="pie"></canvas>
  
</div>

<label class="pie-label">Month-wise Customer Onboarding Distribution</label>

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

</style>