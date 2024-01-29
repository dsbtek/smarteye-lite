<template>
    <div>
        <b-form-group
            id="fieldset-1"
            description=""
            label="Enter your user name"
            label-for="input-1"
            valid-feedback="Thank you!"
            :invalid-feedback="invalidFeedback"
            :state="state"
        >
        <b-form-input id="input-1" v-model="name" :state="state" trim></b-form-input>
    </b-form-group>
    <b-form-group
        id="fieldset-1"
        description=""
        label="Enter your password"
        label-for="input-2"
        valid-feedback="Thank you!"
        :invalid-feedback="invalidFeedback"
        :state="state"
      >
        <b-form-input id="input-2" v-model="name" :state="state" trim></b-form-input>
    </b-form-group>
  
    </div>
</template>
  
  <script>
    export default {
      computed: {
        state() {
          return this.name.length >= 4
        },
        invalidFeedback() {
          if (this.name.length > 0) {
            return 'Enter at least 4 characters.'
          }
          return 'Please enter something.'
        }
      },
      data() {
        return {
          name: ''
        }
      }
    }
  </script>