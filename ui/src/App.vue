<template>
  <div id="app">
   
    <div class="wrap-container">
      <div class="header">
        <img :src="logo" alt="Logo" class="image-size-logo" />
        <div class="filter-items">
          <b-form-select class="w-50 p-3" v-model="selectedProduct" :options="productOptions" @change="filterByProduct">
            <template v-slot:first>
              <option value="" disabled>Select Product to filter</option>
            </template>
          </b-form-select>
        </div>
        <div class="profile">
          <b-dropdown id="dropdown-1" text="Settings" class="m-md-2">
            <b-dropdown-item v-if="!checkToken" @click="$bvModal.show('login-modal')">Login</b-dropdown-item>
            <b-dropdown-item v-if="checkToken" @click="logout">Logout</b-dropdown-item>
            <b-dropdown-item v-if="checkToken" @click="$bvModal.show('product-modal')">Products</b-dropdown-item>
            <b-dropdown-item v-if="checkToken" @click="$bvModal.show('tank-modal')">Tanks</b-dropdown-item>
            <b-dropdown-item v-if="checkToken" @click="$bvModal.show('tcv-chart')">Upload TCV chart</b-dropdown-item>
          </b-dropdown>
        </div>
      </div>
      <div class="main-body">
        <home v-if="tankData.length > 0" :tank-data="filterTankData" />
        <div v-else>
          <img :src="spinner" alt="Loader" class="image-size-spinner" />
        </div>
      </div>
      <div class="footer">
        <i class="fa fa-bolt fa-lg" style="color: red;"></i> 
        <img :src="footerLogo" alt="Footer logo" class="image-size-footer" />
      </div>

      <div class="login-modal-wrap">
        <b-modal id="login-modal" size="lg" centered hide-footer title="Login">
        <LoginUser />
      </b-modal>

        <b-modal id="product-modal" size="lg" centered hide-footer title="Product">
          <ProductList />
        </b-modal>

        <b-modal id="tank-modal" size="lg" centered hide-footer title="Tank">
          <TankList />
        </b-modal>

        <b-modal id="tcv-chart" ref="tcv-chart" size="md" centered hide-footer title="Upload TCV chart">
          <UploadTcvChart />
        </b-modal>

      </div>

    </div>

    

  </div>
</template>

<script>
import axios from 'axios';
import home from './components/index-home.vue';
import 'font-awesome/css/font-awesome.min.css'; 
import 'font-awesome/fonts/fontawesome-webfont.ttf';
import LoginUser from './components/LoginUser.vue'
import ProductList from './common/ProductList.vue'
import TankList from './common/TankList.vue'
import UploadTcvChart from './common/UploadTcvChart.vue';


export default {
  name: 'App',
  components: {
    home,
    LoginUser,
    ProductList,
    TankList,
    UploadTcvChart,

  },
  data() {
    return {
      selectedProduct: '',
      tankData: [],
      filterItem: '',
      logo: require('./assets/Smarteye-newLogo.png'),
      footerLogo: require('./assets/smart-flow.png'),
      spinner: require('./assets/Smartflow-rotating-logo.gif'),
      products:[
      {
        "Name": "All",
        "Code": "All"      
      },
      ]
    };
  },
  
  created() {
     // Retrieve the data from localStorage
     const user = localStorage.getItem('user');
      // Parse the JSON string back to an object
      const parsedData = JSON.parse(user);
      this.user_type = parsedData.user_type;
    // Call the fetchData method every 90 seconds
    setInterval(this.fetchData, 9000); // 90 seconds = 90,000 milliseconds
    this.fetchProducts()
  },
  methods: {
    hideModal() {
      return this.$bvModal.$refs['tcv-chart'].hide()
      // this.$refs['tcv-chart'].hide();
    },
    fetchData() {
      axios.get('http://localhost:8000/tank-logs-temp/')
        .then(response => {
          this.tankData = response.data;
        })
        .catch(error => {
          console.error('API error:', error);
        });
    },
  //   filterByProduct(productCode) {
  //   this.filterItem = productCode;
  // },
  filterData(filterItem) {
  if (filterItem === '' || filterItem === 'All') {
    return this.tankData;
  }
  const itemFilter = this.tankData.filter(item => item.product === filterItem);
  return itemFilter;
},
    all(){ this.filterItem = ''},
    pms(){ this.filterItem = 'PMS'},
    ago(){ this.filterItem = 'AGO'},
    baseOil(){ this.filterItem = 'BASE OIL'},
    jetA(){ this.filterItem = 'JET A1'},
    logout() {
      localStorage.clear()
      window.location.reload()
    },
    fetchProducts() {
      // Fetch the list of registered products from the server
      axios.get('http://localhost:8000/products/')
      .then(response => {
      this.products.push(...response.data);
    })
    .catch(error => {
      console.error('Error fetching products:', error.response);
    });
    },
    filterByProduct() {
      this.filterItem = this.selectedProduct;
    },
  },

  computed: {
    productOptions() {
      // Generate options for the selection box
      return this.products.map(product => ({ text: product.Name, value: product.Code }));
    },
  filterTankData() {
    const res = this.filterData(this.filterItem);
    return res.sort((a, b) => {
      if (a.product === b.product) {
        return a.tank_id - b.tank_id;
      }
      return a.product.localeCompare(b.product);
    });
  },
  checkToken() {
    return localStorage.getItem('token');
  }
},
};
</script>

<style>
#app {
  display: flex;
  flex-direction: column;
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
  justify-content: space-between;
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


.profile {
  /* margin-left: 5em; */
  width:20%;
}

/* .login-modal-wrap {
  width: 100%;
  height: 100%;
  background-color: rgb(47, 76, 205);
} */

.filter-items {
  display: flex;
  justify-content: center;
  align-items: center;
  width:60%;
  height: 50%;
}

</style>
