<template>
  <div class="animated fadeIn">
    <togglebar
      v-model="showForm"
      v-if="CanCreate"
      :switchText="formText"
      :checked="checked"
    ></togglebar>

    <b-row align-h="center" v-if="showForm && !isEdit" id="register-tank-div">
      <b-col md="12">
        <companysite
          @ClearTankForm="showTanksForm = false"
          :company_array="company_array"
          @ShowTankForm="PopulateSite"
          id="register-device-div"
        >
        </companysite>
      </b-col>

      <b-col v-if="showTanksForm">
        <TankView :Site="ActiveSite"> </TankView>
      </b-col>
    </b-row>

    <b-row
      v-if="isEdit && showForm && tank_edit_"
      id="edit-tank-div"
      align-h="center"
    >
      <b-col cols="12" md="12">
        <EdittankForm
          :tankdata="tankdata"
          @closeTankEdit="closeEditForm"
        ></EdittankForm>
      </b-col>
    </b-row>

    <b-row>
      <b-col cols="12" md="12">
        <tankstable @EditTank="EditTank" :SiteName="SiteName"> </tankstable>
      </b-col>
    </b-row>
  </div>
</template>

<script type="text/javascript">
import togglebar from "@/components/togglebar";
import createdevice from "@/MyViews/Devices/Forms/createdevice";
import CompanyClass from "@/Models/CompanyClass";
import TankClass from "@/Models/TankClass";
import tankstable from "@/MyViews/Tanks/Tables/tankstable";
import companysite from "@/MyViews/Tanks/Components/company-site-select";

import UserSession from "@/MyClasses/UserSession";
import TankView from "@/MyViews/Tanks/Forms/createTankinSite";

import EdittankForm from "@/MyViews/Tanks/Forms/EditTankinSite";

import controllertable from "@/MyViews/Controllers/Tables/controllers";

export default {
  components: {
    togglebar,
    createdevice,
    controllertable,
    tankstable,
    companysite,
    TankView,
    EdittankForm,
  },
  name: "add-and-view-devices",
  data() {
    return {
      selected: [], // Must be an array reference!
      showTanksForm: false,
      formText: "Add New Tank",
      showForm: false,
      isEdit: false,
      checked: false,
      edituserdata: "",
      ActiveSite: "",
      tankdata: "",
      SiteName: "",
      tank_edit_: null,
    };
  },
  methods: {
    click() {
      // do nothing
    },
    closeEditForm(data) {
      this.isEdit = false;
      this.checked = false;
    },
    EditTank(data) {
      //console.log(data);

      this.tankdata = data;
      this.TankClass.getTankById(data.Tank_id);
      this.tank_edit_ = this.tankEdit;
      //this.showForm = true;
      this.isEdit = true;
      this.checked = true;

      this.$nextTick(() => {
        this.$scrollTo("#edit-tank-div");
      });
    },
    PopulateSite(event) {
      this.SiteName = "";
      //Some times I send an empty site value just to filter the table

      if (event.site) {
        this.showTanksForm = true;
        this.ActiveSite = event.site;
        this.SiteName = event.site.Name;
      }
    },
  },
  computed: {
    CanCreate() {
      return UserSession.ISsuperadmin() || UserSession.ISE360admin();
    },
    tankEdit: function () {
      return this.$store.state.tank.EdittedTank;
    },
    company_array: function () {
      return this.$store.state.company.AllCompanies;
    },
  },
  created() {
    this.CompanyClass = new CompanyClass();
    this.CompanyClass.getAllCompanies();

    this.TankClass = new TankClass();
    this.TankClass.getAllTanks();
  },
  watch: {
    isCreate: function (newadd) {
      if (newadd) {
        this.formText = "Close Registration Form";
      } else {
        this.formText = "Open Registration Form";
      }
    },
    showForm: function (newshowForm) {
      if (!newshowForm) {
        this.showTanksForm = false;
      }

      if (newshowForm) {
        this.formText = "Close Form";
      } else {
        this.formText = "Add New Tank";
      }
    },
  },
};
</script>
<!-- text.html.vue meta.tag.script.end.html entity.name.tag.script.html -->

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

</script>
