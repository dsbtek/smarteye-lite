<template>
    <b-form-group
      :id="fieldId"
      description=""
      :label="label"
      :label-for="inputId"
      valid-feedback="Thank you!"
      :invalid-feedback="invalidFeedback"
      :state="state"
    >
      <b-form-input :id="inputId" v-model="value" :state="state" trim></b-form-input>
    </b-form-group>
  </template>
  
  <script>
  export default {
    props: {
      fieldId: String,
      label: String,
      inputId: String,
      value: String,
      invalidFeedback: String,
      state: Boolean,
    },
  };
  </script>