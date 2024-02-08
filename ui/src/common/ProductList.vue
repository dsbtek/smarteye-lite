<template>
  <div>
      <EditProduct :editData="editData" :Close="CloseEdit_product" :refresh="fetchProducts" v-if="toggleEditProduct" />
      <AddProduct :Close="CloseAdd_product" :refresh="fetchProducts" v-if="toggleAddProduct" />
    <hr>
    <div>
      <div class="table-header">
       <div class="table-title">
            <h3>List of Products</h3> 
       </div>
       <div class="table-add-tank" :disabled="user_type !== 'Engineer'" @click="add_product">
            <h1>+</h1>
       </div>

     </div>
      <b-table v-if="products.length>0" striped hover :items="products" :fields="fields" class="t-color">
      <template v-slot:cell(action)="data">
        <b-button @click="editProduct(data.item)"  variant="outline-secondary">Edit</b-button>
        <b-button v-if="user_type === 'Engineer'" class="ms-2" @click="deleteProduct(data.item)"  variant="outline-danger">Delete</b-button>
      </template>
    </b-table>
    <div v-else class="no-rec">
      <p>No Record Found.</p>
    </div>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios';
import AddProduct from './AddProduct.vue';
import EditProduct from './EditProduct.vue';

export default {
  components: {
    AddProduct,
    EditProduct
  },
  data() {
    return {
      productData: {
        Name: '',
        Code: '',
        density: '',
        Created_at: '',
      },
      user_type:'',
      editData:'',
      products: [],
      toggleAddProduct: false,
      toggleEditProduct: false,
      fields: [
        { key: 'Name', label: 'Product Name' },
        { key: 'Code', label: 'Code' },
        { key: 'density', label: 'Density' },
        { key: 'Created_at', label: 'Date Created' },
        // Add an action column
        { key: 'action', label: 'Action' },
      ],
      coptions: {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
    }
    };
  },
  created() {
    this.productData.Created_at = new Date().toISOString();
     // Retrieve the data from localStorage
     const user = localStorage.getItem('user');
    // Parse the JSON string back to an object
    const parsedData = JSON.parse(user);
    this.user_type = parsedData.user_type;
    // Fetch the list of registered products when the component is created
    this.fetchProducts();
  },
  methods: {
    formattedDateTime(date_str) { return date_str.toLocaleString('en-US', this.options).replace(/(\d+)\/(\d+)\/(\d+),?/, '$3-$1-$2')},
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
      add_product(){
          return this.toggleAddProduct = !this.toggleAddProduct
      },
      edit_product(){
          if(this.toggleEditProduct) { '' } else {this.toggleEditProduct = true}
          
      },
      CloseAdd_product(){
          this.toggleAddProduct = false;
      },
      CloseEdit_product(){
          this.toggleEditProduct = false;
          
      },
      formatCreatedAt(data) {
          return data.forEach(tank => {
              tank.Created_at = new Date(tank?.Created_at).toLocaleString('en-US', {timeZone: 'UTC'});
              
          });
      },
      fetchProducts() {
        // Fetch the list of registered products from the server
        axios.get('http://localhost:8000/products/')
          .then(response => {
            this.products = response.data;
            this.formatCreatedAt(this.products)
          })
          .catch(error => {
            console.error('Error fetching products:', error.response);
          });
      },
      editProduct(product) {
      // Implement your edit logic here
      this.edit_product()
      this.editData = product
    },
    deleteProduct(product) {
      // Implement your delete logic here
      console.log('Delete tank:', product);
      axios.delete(`http://localhost:8000/products/${product.id}`)
          .then(response => {
            console.log('Deleted product:', response.data);
            this.alertSuccess("Product deleted successfully")
            this.fetchProducts();
          })
          .catch(error => {
            console.error('Error deleting tanks:', error.response);
            this.alertError("Error deleting product")
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
  .t-color {
    color: rgb(85, 85, 86);
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