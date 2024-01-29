<template>
  <b-card :header="caption">
    <SearchTable v-model="filter" />
    <b-table :dark="getScreenMode" :striped="true" :hover="true" responsive :items="devices" :fields="getColumns()" :current-page="currentPage" :per-page="perPage" :filter = "filter" @filtered="streamFilters" :filter-included-fields="filterOn">
      <template #cell(Actions)="data">
        <b-badge variant="warning" class="cusor" v-if="shouldEdit()" @click="EditTank(data.item)">edit</b-badge>&nbsp;&nbsp;
        <b-badge v-b-modal.activatetanknotemodal variant="info" class="cusor mt-2" @click="AddTankNote(data.item)">Note</b-badge>
        <span v-if="data.item.CalibrationChart"><i class="fa fa-check" aria-hidden="true" style="color: green;"></i>&nbsp;&nbsp;
        <b-badge variant="success"  @click="displayChart(data.item)" class="cusor">View chart</b-badge>
        &nbsp;&nbsp;</span>
        &nbsp;&nbsp;
        <b-badge :variant="data.item.Status?'success':'danger'" 
                @click.prevent="ActivateDeActivate(data.item.Status?'Deactivate':'Activate',data.item)" class="cusor" v-if="shouldEdit()">{{data.item.Status?'Active':'Inactive'}}</b-badge>
        <span v-else><i class="fa fa-close" aria-hidden="true" style="color: red;"></i></span>
        
      </template>
    </b-table>
    <calibrationChartModal v-if="chartShow" :tankdetails="selectedTank" @hideModal="HideModal()"></calibrationChartModal>
    <nav>
      <b-pagination :total-rows="rowcount" :per-page="perPage" v-model="currentPage" prev-text="Prev" next-text="Next" />
    </nav>
    <b-modal centered size="md" v-if="activatetanknotemodal" id="activatetanknotemodal" title="Add note/comment for tank.">
      <div>
        <main class="leaderboard__profiles">
          <article class="leaderboard__profile">
            <span class="leaderboard__name">Site: <span>{{addnotedata.Site.Name}}</span></span>
          </article>
          <article class="leaderboard__profile">
            <span class="leaderboard__name">Tank: <span>{{addnotedata.Name}}</span></span>
          </article>
         <article class="leaderboard__profile">
             <b-form-textarea maxlength="22"   style="border:none;"  no-resize  class="reject_style" required type="text" id="rejection_reason" v-model="newnotetext" placeholder="i.e. Service needed!"></b-form-textarea>
          </article>
        </main>
      </div>
      <b-row class="justify-content-md-center">
        <b-col md="6" sm="12" xs="12">
          <b-button :disabled="isLoading" md="2" class="mt-3 custom-color"   block @click="approveNote">Update Note <span v-if="isLoading"><b-spinner small label="Small Spinner" type="grow"></b-spinner></span></b-button>
        </b-col>
        
      </b-row>  
      <div class="text-center text-muted mt-2" style="font-size:11px;">
          Note appears on Tank Dashboard
        </div>    
      <template #modal-footer>
        <span class="text-center"></span>
      </template>
    </b-modal>
  </b-card>
</template>

<script>


import ManipulateTank from '@/MyViews/Tanks/Classes/ManipulateTank';
import UserSession from '@/MyClasses/UserSession';
import SearchTable from '@/components/searchTable';
import calibrationChartModal from '../Components/calibration-chart-modal';
import ActiveDeactiveTank from '@/MyViews/Tanks/Classes/ActiveDeactiveTank';
import UtilityClass from '@/MyClasses/UtilityClass';
import Notify from '@/MyClasses/Notify';
import EditTankNoteClass from '@/MyViews/Tanks/Classes/EditTankNoteClass';


export default {
  components:{
    SearchTable,
    calibrationChartModal
  },
  props:{
    SiteName:String
  },
  name: 'tank-table',
  data: () => {
    return {
      
      caption:" Tanks Tables",
      currentPage: 1,
      perPage: 10,
      totalRows: 0,
      filter: '',
      rowcount:0,
      selectedTank: '',
      chartShow: false,
      activatetanknotemodal: false,
      addnotedata: "",
      newnotetext:"",
      isLoading:false,
      filterOn:['Site Name','Company','Name','Controller Type','Tank Capacity']

    };
  },
  watch:{
    SiteName(newSiteName){
      this.filter = "";
      if (newSiteName) {
        this.filter = newSiteName;
        //console.log(newSiteName);
      }
    }
  },
  methods: {

    HideModal(){
      this.chartShow = false;
    },
    streamFilters(event){
      this.rowcount = event.length;
      //console.log(event);

    },
    shouldEdit(){
      return UserSession.ISsuperadmin() || UserSession.IScompanyadmin()||UserSession.ISE360admin();

    },
     shouldActivate(){
      return UserSession.ISsuperadmin()||UserSession.ISE360admin();

    },
    getBadge (status) {
      return status === 'Active' ? 'success'
        : status === 'Inactive' ? 'secondary'
          : status === 'Pending' ? 'warning'
            : status === 'Banned' ? 'danger' : 'primary';
    },
    getRowCount (items) {
      return items.length;
    },
     EditTank(items) {
      
      this.$emit("EditTank",items);
      return;
    },
    EditItem (items) {
      //{{data.item.Status}}
      this.$root.$emit("ScrollToEdit",items);
      return;
    },
    getColumns(){
      return this.ManipulateTank.TableFields();
    },
    AddTankNote(data){
      this.addnotedata = data
      this.newnotetext=data.Tank_Note
      this.activatetanknotemodal = true
    },

    approveNote(){

      this.addnotedata['Tank_Note'] = this.newnotetext
      this.isLoading = true
      this.UpdateTankNote()
      //validate text input
      // if (this.newnotetext.length < 1){
      //   Notify.warning("Put some texts to continue.")
      //   return;
      // }
      // else{
      //   this.isLoading = true
      //   this.UpdateTankNote()
      // }
      
     
    },
    UpdateTankNote(){
      this.EditTankNoteClass.Tank_Note = this.newnotetext;
      this.EditTankNoteClass.Tank_id = this.addnotedata.Tank_id;
      var $this = this;
      var returned = this.EditTankNoteClass.ProceedToSubmitnote();

      if (UtilityClass.isPromise(returned)) {
          returned.then(function(result) {
            $this.isLoading= false;
            
            Notify.success("Tank Note Updated successfully");

          }).catch(function(error) {
           
            $this.isLoading = false;

          });
      }
     
      
    },

    displayChart(data) {
      this.chartShow = true;
      this.selectedTank = data;
    },
    ActivateDeActivate(state,tank) {
      
      // var r = confirm("Do you really want to "+state+" this tank ?\nDeactivated tanks don't show in Tank Dashboard!");
      var r = confirm("Do you really want to "+state+" this tank ?");
      if (r == true) {
      var $this = this;
      var returned  = this.ActiveDeactiveTank.Toggle(tank.Tank_id);
      if (UtilityClass.isPromise(returned)) {
            $this.loading = true;
              returned.then(function(result){
                $this.loading = false;

                Notify.success("Successfull Action");

              }).catch(function(error){
                $this.loading = false;
                  
              });
        }

      }

    },
  },

  created(){

    this.ManipulateTank = new ManipulateTank();
    this.ActiveDeactiveTank = new ActiveDeactiveTank();
    this.EditTankNoteClass =  new EditTankNoteClass();
  },
  computed: {
    devices: function(){

      var returned = this.ManipulateTank.formatAllTanks(this.$store.state.tank.AllTanks);
      this.rowcount = returned.length;
      return returned;
    },
    getScreenMode(){
      return this.$store.state.user.darkMode;
    },
  },
  
};
</script>

<style lang="scss" scoped>
.reject_style{
    outline: none;
}
*:focus {
    outline: none;
}

.form-control:focus {
  border-color: none;
  -webkit-box-shadow: none;
  box-shadow: none;
}


.leaderboard {
  max-width: 490px;
  width: 100%;
  border-radius: 12px;
  
  &__profiles {
    background-color: #fff;
    border-radius: 0 0 12px 12px;
    padding: 15px 15px 20px;
    display: grid;
    row-gap: 8px;
  }
  
  &__profile {
    display: grid;
    grid-template-columns: 1fr;
    align-items: center;
    padding: 10px 30px 10px 10px;
    overflow: hidden;
    border-radius: 10px;
    box-shadow: 0 5px 7px -1px rgba(51, 51, 51, 0.23);
    cursor: pointer;
    transition: transform .25s cubic-bezier(.7,.98,.86,.98), box-shadow .25s cubic-bezier(.7,.98,.86,.98);
    background-color: #fff;
    
    &:hover {
      transform: scale(1.02);
      box-shadow: 0 1px 5px 1px rgba(51, 51, 51, 0.18);
    }
  }
  
  &__name {
    font-weight: 600;
    font-size: 15px;
    letter-spacing: 0.64px;
    margin-left: 12px;
  }

  &__name > span{
    color: grey;
    border-radius: 10px;
    padding: 2px 10px;
  }
}


.leaderboard {
  box-shadow: 0 0 40px -10px rgba(0, 0, 0, .4);
}

.custom-color{
  background-color: green;
  color: white;
}


</style>

