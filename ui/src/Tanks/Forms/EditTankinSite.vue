<template>
  <b-card v-if="Product" class="card-accent-primary">
    <div slot="header">
      <strong>Edit Tank</strong>
      <span variant="success" class="float-right cusor" @click="closeTankEdit"
        ><i class="fa fa-window-close"></i> close</span
      >
    </div>
    <b-form @submit.prevent="processForm" ref="SubmitForm" id="myform">
      <div>
        <b-row>
          <b-col md="6">
            <b-form-group>
              <label for="Name">Name</label>
              <b-form-input
                required
                type="text"
                id="Name"
                v-model="Name"
                placeholder="Name of Tank"
              ></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Product">Product</label>
              <multiselect
                v-model="Product"
                :options="productslist"
                :multiple="false"
                label="Name"
                track-by="Product_id"
              ></multiselect>
            </b-form-group>
          </b-col>

          <b-col md="4">
            <b-form-group>
              <label for="ControlMode">Control Mode </label>
              <multiselect
                @input="ControlChange($event)"
                v-model="ControlMode"
                :options="control_mode"
                :multiple="false"
                label="name"
                track-by="id"
                :allow-empty="false"
                deselectLabel=" "
                id="ControlMode"
              ></multiselect>
            </b-form-group>
          </b-col>

          <b-col md="4" v-if="ControlMode.id == 'C'">
            <b-form-group>
              <label for="ControllerType">Controller Type</label>
              <multiselect
                v-model="ControllerType"
                :options="controller_type"
                :multiple="false"
                label="name"
                track-by="id"
                :allow-empty="false"
                deselectLabel=" "
                id="ControllerType"
              ></multiselect>
            </b-form-group>
          </b-col>

          <b-col md="4" v-if="ControlMode.id == 'R'">
            <b-form-group>
              <label for="ControllerType">Controller Type</label>
              <multiselect
                v-model="ControllerType"
                :options="probe_type_rs"
                :multiple="false"
                label="name"
                track-by="slug"
                :allow-empty="false"
                deselectLabel=" "
                id="ControllerType"
              ></multiselect>
            </b-form-group>
          </b-col>

          <b-col md="4" v-if="ControlMode.id == 'S'">
            <b-form-group>
              <label for="ControllerType">Controller Type</label>
              <multiselect
                v-model="ControllerType"
                :options="probe_type"
                :multiple="false"
                label="name"
                track-by="slug"
                :allow-empty="false"
                deselectLabel=" "
                id="ControllerType"
              ></multiselect>
            </b-form-group>
          </b-col>

          <b-col md="4">
            <b-form-group>
              <label for="Controller_polling_address"
                >Controller Polling Address</label
              >
              <b-form-input
                type="number"
                min="1"
                max="10"
                step="1"
                v-model="Controller_polling_address"
                id="Controller_polling_address"
                placeholder="Controller Polling Address"
              ></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Tank_index">Tank Index</label>
              <b-form-input
                type="number"
                min="1"
                v-model="Tank_index"
                id="Tank_index"
                placeholder="Tank Index"
              ></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Capacity">Capacity</label>
              <b-form-input
                type="number"
                min="1"
                v-model="Capacity"
                id="Capacity"
                placeholder="Tank Capacity"
              ></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="UOM">Unit of Measurement </label>
              <multiselect
                v-model="UOM"
                :options="UOMlist"
                :multiple="false"
                label="name"
                track-by="id"
                :allow-empty="false"
                deselectLabel=" "
                id="UOM"
              ></multiselect>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Shape">Shape </label>
              <multiselect
                v-model="Shape"
                :options="shape_list"
                :multiple="false"
                label="name"
                track-by="id"
                :allow-empty="false"
                deselectLabel=" "
                id="Shape"
              ></multiselect>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="LL_Level">Tank Low Low Level</label>
              <b-form-input
                type="number"
                min="0"
                v-model="LL_Level"
                id="LL_Level"
                placeholder="Tank Low Low Level"
              ></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="L_Level">Tank Low Level</label>
              <b-form-input
                type="number"
                min="0"
                v-model="L_Level"
                id="L_Level"
                placeholder="Tank Low  Level"
              ></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="HH_Level">Tank High High Level</label>
              <b-form-input
                type="number"
                min="0"
                v-model="HH_Level"
                id="HH_Level"
                placeholder="Tank High High Level"
              ></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="H_Level">Tank High Level</label>
              <b-form-input
                type="number"
                min="0"
                v-model="H_Level"
                id="HH_Level"
                placeholder="Tank High  Level"
              ></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Reorder">Reorder level</label>
              <b-form-input
                type="number"
                min="0"
                v-model="Reorder"
                id="Reorder"
                placeholder="Reorder level"
              ></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Leak">Leak level</label>
              <b-form-input
                ttype="number"
                min="0"
                v-model="Leak"
                id="Leak"
                placeholder="Leak level"
              ></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Leak">Anomaly Volume</label>
              <b-form-input
                type="number"
                min="0"
                v-model="Anomaly_volume"
                id="Anomaly_volume"
                placeholder="Maximum volume drop within the anomaly period"
              ></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Leak">Anomaly period (minutes)</label>
              <b-form-input
                type="number"
                min="0"
                v-model="Anomaly_period"
                id="Anomaly_period"
                placeholder="Time in minutes at which anomaly volume is active"
              ></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Leak">Tank Height</label>
              <b-form-input
                type="number"
                min="0"
                v-model="Tank_height"
                id="Tank_height"
                placeholder="Tank Maximum Height"
              ></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Note">Note</label>
              <b-form-input
                type="text"
                maxlength="22"
                v-model="Tank_Note"
                id="Tank_Note"
                placeholder="(Optional) Short note/comment for tank"
              ></b-form-input>
            </b-form-group>
          </b-col>

          <template v-if="calibrationEligible">
            <b-col md="6">
              <b-form-group>
                <label for="Chart">Upload Calibration Chart</label>
                <b-form-file
                  :state="Boolean(calibrationChart)"
                  v-model="calibrationChart"
                  id="Chart"
                  placeholder="Choose a file..."
                ></b-form-file>
              </b-form-group>
            </b-col>

            <b-col md="6">
              <b-form-group>
                <label for="offset">Offset</label>
                <b-form-input
                  type="number"
                  v-model="offset"
                  id="offset"
                  placeholder="Offset"
                ></b-form-input>
              </b-form-group>
            </b-col>

            <b-col md="6">
              <b-form-group>
                <label for="po4">Tank PO4 (mm)</label>
                <b-form-input
                  type="number"
                  v-model="po4"
                  id="po4"
                  placeholder="Tank PO4(mm)"
                ></b-form-input>
              </b-form-group>
            </b-col>

            <b-col md="6" v-if="ControlMode.id == 'S'">
              <b-form-group>
                <label for="Density">Density</label>
                <b-form-input
                  type="text"
                  v-model="Density"
                  id="po4"
                  placeholder="Liquid Density"
                ></b-form-input>
              </b-form-group>
            </b-col>
          </template>
        </b-row>
      </div>

      <div slot="footer">
        <b-button type="submit" size="sm" variant="primary" :disabled="loading"
          ><i class="fa fa-dot-circle-o"></i> Submit</b-button
        >
      </div>
    </b-form>
  </b-card>
</template>
<script type="text/javascript">
import Multiselect from "vue-multiselect";
import UtilityClass from "@/MyClasses/UtilityClass";
import Notify from "@/MyClasses/Notify";
import TankClass from "@/Models/TankClass";
import EditTankClass from "@/MyViews/Tanks/Classes/EditTankClass";
import ProbeClass from "@/Models/ProbeClass";
export default {
  components: {
    multiselect: Multiselect,
  },
  props: ["tankdata"],
  name: "forms",
  data() {
    return {
      // firstLoad: true,
      selected: [], // Must be an array reference!
      show: true,
      Name: "",
      Product: "",
      Controller_polling_address: "",
      Tank_index: "",
      Capacity: "",
      UOM: "",
      Shape: "",
      LL_Level: "",
      L_Level: "",
      HH_Level: "",
      H_Level: "",
      Reorder: "",
      Leak: "",
      Tank_height: "",
      Tank_Note: "",
      Anomaly_period: "",
      Anomaly_volume: "",
      calibrationChart: null,
      offset: "",
      po4: "",
      Density: "",

      addedTank: "",
      controller_type: [],
      ControllerType: "",
      ControlMode: "",
      control_mode: [],

      UOMlist: [],
      shape_list: "",
      productslist: [],

      TankSubmitteed: false,

      loading: false,
      tank_data: "me",
    };
  },
  computed: {
    companies: function () {
      return this.$store.state.company.AllCompanies;
    },
    tankEdit: function () {
      return this.$store.state.tank.EdittedTank;
    },
    calibrationEligible() {
      return this.ControlMode.id == "S" || this.ControlMode.id == "R";
    },
    probe_type() {
      let related_probes = [];
      this.$store.state.probe.AllProbes.forEach(function (eachValue) {
        if (
          eachValue["slug"] !== "STL" &&
          eachValue["slug"] !== "GMC-485-S" &&
          eachValue["slug"] !== "GMC-485-D" &&
          eachValue["slug"] !== "GMC-485-U" &&
          eachValue["slug"] !== "GMC-485-H"
        ) {
          related_probes.push(eachValue);
        }
      });
      return related_probes;
    },

    probe_type_rs() {
      let related_probes = [];
      this.$store.state.probe.AllProbes.forEach(function (eachValue) {
        if (
          eachValue["slug"] === "STL" ||
          eachValue["slug"] === "GMC-485-S" ||
          eachValue["slug"] === "GMC-485-D" ||
          eachValue["slug"] === "GMC-485-U" ||
          eachValue["slug"] === "GMC-485-H"
        ) {
          related_probes.push(eachValue);
        }
      });
      return related_probes;
    },
  },
  methods: {
    ControlChange: function (mode) {
      this.ControllerType = "";

      if (mode.id !== "S" || mode.id !== "R") {
        this.calibrationChart = null;
        this.offset = null;
        this.po4 = null;
      }
    },

    closeTankEdit() {
      this.$emit("closeTankEdit");
    },
    FillUpTank: function (newtankdata) {
      let get_tank_data = this.tankEdit;
      console.log(get_tank_data.Product)
      var _tempcont = this.TankClass.findTANKCONT(
        newtankdata["Controller Type"],
        true
      );
      if (_tempcont == "probe") {
        this.probe_type.forEach(function (element) {
          if (element.slug == newtankdata["Controller Type"]) {
            _tempcont = element;
          }
        });
      }
      this.ControllerType = _tempcont;
      this.Name = newtankdata.Name;
      this.Product = get_tank_data.Product;
      this.Controller_polling_address = newtankdata.Controller_polling_address;
      this.Tank_index = newtankdata.Tank_index;
      this.Capacity = newtankdata.Capacity;
      this.UOM = this.TankClass.findUOM(newtankdata.UOM, true);
      this.Shape = this.TankClass.findSHAPE(get_tank_data.Shape, true);
      this.LL_Level = get_tank_data.LL_Level;
      this.L_Level = get_tank_data.LL_Level;
      this.HH_Level = get_tank_data.HH_Level;
      this.H_Level = get_tank_data.H_Level;
      this.Reorder = get_tank_data.Reorder;
      this.Leak = get_tank_data.Leak;
      this.Site = newtankdata.Site;
      this.Density = get_tank_data.Density;
      this.Tank_height = get_tank_data.Tank_height;
      this.Tank_Note = get_tank_data.Tank_Note;
      this.Anomaly_period = get_tank_data.Anomaly_period;
      this.Anomaly_volume = get_tank_data.Anomaly_volume;

      // this.ControllerType = this.TankClass.findTANKCONT(newtankdata["Controller Type"],true);
      this.calibrationChart = null;
      this.offset = get_tank_data.Offset;
      this.po4 = get_tank_data.Po4;
      this.ControlMode = this.TankClass.findControlMode(
        newtankdata.Tank_controller,
        get_tank_data.Control_mode,
        true
      );
    },
    processForm(event) {
      this.EditTankClass.Name = this.Name;
      this.EditTankClass.Product = this.Product;
      this.EditTankClass.Site = this.Site;
      this.EditTankClass.Tank_index = this.Tank_index;
      this.EditTankClass.Capacity = this.Capacity;
      this.EditTankClass.UOM = this.UOM;
      this.EditTankClass.Shape = this.Shape;
      this.EditTankClass.LL_Level = this.LL_Level;
      this.EditTankClass.L_Level = this.L_Level;
      this.EditTankClass.HH_Level = this.HH_Level;
      this.EditTankClass.H_Level = this.H_Level;
      this.EditTankClass.Reorder = this.Reorder;
      this.EditTankClass.Leak = this.Leak;
      this.EditTankClass.Controller_polling_address =
        this.Controller_polling_address;
      this.EditTankClass.Tank_id = this.tankdata.Tank_id;
      this.EditTankClass.ControllerType = this.ControllerType;
      this.EditTankClass.calibrationChart = this.calibrationChart;
      this.EditTankClass.offset = this.offset;
      this.EditTankClass.po4 = this.po4;
      this.EditTankClass.ControlMode = this.ControlMode;
      this.EditTankClass.Density = this.Density;
      this.EditTankClass.Tank_height = this.Tank_height;
      this.EditTankClass.Tank_Note = this.Tank_Note;
      this.EditTankClass.Anomaly_volume = this.Anomaly_volume;
      this.EditTankClass.Anomaly_period = this.Anomaly_period;

      var $this = this;
      var returned = this.EditTankClass.ProceedTosubmit();

      if (UtilityClass.isPromise(returned)) {
        $this.loading = true;
        returned
          .then(function (result) {
            $this.loading = false;

            Notify.info("Tank Edited successfully");
            $this.$emit("closeTankEdit");
          })
          .catch(function (error) {
            $this.loading = false;
          });
      }
    },
    ClearForm() {
      this.Name = "";
      this.Product = "";
      this.Tank_index = "";
      this.Capacity = "";
      this.UOM = "";
      this.Shape = "";
      this.LL_Level = "";
      this.L_Level = "";
      this.HH_Level = "";
      this.H_Level = "";
      this.Reorder = "";
      this.Leak = "";
      this.Controller_polling_address = "";
      this.calibrationChart = null;
      this.offset = "";
      this.po4 = "";
      this.ControllerType = "";
      this.ControlMode = "";
      this.Density = "";
      this.Tank_height = "";
      this.Anomaly_height = "";
      this.Anomaly_period = "";
    },
  },
  mounted: function mounted() {
    this.FillUpTank(this.tankdata);
  },

  watch: {
    tankdata(newtankdata) {
      if (newtankdata) {
        this.FillUpTank(newtankdata);
      }
    },
  },
  created() {
    this.TankClass = new TankClass();
    this.productslist = this.TankClass.productslist;
    this.controller_type = this.TankClass.controller_type;
    this.control_mode = this.TankClass.control_mode;
    this.UOMlist = this.TankClass.UOM;
    this.shape_list = this.TankClass.shape_list;
    this.EditTankClass = new EditTankClass();
    this.ProbeClass = new ProbeClass();
    this.ProbeClass.getAllProbes();
    // this.TankClass.getTankById(this.tankdata.Tank_id);
  },
};
</script>
