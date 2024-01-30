<template>
  <div>
    <h2>Create Product</h2>
    <!-- Your product creation form -->
    <b-form @submit.prevent="createProduct">
      <b-form-group label="Name:" label-for="name">
        <b-form-input id="name" v-model="productData.Name" required></b-form-input>
      </b-form-group>

      <b-form-group label="Code:" label-for="code">
        <b-form-input id="code" v-model="productData.Code" required></b-form-input>
      </b-form-group>

      <b-form-group label="Density:" label-for="density">
        <b-form-input id="density" v-model="productData.density" required></b-form-input>
      </b-form-group>
      <br />
      <b-button type="submit" variant="secondary">Create</b-button>
    </b-form>

    <hr>

    <h2>List of Products</h2>
    <div v-if="products.length > 0">
      <b-table striped hover :items="products" :fields="fields"></b-table>
    </div>
    <div v-else>
      <p>No products registered yet.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      productData: {
        Name: '',
        Code: '',
        density: '',
        Created_at: '',
      },
      products: [],
      fields: ['Name', 'Code', 'density', 'Created_at'],
    };
  },
  created() {
    this.productData.Created_at = new Date().toISOString();
    // Fetch the list of registered products when the component is created
    this.fetchProducts();
  },
  methods: {
    createProduct() {
      // Your product creation logic
      axios.post('http://localhost:8000/products/', this.productData)
        .then(response => {
          console.log('Product created successfully:', response);
          // Refresh the list of products after creation
          this.fetchProducts();
        })
        .catch(error => {
          console.error('Error creating product:', error.response);
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
