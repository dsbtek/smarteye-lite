<template>
  <div class="fuel-card">
    <div class="circle-container">
      <TankLevelImage
            :volume="tankData?.vol"
            :capacity="tankData?.capacity"
            :percent="fillPercentage"
          />
    </div>
    <div class="fuel-info">
      <div class="fuel-info-item">
        <p>Tank Name: </p>
        <p>{{ tankData?.tank_name }}</p>
      </div>

      <div class="fuel-info-item">
        <p>Capacity: </p>
        <p>{{ formattedNumber(tankData?.capacity) }} L</p>
      </div>

      <div class="fuel-info-item">
        <p>Volume: </p>
        <p>{{ formattedNumber(tankData?.vol) }} L</p>
      </div>

      <div class ="fuel-info-item">
        <p>TCV: </p>
        <p>{{ formattedNumber(tankData?.tcv) }} L</p>
      </div>

      <div class="fuel-info-item">
        <p>Height: </p>
        <p>{{ formattedNumber(tankData?.height) }} mm</p>
      </div>

      <div class="fuel-info-item">
        <p>Product: </p>
        <p>{{ tankData?.product }}</p>
      </div>

      <div class="fuel-info-item-last">
        <p>Av. Temp: </p>
        <p>{{ tankData?.avg_temp }} &#8451;</p>
      </div>

      <div class="fuel-info-item">
          <p>Temperature Status: </p>
          <p :class="getHourDifference(tankData?.date_time)">{{ getHourDifference(tankData?.date_time) }}</p>
        </div>

        <div class="fuel-info-item fuel-info-item-last">
          <p>ATG Status: </p>
          <p :class="getHourDifference(tankData?.atg_time)">{{ getHourDifference(tankData?.atg_time) }}</p>
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
    if (this.tankData && this.tankData?.vol !== undefined && this.tankData?.capacity !== undefined) {
      return ((this.tankData?.vol / this.tankData?.capacity) * 100).toFixed();
    }
    return 0;
  },
},
methods:{
  getHourDifference(dateTime2) {
    const dateTime1 = new Date();
    const timestamp1 = new Date(dateTime1).getTime();
    const timestamp2 = new Date(dateTime2).getTime();

    // Check if either date is invalid
    if (isNaN(timestamp1) || isNaN(timestamp2)) {
        return "Inactive";
    }

    // Calculate the time difference in milliseconds
    const timeDifference = Math.abs(timestamp2 - timestamp1);
    
    // Check if timeDifference is NaN (which could happen in some edge cases)
    if (isNaN(timeDifference)) {
        return "Inactive";
    }

    // Convert the time difference to hours
    const hoursDifference = timeDifference / (1000 * 60 * 60);
    if (hoursDifference > 24) {
        return "Offline";
    } else if (hoursDifference > 4) {
        return "Offline";
    } else {
        return "Online";
    }
},
  formattedNumber(num){ return num.toLocaleString('en-US', {
    minimumFractionDigits: 3,
    maximumFractionDigits: 3,
    });
  }
}
};
</script>

<style scoped>
.fuel-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  border: 1px solid #ccc;
  color: rgb(85, 85, 86);
  padding-top: 20px;
  border-radius: 10px;
  width: 300px;
  height: 500px;
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
  width: 100%;
  height: 2em;
  border: #ccc 1px solid;
  padding: 5px;
}

.Online {
  border-radius: 5px;
  background-color:#04ab0c;
  width: 70px;
}
.Offline {
  border-radius: 5px;
  background-color:#f1f116;
  width: 70px;
}

.Inactive {
  border-radius: 5px;
  background-color:#f1168b;
  width: 70px;
}

.fuel-info-item-last {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  height: 2em;
  padding: 5px;
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
