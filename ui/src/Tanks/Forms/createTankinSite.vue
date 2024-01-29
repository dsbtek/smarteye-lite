<template>
  <b-card class="card-accent-primary" >
    <div slot="header">
      <strong>Add Tank to Site</strong>
      <!-- <span variant="success" class="float-right cusor" @click="closeEdit"><i class='fa fa-window-close'></i> close</span> -->
    </div>
    <b-form @submit.prevent="processForm" ref="SubmitForm">
      <div>
        <b-row>

          <b-col md="6">
            <b-form-group>
              <label for="Name">Name</label>
              <b-form-input required type="text" id="Name" v-model="Name" placeholder="Name of Tank"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Product">Product</label>
              <multiselect v-model="Product" :options="productslist" :multiple="false" label="Name" track-by="Product_id" :allow-empty="false" deselectLabel=" " id="Product"></multiselect>
            </b-form-group>
          </b-col>

          <b-col md="4">
            <b-form-group>
              <label for="ControlMode">Control Mode</label>
              <multiselect v-model="ControlMode" :options="control_mode" :multiple="false" label="name" track-by="id" :allow-empty="false" deselectLabel=" " id="ControlMode"></multiselect>
            </b-form-group>
          </b-col>

          <b-col md="4" v-if="ControlMode==''">
            <b-form-group>
              <label for="ControllerType">Controller Type</label>
              <multiselect v-model="ControllerType" :options="empty_type" :multiple="false" label="name" track-by="id" :allow-empty="false" deselectLabel=" " id="ControllerType"></multiselect>
            </b-form-group>
          </b-col>

          <b-col md="4" v-if="ControlMode.id=='C'">
            <b-form-group>
              <label for="ControllerType">Controller Type</label>
              <multiselect v-model="ControllerType" :options="controller_type" :multiple="false" label="name" track-by="id" :allow-empty="false" deselectLabel=" " id="ControllerType"></multiselect>
            </b-form-group>
          </b-col>

          <b-col md="4" v-if="ControlMode.id=='R'">
            <b-form-group>
              <label for="ControllerType">Controller Type</label>
              <multiselect v-model="ControllerType" :options="probe_type_rs" :multiple="false" label="name" track-by="slug" :allow-empty="false" deselectLabel=" " id="ControllerType"></multiselect>
            </b-form-group>
          </b-col>

          <b-col md="4" v-if="ControlMode.id=='S'">
            <b-form-group>
              <label for="ControllerType">Controller Type</label>
              <multiselect v-model="ControllerType" :options="probe_type" :multiple="false" label="name" track-by="slug" :allow-empty="false" deselectLabel=" " id="ControllerType"></multiselect>
            </b-form-group>
          </b-col>

          <b-col md="4">
            <b-form-group>
              <label for="Controller_polling_address">Controller Polling Address</label>
              <b-form-input  type="number" min=1 max=10 step=1 v-model="Controller_polling_address" id="Controller_polling_address" placeholder="Controller Polling Address"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Tank_index">Tank Index / Probe Address</label>
              <b-form-input  type="number" min="1" v-model="Tank_index" id="Tank_index" placeholder="Tank Index"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Capacity">Capacity</label>
              <b-form-input  type="number" min="1" v-model="Capacity" id="Capacity" placeholder="Tank Capacity"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
             <b-form-group>
              <label for="UOM">Unit of Measurement </label>
              <multiselect v-model="UOM" :options="UOMlist" :multiple="false" label="name" track-by="id" :allow-empty="false" deselectLabel=" " id="UOM"></multiselect>
            </b-form-group>
          </b-col>

          <b-col md="6">
             <b-form-group>
              <label for="Shape">Shape </label>
              <multiselect v-model="Shape" :options="shape_list" :multiple="false" label="name" track-by="id" :allow-empty="false" deselectLabel=" " id="Shape"></multiselect>
            </b-form-group>
          </b-col>

            
          <b-col md="6">
            <b-form-group>
              <label for="LL_Level">Tank Low Low Level</label>
              <b-form-input  type="number" min="0" v-model="LL_Level" id="LL_Level" placeholder="Tank Low Low Level"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="L_Level">Tank Low Level</label>
              <b-form-input  type="number" min="0" v-model="L_Level" id="L_Level" placeholder="Tank Low  Level"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="HH_Level">Tank High High Level</label>
              <b-form-input  type="number" min="0" v-model="HH_Level" id="HH_Level" placeholder="Tank High High Level"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="H_Level">Tank High Level</label>
              <b-form-input  type="number" min="0" v-model="H_Level" id="HH_Level" placeholder="Tank High Level"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Reorder">Reorder level</label>
              <b-form-input  type="number" min="0" v-model="Reorder" id="Reorder" placeholder="Reorder level"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Leak">Leak level</label>
              <b-form-input  type="number" min="0" v-model="Leak" id="Leak" placeholder="Leak level"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Leak">Anomaly Volume</label>
              <b-form-input  type="number" min="0" v-model="Anomaly_volume" id="Anomaly_volume" placeholder="Maximum volume drop within the anomaly period"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Leak">Anomaly period (minutes)</label>
              <b-form-input  type="number" min="0" v-model="Anomaly_period" id="Anomaly_period" placeholder="Time in minutes at which anomaly volume is active"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Leak">Tank Height</label>
              <b-form-input  type="number" min="0" v-model="Tank_height" id="Tank_height" placeholder="Tank Maximum Height"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="Note">Note</label>
              <b-form-input  type="text" maxlength="22" v-model="Tank_Note" id="Tank_Note" placeholder="(Optional) Short note/comment for tank"></b-form-input>
            </b-form-group>
          </b-col>

          <template v-if="calibrationEligible">
          <b-col md="6">
            <b-form-group>
              <label for="Chart">Upload Calibration Chart</label>
              <b-form-file  :state="Boolean(calibrationChart)" v-model="calibrationChart" id="Chart" placeholder="Choose a file..."></b-form-file>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="offset">Offset</label>
              <b-form-input  type="text" v-model="offset" id="offset" placeholder="Offset"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6">
            <b-form-group>
              <label for="po4">Tank PO4</label>
              <b-form-input  type="text" v-model="po4" id="po4" placeholder="Tank PO4(cm)"></b-form-input>
            </b-form-group>
          </b-col>

          <b-col md="6" v-if="ControlMode.id=='S'">
            <b-form-group>
              <label for="Density">Density</label>
              <b-form-input  type="text" v-model="Density" id="Density" placeholder="Liquid Density"></b-form-input>
            </b-form-group>
          </b-col>

          </template>
        </b-row>
        
      </div>

       <div slot="footer">
              <b-button type="submit" size="sm" variant="primary" :disabled="loading"><i class="fa fa-dot-circle-o"></i> Submit</b-button>
        </div>
    </b-form>
  </b-card>
</template>
<script type="text/javascript">
import Multiselect from 'vue-multiselect';
import UtilityClass from '@/MyClasses/UtilityClass';
import Notify from '@/MyClasses/Notify';
import TankClass from '@/Models/TankClass';
import ProbeClass from '@/Models/ProbeClass';
import RegisterTank from '@/MyViews/Tanks/Classes/RegisterTank';

export default {
  components: {
    multiselect: Multiselect
  },

  props: [
    'userdata','Site','item'
  ],
  name: 'forms',
  data() {
    return {
      selected: [], // Must be an array reference!
      show: true,
      Name: '',
      Product: '',
      ControllerType: '',
      ControlMode: '',
      Controller_polling_address: '',
      Tank_index: '',
      Capacity: '',
      UOM: '',
      Shape: '',
      LL_Level: '',
      L_Level: '',
      HH_Level: '',
      H_Level: '',
      Reorder: '',
      Leak: '',
      Tank_height: '',
      Tank_Note:'',
      Anomaly_period: '',
      Anomaly_volume: '',
      calibrationChart: null,
      offset: null,
      po4: null,
      Density: null,
      
      addedTank:'',

      UOMlist:[],
      shape_list:'',
      productslist:[],
      controller_type:[],
      empty_type: [],
      control_mode:[],

      TankSubmitteed:false,

      loading: false,


    };
  },
  computed: {
    companies: function() {
      return this.$store.state.company.AllCompanies;
    },

    probe_type() {
      let related_probes = []
      this.$store.state.probe.AllProbes.forEach(function(eachValue){
        if (eachValue['slug'] !== 'STL' && eachValue['slug'] !== 'GMC-485-S' && eachValue['slug'] !== 'GMC-485-D' && eachValue['slug'] !== 'GMC-485-U' && eachValue['slug'] !== 'GMC-485-H'){
          related_probes.push(eachValue)
        }
      })
      return related_probes
    },

    probe_type_rs() {
      let related_probes = []
      this.$store.state.probe.AllProbes.forEach(function(eachValue){
        if (eachValue['slug'] === 'STL' || eachValue['slug'] === 'GMC-485-S' || eachValue['slug'] === 'GMC-485-D' || eachValue['slug'] === 'GMC-485-U' || eachValue['slug'] === 'GMC-485-H'){
          related_probes.push(eachValue)
        }
      })
      return related_probes
    },

    calibrationEligible() {
      return this.ControlMode.id=='S' || this.ControlMode.id=='R';
    },

  },
  methods: {
    closeEdit() {

      this.$emit("CloseUserEditForm");
    },
    processForm(event) {

      this.RegisterTank.Name = this.Name;
      this.RegisterTank.Product = this.Product;
      this.RegisterTank.Site = this.Site;
      this.RegisterTank.Tank_index = this.Tank_index;
      this.RegisterTank.Capacity = this.Capacity;
      this.RegisterTank.UOM = this.UOM;
      this.RegisterTank.Shape = this.Shape;
      this.RegisterTank.LL_Level = this.LL_Level;
      this.RegisterTank.L_Level = this.L_Level;
      this.RegisterTank.HH_Level = this.HH_Level;
      this.RegisterTank.H_Level = this.H_Level;
      this.RegisterTank.Reorder = this.Reorder;
      this.RegisterTank.Leak = this.Leak;
      this.RegisterTank.ControlMode = this.ControlMode;
      this.RegisterTank.Controller_polling_address = this.Controller_polling_address;
      this.RegisterTank.ControllerType = this.ControllerType;
      this.RegisterTank.calibrationChart = this.calibrationChart;
      this.RegisterTank.offset = this.offset;
      this.RegisterTank.po4 = this.po4;
      this.RegisterTank.Density = this.Density;
      this.RegisterTank.Tank_height = this.Tank_height;
      this.RegisterTank.Tank_Note = this.Tank_Note;
      this.RegisterTank.Anomaly_volume = this.Anomaly_volume;
      this.RegisterTank.Anomaly_period = this.Anomaly_period;
      
      var $this = this;
      var returned = this.RegisterTank.ProceedTosubmit();

      if (UtilityClass.isPromise(returned)) {
          $this.loading = true;
          returned.then(function(result) {
            $this.loading = false;
            $this.TankSubmitteed = true;
            $this.addedTank = result;



            $this.$emit("RemoveTank",{value:$this.item});

            $this.ClearForm();

            Notify.info("Tank Added successfully");

          }).catch(function(error) {
           
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
      this.offset = null;
      this.ControllerType = "";
      this.ControlMode = "";
      this.po4 = null;
      this.Density = "";
      this.Tank_Note="";

    },
  },
  watch: {
    // Tank_index:function(){
    //   this.$emit("RemoveTank",{value:this.item});
    // }
    ControlMode(newMode) {
      this.ControllerType = '';
      if (newMode.id !== 'S') {
        this.calibrationChart = null;
        this.offset = null;
        this.po4 = null;
      }
    }
  },
  created() {

    this.TankClass =  new TankClass();
    this.productslist = this.TankClass.productslist;
    this.UOMlist = this.TankClass.UOM;
    this.shape_list = this.TankClass.shape_list;
    this.controller_type = this.TankClass.controller_type;
    this.control_mode = this.TankClass.control_mode;
    this.RegisterTank =  new RegisterTank();
    this.ProbeClass = new ProbeClass();
    this.ProbeClass.getAllProbes();
  }
};

</script>
