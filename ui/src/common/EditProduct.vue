<template>
    <b-form @submit.prevent="updateProduct">
     <b-form-group label="Name:" label-for="name">
       <b-form-input id="name" v-model="productData.Name" :disabled="user_type !== 'Engineer'" required></b-form-input>
     </b-form-group>

     <b-form-group label="Code:" label-for="code">
       <b-form-input id="code" v-model="productData.Code" :disabled="user_type !== 'Engineer'" required></b-form-input>
     </b-form-group>

     <b-form-group label="Density:" label-for="density">
       <b-form-input id="density" v-model="productData.density" required></b-form-input>
     </b-form-group>
     <br />
    <b-button type="submit" variant="outline-secondary">Update</b-button>
    <b-button class="ms-3" @click="Close" variant="outline-success">Cancel</b-button>

   </b-form>
</template>


<script>
import axios from 'axios';
// import Multiselect from 'vue-multiselect';
// import vSelect from "vue-select";


export default {
    props: ['editData', 'Close', 'refresh'],
    data() {
    return {
        productData: {
        Name: '',
        Code: '',
        density: '',
        Updated_at: '',
        },
        products: [],
        user_type:''
    };
 },
 created() {
    this.productData.Updated_at = new Date().toISOString();
    // Retrieve the data from localStorage
    const user = localStorage.getItem('user');
    // Parse the JSON string back to an object
    const parsedData = JSON.parse(user);
    this.user_type = parsedData.user_type;
    // Fetch the list of tanks when the component is created
    this.fetchProducts();
    this.productData.Name=this.editData?.Name,
    this.productData.Code= this.editData?.Code,
    this.productData.density= this.editData?.density
 },
 methods: {
   closeAddTank() {
       this.CloseAdd_Tank();
   },
   updateProduct() {

      axios.put(`http://localhost:8000/products/${this.editData.id}`, this.productData)
        .then(response => {
            console.log('Product updated successfully:', response);
            this.refresh();
            this.Close();
        })
        .catch(error => {
          console.error('Error updating product:', error.response);
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