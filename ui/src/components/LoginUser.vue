<template>
  <b-container class="" fluid>
    <b-row align-h="center">
      <b-col md="12">
        <b-card>
          <b-form @submit.prevent="login">
            <b-form-group
              id="username-group"
              label="Username:"
              label-for="username"
              description="Enter your username"
            >
              <b-form-input
                id="username"
                v-model="username"
                required
                placeholder="Enter your username"
              ></b-form-input>
            </b-form-group>

            <b-form-group
              id="password-group"
              label="Password:"
              label-for="password"
              description="Enter your password"
            >
              <b-form-input
                id="password"
                type="password"
                v-model="password"
                required
                placeholder="Enter your password"
              ></b-form-input>
            </b-form-group>
            <br />
            <b-button type="submit" variant="outline-secondary">Login</b-button>
          </b-form>
          <b-card-body style="width: 100%;">
          </b-card-body>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import axios from "axios";
export default {
  components: {
    
  },
  data() {
    return {
      username: "",
      password: "",
    };
  },
  computed: {
    nameState() {
      return this.username.length >= 2;
    },
    nameInvalidFeedback() {
      if (this.username.length > 0) {
        return "Enter at least 4 characters.";
      }
      return "Please enter something.";
    },
    passwordState() {
      return this.password.length >= 4;
    },
    passwordInvalidFeedback() {
      if (this.password.length > 0) {
        return "Enter at least 8 characters for the password.";
      }
      return "Please enter a password.";
    },
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
    
    
    login() {
      if (this.nameState && this.passwordState) {
        const credentials = {
          username: this.username,
          password: this.password,
        };

         axios.post('http://localhost:8000/login', credentials)
          .then(response => {
            this.alertSuccess("Login Success")
            localStorage.setItem('token', response?.data?.access_token);
            localStorage.setItem('user', JSON.stringify(response?.data?.user));
            this.$emit('$bvModal.hide("login-modal")');
            window.location.reload()
          }) 
          .catch(error => {
            this.alertError(error?.response?.data?.detail)
          });
          
      } else {
            this.alertError("You most provide your credentials before login")
      }
    },
  },
};
</script>

<style scoped>
  
</style>
