<template>
    <div>
    <b-form @submit.prevent="createTank">
        <b-row>
           

        <b-col md="6">
            <b-form-group label="Name:" label-for="tankName">
            <b-form-input id="tankName" v-model="tankData.Name" placeholder="Enter Tank Name" :disabled="user_type !== 'Engineer'" required></b-form-input>
            </b-form-group>
        </b-col>

        <b-col md="6">
            <b-form-group label="Product:" label-for="tankProduct">
            <select v-model="selectedProductId"  class="custom-select" placeholder="Select Product"  :disabled="user_type !== 'Engineer'">
                <option disabled value="">Select Product</option>
                <option v-for="product in products" :key="product.id" :value="product">{{ product.Name }}</option>
            </select>
            </b-form-group>
        </b-col>

    <!-- <b-col md="6">
        <b-form-group label="Control mode:" label-for="Control_mode" >
          <b-form-input id="Control_mode" v-model="tankData.Control_mode" placeholder="Enter Control Mode" :disabled="user_type !== 'Engineer'" required></b-form-input>
        </b-form-group>
    </b-col> -->

    <!-- <b-col md="6">
        <b-form-group label="Tank Controller:" label-for="Tank_controller">
          <b-form-input id="Tank_controller" v-model="tankData.Tank_controller" placeholder="Enter Tank Controller" :disabled="user_type !== 'Engineer'" required></b-form-input>
        </b-form-group>
    </b-col> -->

    <b-col md="6">
        <b-form-group label="Controller Polling Address:" label-for="Controller_polling_address">
          <b-form-input id="Controller_polling_address" v-model="tankData.Controller_polling_address"  placeholder="Enter Tank Polling Address" :disabled="user_type !== 'Engineer'" required></b-form-input>
        </b-form-group>
    </b-col>

    <b-col md="6">
            <b-form-group label="Tank Index:" label-for="Tank_index">
            <select v-model="tankData.Tank_index"  class="custom-select" placeholder="Select Tank Index"  :disabled="user_type !== 'Engineer'">
                <option disabled value="">Select Tank Index</option>
                <option>1</option>
                <option>2</option>
                <option>3</option>
                <option>4</option>

            </select>
            </b-form-group>
        </b-col>

    <!-- <b-col md="6">
        <b-form-group label="Tank Index:" label-for="Tank_index">
          <b-form-input id="Tank_index" v-model="tankData.Tank_index" placeholder="Enter Tank Index" :disabled="user_type !== 'Engineer'" required></b-form-input>
        </b-form-group>
    </b-col> -->

    <b-col md="6">
        <b-form-group label="Capacity:" label-for="Capacity">
          <b-form-input id="Capacity" v-model="tankData.Capacity" placeholder="Enter Tank Capacity" :disabled="user_type !== 'Engineer'" required></b-form-input>
        </b-form-group>
    </b-col>

    <b-col md="6">
        <b-form-group label="Tank height:" label-for="Tank_height">
          <b-form-input id="Tank_height" v-model="tankData.Tank_height" :disable="user_type !== 'Engineer'" required></b-form-input>
        </b-form-group>
    </b-col>

    </b-row>
        <br />
        <b-button type="submit" variant="outline-secondary">Create</b-button>
        <b-button class="ms-3" @click="Close" variant="outline-success">Cancel</b-button>
    
    </b-form>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    props: ['Close', 'refresh'],

  data() {
    return {
        tankData: {
            Name: '',
            product: '',
            // Control_mode: '',
            // Tank_controller: '',
            Controller_polling_address: '',
            Tank_index: '',
            Capacity: '',
            // UOM: '',
            // Shape: '',
            // LL_Level: '',
            // L_Level: '',
            // HH_Level: '',
            // H_Level: '',
            // Reorder: '',
            // Leak: '',
            Status: true,
            // Offset: '',
            Po4: '',
            Display_unit: '',
            // Density: '',
            Tank_height: '',
            // Anomaly_period: '',
            // Anomaly_volume: '',
            // Tank_Note: '',
        },
        tanks: [],
        products: [],
        selectedProductId: null,
        selectedShape: null,
        selectedUOM: null,
        selectedDUOM: null,
        user_type: '',
        measures: [
                    {
                    "name": "Liters",
                    "abbreviation": "L",
                    "id": 1
                },
                {
                    "name": "Tonnes",
                    "abbreviation": "T",
                    "id": 2
                },
                {
                    "name": "Kilogrammes",
                    "abbreviation": "kg",
                    "id": 3
                },
                {
                    "name": "Metres",
                    "abbreviation": "m",
                    "id": 4
                },
                {
                    "name": "Millimeters",
                    "abbreviation": "mm",
                    "id": 5
                },
                {
                    "name": "Centimeters",
                    "abbreviation": "cm",
                    "id": 6
                },
                {
                    "name": "Cubic Meters",
                    "abbreviation": "m³",
                    "id": 7
                },
                {
                    "name": "Gallons",
                    "abbreviation": "gal",
                    "id": 8
                },
                ],
        shapes: [
                {
                    "name": "Lying Cylindrical",
                    "id": 1
                },
                {
                    "name": "Standing Cylindrical",
                    "id": 2
                },
                {
                    "name": "Lying Rectangular",
                    "id": 3
                },
                {
                    "name": "Standing Rectangular",
                    "id": 4
                },
                {
                    "name": "Standing Round View",
                    "id": 5
                },
                ],

    };
  },
  created() {
      this.tankData.Created_at = new Date().toISOString();
      // Retrieve the data from localStorage
      const user = localStorage.getItem('user');
      // Parse the JSON string back to an object
      const parsedData = JSON.parse(user);
      this.user_type = parsedData.user_type;
    // Fetch the list of tanks when the component is created
    this.fetchProducts();
  },
  methods: {
    alertError(msg) {
        this.$notify.error({
          title: 'Login Error',
          message: msg
        });
      },
    alertSuccess(msg) {
        this.$notify({
          title: 'Success',
          message: msg,
          type: 'success'
        });
      },
    closeAddTank() {
        this.Close();
    },
    createTank() {
      // Your tank creation logic

      this.tankData['product'] = this.selectedProductId.id
      this.tankData['Density'] = this.selectedProductId.density

      axios.post('http://localhost:8000/tanks/', this.tankData)
        .then(response => {
          console.log(response)
          this.alertSuccess('Tank created successfully')
          this.refresh();
          this.Close()
        })
        .catch(error => {
          this.alertError('Error creating tank:', error.response);
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
  editTank(tank) {
    // Implement your edit logic here
    console.log('Edit tank:', tank);
  },
  deleteTank(tank) {
    // Implement your delete logic here
    console.log('Delete tank:', tank);
  },
  },
};
</script>
<style scoped>
.custom-select {
  width: 100%;
  padding: 0.375rem 1.75rem 0.375rem 0.75rem;
  line-height: 1.5;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
  background-color: #fff;
}
</style>