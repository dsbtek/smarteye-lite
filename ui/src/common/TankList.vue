<template>
    <div>
      <AddTank :Close="CloseAdd_Tank" :refresh="fetchTanks" v-if="toggleAddTank" />
      <EditTank :editData="editData" :Close="CloseEdit_Tank" :refresh="fetchTanks" v-if="toggleEditTank" />
    
      <hr>
      <div class="table-header">
       
        <div class="table-title">
             <h3>List of Tanks</h3> 
        </div>
        <div v-if="user_type !== 'Engineer'" class="table-add-tank" :disabled="user_type !== 'Engineer'" @click="add_Tank">
             <h1>+</h1>
        </div>

      </div>
      
      <b-table v-if="tanks.length>0" striped hover :items="tanks" :fields="fields" class="t-color">
      <template v-slot:cell(action)="data">
        <b-button v-if="user_type !== 'Engineer'" @click="editTank(data.item)"  variant="outline-secondary">Edit</b-button>
        <b-button v-if="user_type !== 'Engineer'" class="ms-2" @click="deleteTank(data.item)"  variant="outline-danger">Delete</b-button>
      </template>
    </b-table>
    <div v-else class="no-rec">
      <p>No Record Found.</p>
    </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import AddTank from './AddTank.vue';
  import EditTank from './EditTank.vue';

  
  export default {
    components: {
    AddTank,
    EditTank
  },
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
        toggleAddTank: false,
        toggleEditTank: false,
        tanks: [],
        products: [],
        editData: '',
        user_type:'',
        fields: [
        // { key: 'Tank_id', label: 'Tank ID' },
        { key: 'Name', label: 'Tank Name' },
        { key: 'Product_id.Code', label: 'Product' },
        { key: 'Created_at', label: 'Date Created' },
        // Add an action column
        { key: 'action', label: 'Action' },
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
      this.fetchTanks();
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
        add_Tank(){
            return this.toggleAddTank = !this.toggleAddTank
        },
        edit_Tank(){
            if(this.toggleEditTank) { '' } else {this.toggleEditTank = true}
            
        },
        CloseAdd_Tank(){
            this.toggleAddTank = false;
        },
        CloseEdit_Tank(){
            this.toggleEditTank = false;
            
        },
        formatCreatedAt(data) {
          return data.forEach(tank => {
              tank.Created_at = new Date(tank?.Created_at).toLocaleString('en-US', {timeZone: 'UTC'});
              
          });
      },
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
            this.formatCreatedAt(this.tanks)
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
      this.edit_Tank()
      this.editData = tank
    },
    deleteTank(tank) {
    // Implement your delete logic here
    console.log('Delete tank:', tank);
    axios.delete(`http://localhost:8000/tanks/${tank.Tank_id}`)
    .then(response => {
    console.log('Deleted tank:', response.data);
    this.alertSuccess("Tank deleted successfully")
    this.fetchTanks();
    })
    .catch(error => {
    console.error('Error deleting tanks:', error.response);
    this.alertError("Error deleting tank")
    });
    },
    },
  };
  </script>
  <style scoped>
  .table-header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    height: 40px;
    width: 100%;
    background-color: rgb(85, 85, 86);
    color: aliceblue;
    margin: 5px;
  }

  .table-title {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    height: 40px;
    width: 90%;
    background-color: rgb(85, 85, 86);
    color: aliceblue;
    margin: 5px;
  }
  .t-color {
    color: rgb(85, 85, 86);
  }
  .table-add-tank {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    height: 40px;
    width: 10%;
    background-color: rgb(85, 85, 86);
    color: aliceblue;
    margin: 5px;
  }
  .table-add-tank:hover {
    cursor: pointer;
    color: rgb(199, 200, 201);
  }
  .no-rec {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
  </style>