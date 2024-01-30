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

            <b-button type="submit" variant="primary">Login</b-button>
          </b-form>
          <!-- Apply style to make the modal body fill the width -->
          <b-card-body style="width: 100%;">
            <!-- Your modal body content goes here -->
          </b-card-body>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import axios from "axios";
export default {
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
    login() {
      if (this.nameState && this.passwordState) {
        const credentials = {
          username: this.username,
          password: this.password,
        };
        console.log(credentials);

        // Replace 'YOUR_LOGIN_ENDPOINT' with the actual login endpoint
        axios.post('http://localhost:8000/login', credentials)
          .then(response => {
            localStorage.setItem('token', response.data.access_token);
            console.log(response.data);
            this.$emit('$bvModal.hide("login-modal")');
            window.location.reload()
          })
          .catch(error => {
            // Handle login error
            console.error(error.response.data);
          });
      } else {
        console.error('Invalid inputs. Please check your username and password.');
      }
    },
  },
};
</script>

<style scoped>
  
</style>
