<template>
  
    <b-alert show variant="light" class="cover-selects">
      <b-row class="justify-content-md-center">
        <b-col cols="6">
          <multiselect v-model="company" :options="company_array" :multiple="false" label="Name" track-by="Company_id" :allow-empty="false" placeholder="Select Company" deselectLabel=" "></multiselect>
        </b-col>
        <b-col cols="6">
          <multiselect v-model="site" :options="site_array" :multiple="false" label="Name" track-by="Site_id" :allow-empty="false" placeholder="Select Site" v-if="show_sites"></multiselect>
        </b-col>
      </b-row>
    </b-alert>

</template>
<script type="text/javascript">
import Multiselect from 'vue-multiselect';
import Notify from '@/MyClasses/Notify';
import SiteClass from '@/Models/SiteClass';

import UtilityClass from '@/MyClasses/UtilityClass';

export default {
  components: {
    multiselect: Multiselect
  },
  name: 'toggle-bar',
  props: {
    company_array: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      company: '',
      show_sites:true,
      site_array: [],
      site: '',
      company_site_array: {},
    };
  },
  methods: {
  },
  created() {
    this.SiteClass = new SiteClass();
  },
  watch: {
    site: function(newsite){

      var $this =  this;
      if (newsite) {
        $this.$emit("ShowTankForm", {site: newsite});
      }

    },
    company: function(newcompany) {
      var $this = this;
      $this.$emit("ShowTankForm",{site:""}); //Clear the search key
      if (newcompany) {

        $this.$emit("ClearTankForm");

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
    }
  }
};

</script>
<style type="text/css">
.toggleborder {
  margin-bottom: 5px
}

</style>
