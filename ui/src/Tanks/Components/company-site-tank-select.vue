<template>

    <b-alert show variant="light" class="cover-selects">
      <b-row class="justify-content-md-center">
        <b-col cols="4">
          <multiselect v-model="company" :options="company_array" :multiple="false" label="Name" track-by="Company_id" :allow-empty="false" placeholder="Select Company" deselectLabel=" "></multiselect>
        </b-col>
        <b-col cols="4">
          <multiselect v-model="site" :options="site_array" :multiple="false" label="Name" track-by="Site_id" :allow-empty="false" placeholder="Select Site"></multiselect>
        </b-col>
        <b-col cols="3">
          <multiselect v-model="tank" :options="tank_array" :multiple="false" label="Name" track-by="Tank_id" :allow-empty="false" placeholder="Select Tank"></multiselect>
        </b-col>
        <b-col cols="1">
          <b-button size="md" type="submit" variant="success" @click="fetchNewDetails()">
            Submit
          </b-button>
        </b-col>
      </b-row>
    </b-alert>

</template>
<script type="text/javascript">
import Multiselect from 'vue-multiselect';
import Notify from '@/MyClasses/Notify';
import SiteClass from '@/Models/SiteClass';
import TankClass from '@/Models/TankClass';
import CompanyClass from '@/Models/CompanyClass';
import UtilityClass from '@/MyClasses/UtilityClass';

export default {
  components: {
    multiselect: Multiselect
  },
  name: 'company-site-tank-select',
  data() {
    return {
      company: '',
      site_array: [],
      site: '',
      tank_array: [],
      tank: '',
      company_site_array: {},
      site_tank_array: {}
    };
  },
  methods: {
      fetchNewDetails() {
          if (!this.tank){
              Notify.warning('Tank Selection is empty');
          }else{
              this.$emit('NewTankLogs', {tank:this.tank});
          }
      }
  },
  created() {
    this.SiteClass = new SiteClass();
    this.TankClass = new TankClass();
    this.CompanyClass = new CompanyClass();
    this.CompanyClass.getAllCompanies();
  },
  computed: {
      company_array: function(){
      return this.$store.state.company.AllCompanies;
    }
  },
  watch: {
    company: function(newcompany) {
      var $this = this;
      if (newcompany) {

        if (!this.company_site_array[newcompany.Company_id]) {
          UtilityClass.onSpinner(".cover-selects");

          var result = this.SiteClass.getSitesInCompany(newcompany.Company_id);
          result.then(function(sites) {
            UtilityClass.offSpinner(".cover-selects");
            $this.site_array = sites;
            $this.company_site_array[newcompany.Company_id] = sites;

            $this.site = '';

          }).catch(function(){

            UtilityClass.offSpinner(".cover-selects");
          });
        } else {

          $this.site_array = $this.company_site_array[newcompany.Company_id];
          $this.site = '';

        }

      }
    },
    site: function(newsite) {
        var $this = this;
      if (newsite) {

        if (!this.site_tank_array[newsite.Site_id]) {
          UtilityClass.onSpinner(".cover-selects");

          var result = this.TankClass.TankIDSfromSite({"site":newsite.Site_id});
          result.then(function(tanks) {
            UtilityClass.offSpinner(".cover-selects");
            $this.tank_array = tanks;
            $this.site_tank_array[newsite.Site_id] = tanks;

            $this.tank = '';

          }).catch(function(){

            UtilityClass.offSpinner(".cover-selects");
          });
        } else {

          $this.tank_array = $this.site_tank_array[newsite.Site_id];
          $this.tank = '';

        }

      }
    }
  }
};

</script>
<style type="text/css">
.toggleborder {
  margin-bottom: 5px
}

</style>
