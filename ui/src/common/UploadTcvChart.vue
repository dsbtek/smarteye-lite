<template>
    <b-form @submit.prevent="uploadFile">
      <div v-if="user_type !== 'Engineer'" class="wrap-upload">
        <el-upload
          class="upload-demo"
          drag
          ref="upload"
          size="sm"
          action="http://localhost:8000/upload" 
          :on-preview="handlePreview"
          :on-remove="handleRemove"
          :on-success="handleOnSuccess"
          :on-error="handleOnError"
          :auto-upload="false"
          :limit="1"
          :file-list="fileList"
          :before-upload="beforeUpload"
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">Drop TCV chart file here or <em>click to upload</em></div>
        </el-upload>
      <br />
      <el-button style="" size="large" type="success" @click="uploadFile">Upload Chart</el-button>
    </div>

    </b-form>
  </template>
  
  <script>
//   import axios from 'axios';
  
  export default {
    data() {
      return {
        fileList: [],
        fileData: {
          Name: '',
          Created_at: '',
        },
        products: [],
      };
    },
    created() {
        this.tankData.Created_at = new Date().toISOString();
       // Retrieve the data from localStorage
      const user = localStorage.getItem('user');
      // Parse the JSON string back to an object
      const parsedData = JSON.parse(user);
      this.user_type = parsedData.user_type;
      
    },
    methods: {
        closeModal() {
      this.Close(); 
    },
      uploadFile() {
        this.$refs.upload.submit();
      },
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePreview(file) {
        console.log(file);
      },
      handleOnSuccess(response) {
        this.alertSuccess(`${response.filename} uploaded successfully`)
        window.location.reload()
      },
      handleOnError(err) {
        console.log(err);
        this.alertError(`Error uploading the chart`)
      },
      beforeUpload(file) {
      const isCSV = file.name.toLowerCase().endsWith('.csv');
      if (!isCSV) {
        this.alertError('Only CSV files are allowed!');
      }
      return isCSV;
    },
      alertError(msg) {
        this.$notify.error({
          title: 'An Error Occured',
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
    },
  };
  </script>
  
  <!-- Add your styles here if needed -->
  <style scoped>
 .wrap-upload {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
 }
  </style>
  