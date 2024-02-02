<!-- ToastComponent.vue -->
<template>
  <div v-if="show" class="custom-toast" :class="{'success': variant === 'success', 'error': variant === 'error'}">
    <p>{{ message }}</p>
    <button @click="hideToast">Close</button>
  </div>
</template>

<script>
export default {
  props: {
    show: Boolean,
    message: String,
    variant: String,
  },
  methods: {
    hideToast() {
      this.$emit('close');
    },
  },
  watch: {
    show(newVal) {
      if (newVal) {
        // Automatically hide the toast after 3000 milliseconds (3 seconds)
        setTimeout(() => {
          this.hideToast();
        }, 3000);
      }
    },
  },
};
</script>

<style scoped>
.custom-toast {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px;
  background-color: #333;
  color: #fff;
  border-radius: 5px;
}

.success {
  background-color: #5cb85c;
}

.error {
  background-color: #d9534f;
}
</style>
