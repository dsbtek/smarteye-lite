<template>
  <div id="app">
    <div class="wrap-container">
      <div class="header">
        <img :src="logo" alt="Logo" class="image-size-logo" />
      </div>
      <div class="main-body">
        <home v-if="tankData.length > 0" :tank-data="tankData" />
        <div v-else>
          <img :src="spinner" alt="Loader" class="image-size-spinner" />
        </div>
      </div>
      <div class="footer">
        <i class="fa fa-bolt fa-lg" style="color: red;"></i> 
        <img :src="footerLogo" alt="Footer logo" class="image-size-footer" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import home from './components/index-home.vue';
import 'font-awesome/css/font-awesome.min.css'; 
import 'font-awesome/fonts/fontawesome-webfont.ttf';

export default {
  name: 'App',
  components: {
    home,
  },
  data() {
    return {
      tankData: [],
      logo: require('./assets/Smarteye-newLogo.png'),
      footerLogo: require('./assets/smart-flow.png'),
      spinner: require('./assets/Smartflow-rotating-logo.gif'),
    };
  },
  created() {
    // Call the fetchData method every 90 seconds
    setInterval(this.fetchData, 9000); // 90 seconds = 90,000 milliseconds
  },
  methods: {
    fetchData() {
      axios.get('http://localhost:8000/tank-logs-temp/')
        .then(response => {
          this.tankData = response.data;
        })
        .catch(error => {
          console.error('API error:', error);
        });
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  height: 100%;
  width: 100%;
}

body {
  margin: 0;
  padding: 0;
}

.main-body {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 80%;
  width: 100%;
}

.wrap-container {
  height: 100vh;
  width: 100%;
}

.header {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  /* background-color: rgb(218, 218, 218); */
  box-shadow: rgba(0, 0, 0, 0.07) 0px 1px 1px, rgba(0, 0, 0, 0.07) 0px 2px 2px, rgba(0, 0, 0, 0.07) 0px 4px 4px, rgba(0, 0, 0, 0.07) 0px 8px 8px, rgba(0, 0, 0, 0.07) 0px 16px 16px;
  height: 10%;
  width: 100%;
}

.footer {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-end;
  background-color: rgb(240, 240, 240);
  height: 10%;
  width: 100%;
}

.image-size-logo {
  /* width: 200px; */
  height: 50px;
  margin-left: 3em;
}

.image-size-spinner {
  /* width: 200px; */
  height: 100px;
}

.image-size-footer {
  /* width: 200px; */
  height: 50px;
  margin-right: 3em;

}
</style>
