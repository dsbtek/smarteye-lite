<template>
  <div class="container">
    <div class="card-container">
      <tank-card
        v-for="(item, index) in tankData"
        :key="index"
        :tankData="item"
        @click.native="showModal(item)"
      />
    </div>
    <div :class="computeOverlay" @click="closeModalOnOverlay">
      <TankCardModal :modalContent="modalContent" v-if="modalContent" @closeModal="closeModal" />
    </div>
  </div>
</template>

<script>
import TankCard from '../common/tankCard.vue';
import TankCardModal from '../common/ChakraTankCardModal.vue';

export default {
  name: 'DashboardPage',
  props: {
    tankData: Array,
  },
  data() {
    return {
      modalContent: null,
    };
  },
  methods: {
    showModal(item) {
      this.modalContent = item;
    },
    closeModal() {
      this.modalContent = null;
    },
    closeModalOnOverlay(event) {
      if (event.target.classList.contains('modal-bg')) {
        this.closeModal();
      }
    },
  },
  components: {
    TankCard,
    TankCardModal,
  },
  computed: {
  computeOverlay() {
    if (this.modalContent) {
      return 'modal-bg';
    } else {
      return '';
    }
  },
},
};
</script>

<style>
/* Add any additional styles if needed */
.modal-bg {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(98, 98, 98, 0.5); /* Semi-transparent overlay */
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 500; /* Ensure the overlay is above other content */
}
.container {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  overflow-y: scroll;
  height: 100vh;
  width: 100%;
}

.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  align-items: center;
  justify-content: center;
  overflow-y: scroll;
  height: 80%;
  width: 100%;
  padding-top: 5%;
  padding-bottom: 5%;
}
</style>