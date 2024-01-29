<template>
  <div class="animated fadeIn">
    <b-row align-h="center">
      <b-col>
        <companysitetank @NewTankLogs="fetchNewLogs"></companysitetank>
      </b-col>
    </b-row>
    <b-row align-h="center" v-if="showLogs">
      <b-col>
        <b-card :header="caption">
          <b-table
            :striped="true"
            :hover="true"
            responsive
            :fields="tablefields"
            :items="items"
          >
            <template slot="Current Offset value" slot-scope="data">
              <p v-if="!data.value">N/A</p>
              <p v-else>{{ data.value }}</p>
            </template>
            <template slot="Height" slot-scope="data">
              {{ data.value }}mm
            </template>
            <template slot="Volume" slot-scope="data">
              {{ data.value }}{{ data.item.Unit }}
            </template>
            <template slot="New Height" slot-scope="data">
              <strong>{{ parsed + parseFloat(data.item.Height) }}mm</strong>
            </template>
          </b-table>
          <div slot="footer">
            <b-row>
              <b-col sm="2">
                <h5>Input Dip Height Value:</h5>
              </b-col>
              <b-col sm="2.5">
                <b-form-input
                  :type="'number'"
                  :step="'0.1'"
                  :state="null"
                  v-model="newOffset"
                  placeholder="Input Dip Height Value"
                ></b-form-input>
              </b-col>
              <b-col sm="2">
                <h5>Input ATG Height:</h5>
              </b-col>
              <b-col sm="2.5">
                <b-form-input
                  :type="'number'"
                  :step="'0.1'"
                  :state="null"
                  v-model="atgHeight"
                  placeholder="Input ATG Height"
                ></b-form-input>
              </b-col>
              <b-col sm="3">
                <b-button
                  type="submit"
                  size="md"
                  variant="secondary"
                  @click="EvaluateOffset"
                  >Apply</b-button
                >
                &nbsp;&nbsp;
                <b-button
                  type="submit"
                  size="md"
                  variant="warning"
                  @click.prevent="RevertOffset"
                  >Revert</b-button
                >
                &nbsp;&nbsp;
                <b-button
                  type="submit"
                  size="md"
                  variant="primary"
                  @click.prevent="saveOffset"
                  >Save</b-button
                >
              </b-col>
            </b-row>
          </div>
        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import companysitetank from "./Components/company-site-tank-select";
import TankClass from "@/Models/TankClass";
import Notify from "@/MyClasses/Notify";

export default {
  components: {
    companysitetank,
  },
  data() {
    return {
      selectedtank: "",
      showLogs: false,
      caption: "Tank Most Recent Logs",
      items: [],
      fields: [
        { key: "Site Name", label: "Site" },
        { key: "Tank Name", label: "Tank" },
        { key: "Height", label: "Height" },
        { key: "Volume", label: "Volume" },
        { key: "Current Offset value", label: "Offset" },
        { key: "Log Time", label: "Log Time" },
      ],
      newOffset: "",
      atgHeight: "",
      newheightflag: false,
      parsed: 0.0,
      applied: false,
    };
  },
  filters: {
    parsefloat: function (value) {
      var parsed = parseFloat(value);
      if (parsed) {
        return parsed;
      }
    },
  },
  computed: {
    tablefields() {
      return this.fields;
    },
    evaluatedOffset() {
      let offset = this.items[0]["Current Offset value"];
      if (offset) {
        return this.parsed;
      } else {
        return this.parsed;
      }
    },
  },
  methods: {
    fetchNewLogs(event) {
      this.showLogs = true;
      if (this.selectedtank !== event.tank) {
        this.selectedtank = event.tank;
        this.TankClass.TankRecentLogs(this.selectedtank.Tank_id).then(
          (data) => {
            this.items = data;
          }
        );
      }
    },
    RevertOffset() {
      this.newOffset = "";
      this.atgHeight = "";
      this.parsed = 0.0;
      this.newheightflag = false;
      if (this.fields.length == 7) {
        this.fields.splice(3, 1);
      }
      this.applied = false;
    },
    ReloadTankLogs() {
      this.TankClass.TankRecentLogs(this.selectedtank.Tank_id).then(() => {
        this.RevertOffset();
      });
    },

    EvaluateOffset() {
      if (this.newOffset) {
        this.parsed = parseFloat(this.newOffset / this.atgHeight);
        console.log(this.parsed);
        this.applied = true;
        if (!this.newheightflag) {
          // console.log(this.newheightflag)
          var key = { key: "New Height" };
          if (this.fields.length == 6) {
            this.fields.splice(3, 0, key);
          }
          this.newheightflag = true;
        }
      } else {
        Notify.warning("Invalid offset value. Offset must be integer or float");
      }
    },
    saveOffset() {
      if (this.parsed && this.applied) {
        this.TankClass.UpdateOffset({
          Offset: this.evaluatedOffset,
          Tank_id: this.selectedtank.Tank_id,
        });
        this.ReloadTankLogs();
        Notify.success("Tank Offset successfully updated");
      } else {
        Notify.warning("Apply offset before saving");
      }
    },
  },
  created() {
    this.TankClass = new TankClass();
  },
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
