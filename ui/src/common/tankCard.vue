<template>
  <div class="fuel-card">
    <div class="circle-container">
      <TankLevelImage
            :volume="tankData.vol"
            :capacity="tankData.capacity"
            :percent="fillPercentage"
          />
    </div>
    <div class="fuel-info">
      <div class="fuel-info-item">
        <p>Tank Name: </p>
        <p>Tank {{ tankData.tank_id }}</p>
      </div>

      <div class="fuel-info-item">
        <p>Capacity: </p>
        <p>{{ tankData.capacity }}L</p>
      </div>

      <div class="fuel-info-item">
        <p>Volume: </p>
        <p>{{ tankData.vol }}L</p>
      </div>

      <div class ="fuel-info-item">
        <p>TCV: </p>
        <p>{{ tankData.tcv }}L</p>
      </div>

      <div class="fuel-info-item">
        <p>Height: </p>
        <p>{{ tankData.height }}L</p>
      </div>

      <div class="fuel-info-item">
        <p>Av. Temp: </p>
        <p>{{ tankData.avg_temp }}&#8451;</p>
      </div>

      <div class="fuel-info-item">
        <p>Temp 1: </p>
        <p>{{ tankData.temp_1 }}&#8451;</p>
      </div>

      <div class="fuel-info-item">
        <p>Temp 2: </p>
        <p>{{ tankData.temp_2 }}&#8451;</p>
      </div>

      <div class="fuel-info-item">
        <p>Temp 3: </p>
        <p>{{ tankData.temp_3 }}&#8451;</p>
      </div>

      <div class="fuel-info-item">
        <p>Temp 4: </p>
        <p>{{ tankData.temp_4 }}&#8451;</p>
      </div>

      <div class="fuel-info-item fuel-info-item-last">
        <p>Temp 5: </p>
        <p>{{ tankData.temp_5 }}&#8451;</p>
      </div>
    </div>
  </div>
</template>

<script>
import TankLevelImage from "./tank-level-image";

export default {
  props: {
    tankData: Object,
  },
  components: {
    TankLevelImage
  },
  data() {
    return {
      liquidColor: '#c5b550',
    };
  },
  computed: {
  fillPercentage() {
    if (this.tankData && this.tankData.vol !== undefined && this.tankData.capacity !== undefined) {
      return ((this.tankData.vol / this.tankData.capacity) * 100).toFixed();
    }
    return 0;
  },
},
};
</script>

<style scoped>
.fuel-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  border: 1px solid #ccc;
  padding-top: 20px;
  border-radius: 10px;
  width: 300px;
  height: 475px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin-bottom: 3%;
}

.circle-container {
  position: relative;
}

.circle {
  position: relative;
  width: 150px;
  height: 150px;
}

.percentage {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 16px;
  font-weight: bold;
  animation: ripple 2s infinite;
}

.fuel-info {
  width: 100%;
  border-radius: 10px;
}

h2 {
  font-size: 20px;
  margin: 0;
  padding-bottom: 5px;
}

p {
  margin: 0;
}

.fuel-info-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 96%;
  height: 1em;
  border: #ccc 1px solid;
  padding: 5px;
}

.fuel-info-item-last {
  border-radius: 0px 0px 10px 10px;
}

@keyframes ripple {
  0% {
    transform: scaleY(1);
  }
  50% {
    transform: scaleY(0.8);
  }
  100% {
    transform: scaleY(1);
  }
}

 /* Define the fill animation */
 @keyframes fillAnimation {
    0% {
      y: 100%;
      height: 0;
    }
    100% {
      y: 0;
      height: 100%;
    }
  }

  .liquid-rect {
    animation: fillAnimation 2s ease;
  }
</style>
