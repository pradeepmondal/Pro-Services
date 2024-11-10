<script>
import Login from './Login.vue'

export default {
  components : {
    Login
  }
}

</script>

<template>
  <div class="custom-container">
    <h1 id="heading"></h1>
    <div class="hovering-img-container">
      <img class="graphics-1" src="../assets/graphic-1.png" />
      <img class="graphics-2" src="../assets/graphic-2.png" />
    </div>
    <Login />

    
  </div>

  <!-- <ul>
        <li><router-link to='/login'>Login</router-link></li>
        <li><router-link to='/signup'>Sign Up</router-link></li>
    </ul> -->
</template>

<style>
body {
  background-color: black;
}
</style>

<style scoped>


.custom-container {
  display: flex;
  justify-content: space-between;
  padding: 5rem;
  border: 2px solid green;
  height: 100vh;
  background-color: hsl(268, 48%, 71%);
}

.hovering-img-container {
  padding: 2rem 1rem;
  display: flex;
  flex-direction: column;
  border: 2px solid hsl(279, 72%, 39%);
  width: fit-content;
  height: fit-content;
  background-color: hsl(279, 43%, 55%);
  border-radius: 2rem;
  
}

.graphics-1 {
  background-color: rgb(215, 237, 245);
}
.graphics-2 {
  background-color: rgb(255, 179, 0);
}

.hovering-img-container img {
  width: 22rem;
  padding: 2rem;
}

</style>
