<template>
    <b-modal id="calibrationChartModal" title="Chart Preview" hide-footer hide-header-close no-close-on-esc no-close-on-backdrop>
        <!-- <div v-if="!tankdetails.CalibrationChart">
            <p>{{error_text}}</p>
        </div> -->
        <div>
            <div class="text-center" v-if="!chartLoaded">
                <b-spinner variant="primary" label="Text Centered" /> &nbsp; &nbsp; loading ...
            </div>
            <div v-else>
                <div v-if="!chart">
                    <p>{{error_text}}</p>
                </div>
                <div v-else>
                    <b-table striped hover :items="items" :fields="fields">
                    </b-table>  
                </div>
                <hr>
            </div>
        </div>
        <b-btn class="mt-1" variant="warning" block @click="hideModal()">Dismiss</b-btn>
    </b-modal>
</template>

<script type="text/javascript">
import TankClass from '@/Models/TankClass';

export default {
    name: 'calibration-chart-modal',
    props: ['tankdetails'],
    data(){
        return {
            chartLoaded: false,
            fields: [
                {key:"Volume(ltrs)",label:"Product Volume (ltrs)"},
                {key:"Height(mm)",label:"Product Height (mm)"},
            ],
            items: '',
            chart: false,
            error_text: 'Oops, no chart has been loaded!'
            

        }
    },
    methods:{
        hideModal(){
            this.$bvModal.hide('calibrationChartModal');
            this.$emit('hideModal');
        },

    },
    mounted() {
        this.$bvModal.show('calibrationChartModal');
        var $this = this;
        this.TankClass.GetTankChart(this.tankdetails.Tank_id).then((data) => {
            if (data.status !== 'success'){
                $this.error_text = data.errors 
                $this.chartLoaded = true;
                $this.chart = false;        
            }
            else{
                $this.items = data.data;
                this.chartLoaded = true;
                this.chart = true;
            }
            
        });
    },
    created(){
        //connect to dB
        this.TankClass = new TankClass();

    }


}
</script>