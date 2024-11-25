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
        professionals: null,

        category_wise_chart: {

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
        const res = await fetch('http://localhost:5050' + '/sps/0', {method: 'GET', headers: {"content-type" : "application/json", 'auth-token': this.$store.state.auth_token}})
        if(res.ok){

            const data = await res.json()
            this.professionals = data

            let cat_sp_obj = {}

            this.professionals.forEach(sp => {
              if (sp.service.category.name in cat_sp_obj) {
                cat_sp_obj[sp.service.category.name] += 1
              }
              else {
                cat_sp_obj[sp.service.category.name] = 1

              }
              
            });

            for (const cat in cat_sp_obj) {
              this.category_wise_chart.chart_labels.push(cat)
              this.category_wise_chart.chart_data.push(cat_sp_obj[cat])

            }

            let rating_sr_obj = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

            this.professionals.forEach(sr => {


              if (sr.rating > 0) {

                sr.rating = Math.round(sr.rating)
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


      new Chart(this.$refs.bar,
        {
          type: 'bar',
          data: {
          
            labels: this.rating_dist_chart.chart_labels,
            datasets: [{
              label: 'Professional Count',
              data: this.rating_dist_chart.chart_data,
              
            }]
          },

          options: { responsive: true, maintainAspectRatio: false,
            
            scales: {
              x: {

                title: {
                  display: true,
                  text: 'Ratings'
                },
                
                ticks: {
                  stepSize: 1
                },
              },

              y: {
                title: {
                  display: true,
                  text: 'Professional Count'
                },
                
                ticks: {
                  stepSize: 1
                },
              },
            },
            indexAxis: 'x',
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

<label class="services-stats-label">Professional Stats</label>

<div class="chart-container">

  <div class="chart1">

    <div class="category-wise-service-distribution">
  <canvas id="pie_chart" width="400" ref="pie"></canvas>
  
</div>

<label class="pie-label">Category wise Professionals distribution</label>



  </div>

  <div class="chart2">

    <div class="category-wise-service-distribution">
  <canvas id="pie_chart" width="700" ref="bar"></canvas>
  
</div>

<label class="pie-label">Ratings distribution across Professionals</label>


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