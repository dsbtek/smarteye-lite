<template>
  
    <div class="card-container">
      <!-- Use v-for to render tank-card components for each item in tankData -->
      <tank-card v-for="(item, index) in tankData" :key="index" :tankData="item" />
      <!-- <tank-card /> -->
    </div>

</template>

<script>
import TankCard from '../common/tankCard.vue';

export default {
  name: 'DashboardPage',
  props: {
    tankData: Array,
  },
  data() {
    return {
      rs: [],
    };
  },
  components: {
    TankCard,
  },
};
</script>
<style>


.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px; 
  align-items: center;
  justify-content: center;
  overflow-y: scroll;
  height: 80%;
  width: 100%;
  padding-top:5%;
  padding-bottom:5%;
}

</style>