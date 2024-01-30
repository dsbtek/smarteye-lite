<template>
    <div>
      <b-form @submit.prevent="createTank">
        <b-row>
            <b-col md="6">
                <b-form-group label="Name:" label-for="tankName">
                <b-form-input id="tankName" v-model="tankData.Name" required></b-form-input>
                </b-form-group>
            </b-col>

            <b-col md="6">
                <b-form-group label="Product:" label-for="tankProduct">
                <!-- You may want to replace this with a dropdown or autocomplete based on your product data -->
                <b-form-input id="tankProduct" v-model="tankData.product" required></b-form-input>
                </b-form-group>
            </b-col>
<b-col md="6">
        <b-form-group label="Control mode:" label-for="Control_mode">
          <b-form-input id="Control_mode" v-model="tankData.Control_mode" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="Tank Controller:" label-for="Tank_controller">
          <b-form-input id="Tank_controller" v-model="tankData.Tank_controller" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="Controller Polling Address:" label-for="Controller_polling_address">
          <b-form-input id="Controller_polling_address" v-model="tankData.Controller_polling_address" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="Tank Index:" label-for="Tank_index">
          <b-form-input id="Tank_index" v-model="tankData.Tank_index" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">

        <b-form-group label="Capacity:" label-for="Capacity">
          <b-form-input id="Capacity" v-model="tankData.Capacity" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="UOM:" label-for="UOM">
          <b-form-input id="UOM" v-model="tankData.UOM" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="Shape:" label-for="Shape">
          <b-form-input id="Shape" v-model="tankData.Shape" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="LL Level:" label-for="LL_Level">
          <b-form-input id="LL_Level" v-model="tankData.LL_Level" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="L Level:" label-for="L_Level">
          <b-form-input id="L_Level" v-model="tankData.L_Level" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="HH Level:" label-for="HH_Level">
          <b-form-input id="HH_Level" v-model="tankData.HH_Level" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="H Level:" label-for="H_Level">
          <b-form-input id="H_Level" v-model="tankData.H_Level" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="Reorder:" label-for="Reorder">
          <b-form-input id="Reorder" v-model="tankData.Reorder" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="Leak:" label-for="Leak">
          <b-form-input id="Leak" v-model="tankData.Leak" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="Offset:" label-for="Offset">
          <b-form-input id="Offset" v-model="tankData.Offset" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="Po4:" label-for="Po4">
          <b-form-input id="Po4" v-model="tankData.Po4" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="Display unit:" label-for="Display_unit">
          <b-form-input id="Display_unit" v-model="tankData.Display_unit" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="Density:" label-for="Density">
          <b-form-input id="Density" v-model="tankData.Density" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="Tank height:" label-for="Tank_height">
          <b-form-input id="Tank_height" v-model="tankData.Tank_height" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="Anomaly period:" label-for="Anomaly_period">
          <b-form-input id="Anomaly_period" v-model="tankData.Anomaly_period" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="6">
        <b-form-group label="Anomaly volume:" label-for="Anomaly_volume">
          <b-form-input id="Anomaly_volume" v-model="tankData.Anomaly_volume" required></b-form-input>
        </b-form-group>
    </b-col>
    <b-col md="12">
        <b-form-group label="Tank Note:" label-for="Tank_Note">
          <b-form-input id="Tank_Note" v-model="tankData.Tank_Note" required></b-form-input>
        </b-form-group>

    </b-col>
</b-row>
        <br />
        <b-button type="submit" variant="secondary">Create</b-button>
        
    
      </b-form>
    
      <hr>
      <!-- List of Tanks -->
      <h3>List of Tanks</h3>
      <b-table striped hover :items="tanks" :fields="fields"></b-table>

    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        tankData: {
            id: '',
            Name: '',
            product: '',
            Control_mode: '',
            Tank_controller: '',
            Controller_polling_address: '',
            Tank_index: '',
            Capacity: '',
            UOM: '',
            Shape: '',
            LL_Level: '',
            L_Level: '',
            HH_Level: '',
            H_Level: '',
            Reorder: '',
            Leak: '',
            Status: false,
            Offset: '',
            Po4: '',
            Display_unit: '',
            Density: '',
            Tank_height: '',
            Anomaly_period: '',
            Anomaly_volume: '',
            Tank_Note: '',
        },
        tanks: [],
        products: [],
        fields: ['Name', 'Capacity', 'Display_unit', 'Created_at'],
      };
    },
    created() {
        this.tankData.Created_at = new Date().toISOString();

      // Fetch the list of tanks when the component is created
      this.fetchTanks();
      this.fetchProducts();
    },
    methods: {
      createTank() {
        // Your tank creation logic
        axios.post('http://localhost:8000/tanks/', this.tankData)
          .then(response => {
            console.log('Tank created successfully:', response);
            // Refresh the list of tanks after creation
            this.fetchTanks();
          })
          .catch(error => {
            console.error('Error creating tank:', error.response);
          });
      },
      fetchTanks() {
        // Fetch the list of tanks from the server
        axios.get('http://localhost:8000/tanks/')
          .then(response => {
            this.tanks = response.data;
          })
          .catch(error => {
            console.error('Error fetching tanks:', error.response);
          });
      },
      fetchProducts() {
      // Fetch the list of registered products from the server
      axios.get('http://localhost:8000/products/')
        .then(response => {
          this.products = response.data;
        })
        .catch(error => {
          console.error('Error fetching products:', error.response);
        });
    },
    },
  };
  </script>
  