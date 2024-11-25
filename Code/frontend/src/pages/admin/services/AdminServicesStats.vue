<script>
import Navbar from '../components/Navbar.vue';
import Chart from 'chart.js/auto'
import 'chartjs-plugin-colorschemes';

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
        services: null,
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
        const res = await fetch('http://localhost:5050' + '/services/0', {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.services = data

            let cat_services_obj = {}

            this.services.forEach(service => {
              if (service.category.name in cat_services_obj) {
                cat_services_obj[service.category.name] += 1
              }
              else {
                cat_services_obj[service.category.name] = 1

              }
              
            });

            for (const cat in cat_services_obj) {
              this.chart_labels.push(cat)
              this.chart_data.push(cat_services_obj[cat])

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
            labels: this.chart_labels,
            datasets: [{
              data: this.chart_data,
              
            }]
          },

          options: { responsive: true, maintainAspectRatio: false, plugins: { colorschemes: { scheme: 'brewer.Paired12' } } }
        }
      )
    }
  }
};
</script>

<template>
<Navbar :email="email"/>

<label class="services-stats-label">Services Stats</label>
<div class="category-wise-service-distribution">
  <canvas id="pie_chart" width="500" ref="pie"></canvas>
  
</div>

<label class="pie-label">Category wise service distribution</label>


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