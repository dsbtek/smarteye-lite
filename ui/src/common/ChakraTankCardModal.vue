<template>
  <div class="tank-modal" @click="handleClick">
    <div class="fuel-card">
      <div class="circle-container">
        <TankLevelImage
              :volume="modalContent?.vol"
              :capacity="modalContent?.capacity"
              :percent="fillPercentage"
            />
      </div>
    </div>

    <div class="tank-modal-items">
      <div class="fuel-info">
        <div class="fuel-info-item fuel-info-item-first">
          <p>Tank Name: </p>
          <p>Tank {{ modalContent?.tank_id }}</p>
        </div>

        <div class="fuel-info-item">
          <p>Capacity: </p>
          <p>{{ modalContent?.capacity }} Ltrs</p>
        </div>

        <div class="fuel-info-item">
          <p>Volume: </p>
          <p>{{ formattedNumber(modalContent?.vol) }} Ltrs</p>
        </div>

        <div class ="fuel-info-item">
          <p>TCV: </p>
          <p>{{ formattedNumber(modalContent?.tcv) }} Ltrs</p>
        </div>

        <div class="fuel-info-item">
          <p>Height: </p>
          <p>{{ formattedNumber(modalContent?.height) }} mm</p>
        </div>

        <div class="fuel-info-item">
          <p>Product: </p>
          <p>{{ modalContent?.product }}</p>
        </div>

        <div class="fuel-info-item">
          <p>Av. Temp: </p>
          <p>{{ modalContent?.avg_temp }} &#8451;</p>
        </div>

        <div class="fuel-info-item">
          <p>Temp 1: </p>
          <p>{{ modalContent?.temp_1 }} &#8451;</p>
        </div>

        <div class="fuel-info-item">
          <p>Temp 2: </p>
          <p>{{ modalContent.temp_2 }} &#8451;</p>
        </div>

        <div class="fuel-info-item">
          <p>Temp 3: </p>
          <p>{{ modalContent?.temp_3 }} &#8451;</p>
        </div>

        <div class="fuel-info-item">
          <p>Temp 4: </p>
          <p>{{ modalContent?.temp_4 }} &#8451;</p>
        </div>

        <div class="fuel-info-item">
          <p>Temp 5: </p>
          <p>{{ modalContent?.temp_5 }} &#8451;</p>
        </div>

        <div class="fuel-info-item">
          <p>Last Updated Time: </p>
          <p>{{ modalContent?.date_time }}</p>
        </div>

        <div class="fuel-info-item fuel-info-item-last">
          <p>Status: </p>
          <p :class="getHourDifference(modalContent?.date_time)">{{ getHourDifference(modalContent?.date_time) }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TankLevelImage from "./tank-level-image";

export default {
  props: {
    modalContent: Object,
  },
  components: {
    TankLevelImage
  },
  methods: {
    handleClick() {
      this.$emit('closeModal');
    },
  getHourDifference(dateTime2) {
    const dateTime1 = new Date();
    const timestamp1 = new Date(dateTime1).getTime();
    const timestamp2 = new Date(dateTime2).getTime();
    // Calculate the time difference in milliseconds
    const timeDifference = Math.abs(timestamp2 - timestamp1);
    // Convert the time difference to hours
    const hoursDifference = timeDifference / (1000 * 60 * 60);
      if (hoursDifference > 2)  {return "Offline"} else {return "Online"}
  },
  formattedNumber(num){ return num.toLocaleString('en-US', {
    minimumFractionDigits: 3,
    maximumFractionDigits: 3,
    });
  }
  },
  computed: {
  fillPercentage() {
    if (this.modalContent && this.modalContent?.vol !== undefined && this.modalContent?.capacity !== undefined) {
      return ((this.modalContent?.vol / this.modalContent?.capacity) * 100).toFixed();
    }
    return 0;
  },
},
};
</script>

<style scoped>
.tank-modal {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border: 1px solid #ddd;
  /* padding: 10px; */
  height: 500px;
  width: 800px;
  background-color:rgb(79, 85, 78);
  color:aliceblue;
  border-radius: 10px;
}

.tank-modal-items {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  /* background-color:rgb(9, 56, 56); */
  width: 50%;
  height: 100%;
}
.fuel-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  /* border: 1px solid #ccc; */
  padding-top: 20px;
  /* border-radius: 10px; */
  width: 300px;
  height: 95%;
  /* box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); */
  /* margin-bottom: 3%; */
}

.circle-container {
  position: relative;
}

.circle {
  position: relative;
  width: 150;
  height: 150;
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

.fuel-info-item-first {
  border-radius: 10px 10px 0px 0px;
}

.fuel-info-item-last {
  border-radius: 0px 0px 10px 10px;
}
.Online {
  border-radius: 5px;
  background-color:#04ab0c;
  width: 70px;
}
.Offline {
  border-radius: 5px;
  background-color:#f1168b;
  width: 70px;
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
