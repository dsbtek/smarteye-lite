<template>
  <!-- <div class="glass" >
    <div class="water" ref="water"></div>
  </div> -->

  <div id="banner" :class="randomClass"> 
 
    <div class="fill">
      <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="300px" height="300px" viewBox="0 0 300 300" enable-background="new 0 0 300 300" xml:space="preserve">
        <path fill="#04ACFF" id="waveShape" d="M300,300V2.5c0,0-0.6-0.1-1.1-0.1c0,0-25.5-2.3-40.5-2.4c-15,0-40.6,2.4-40.6,2.4
              c-12.3,1.1-30.3,1.8-31.9,1.9c-2-0.1-19.7-0.8-32-1.9c0,0-25.8-2.3-40.8-2.4c-15,0-40.8,2.4-40.8,2.4c-12.3,1.1-30.4,1.8-32,1.9
              c-2-0.1-20-0.8-32.2-1.9c0,0-3.1-0.3-8.1-0.7V300H300z" />
      </svg>
    </div>
     <span class="custom-center-style form-inline text-center font-weight-bolder">{{percent}}%</span>
  </div>

</template>
<script>
  //import tank_reading_table from "@/MyViews/Dashboard/table/tank_reading_table";
import UtilityClass from './UtilityClass';
// import products from './products';
import Jquery from "jquery";

export default {
  props: {
    volume: {
      type: [String,Number],
      default: '0'
    },
    capacity: {
      type: [String,Number],
      default: '0'
    },
    percent: {
      type: [String,Number],
      default: 0
    },
    product: {
      type: [String],
      default: ""
    },
    tank_note:{
      default:""
    }

  },
    components: {
        //tankReadingTable: tank_reading_table
    },
    name: 'tank-level-image',
    data() {
        return {
            tabIndex: 0,
            injectedStyle:"",
            randomClass:UtilityClass.randomStringsOnly(),
        };
    },
    methods: {
        deleteStyle(){
          // So here we clear the Injected Styles and make it clear
          if (this.injectedStyle) {
            let seletme = this.injectedStyle.parentNode.querySelectorAll(`.${this.randomClass}`);

            seletme.forEach((node) => {
              node.parentNode.removeChild(node);
            });
            
          }
        },

        setCss(){
          let color = '#c5b550';
          var styleEl = document.createElement("style");
           styleEl =UtilityClass.addClass(styleEl,this.randomClass);
          document.head.appendChild(styleEl);
          let glassStyle = `margin: 3px auto;
                            height: 150px;
                            width: 120px;
                            position: relative;
                            border-style: none solid solid solid;
                            border-width: 5px;
                            border-color: lightgray;
                            border-radius: 10px;`;
                            
          let waterStyle = `width: 100%;
                            height: 3%;
                            background-color: ${color};
                            position: absolute;
                            bottom: 0;`;


          styleEl = UtilityClass.Setcss(styleEl, `.${this.randomClass}`, glassStyle);
          styleEl = UtilityClass.Setcss(styleEl, `.${this.randomClass} .water`, waterStyle);

          this.injectedStyle = styleEl;
          //console.log(styleEl);
        },

        setCircleTankCss(percentage){
          // console.log(percentage)
          percentage = 100-percentage;
          
          let color = '#c5b550';
          var styleEl = document.createElement("style");
           styleEl =UtilityClass.addClass(styleEl,this.randomClass);
          document.head.appendChild(styleEl);

          let fillActionText = UtilityClass.randomStringsOnly(10);
          let WaveActionText = UtilityClass.randomStringsOnly(10);
          let StandardHeight = 150;
          let supposedHeight = (150 * percentage) / 100;

          let banner =`
                        border-radius: 50%;
                        width: 150px;
                        height: 150px;
                        background: #eef1d2;
                        overflow: hidden;
                        backface-visibility: hidden;
                        transform: translate3d(0, 0, 0);
                      `;

          let banner_fill  = `
                              animation-name: ${fillActionText};
                              animation-iteration-count: 1;
                              animation-timing-function: cubic-bezier(.2, .6, .8, .4);
                              animation-duration: 4s;
                              animation-fill-mode: forwards;
                              `;

           let banner_waveShape  = `
                                    animation-name: ${WaveActionText};
                                    animation-iteration-count: infinite;
                                    animation-timing-function: linear;
                                    animation-duration: 2s;
                                    width: 100%;
                                    height: 100%;
                                    fill: ${color};`;

        let fillActionStyle = `
                              @keyframes ${fillActionText} {
                                0% {
                                  transform: translate(0, ${StandardHeight}px);
                                }

                                100% {
                                  transform: translate(0, ${supposedHeight}px);
                                }
                              }`;

let WaveActionStyle = `@keyframes ${WaveActionText} {
                        0% {
                          transform: translate(-${StandardHeight}px, 0);
                        }

                        100% {
                          transform: translate(0, 0);
                        }
                      }`;

          styleEl = UtilityClass.Setcss(styleEl, null, fillActionStyle);
          styleEl = UtilityClass.Setcss(styleEl, null, WaveActionStyle);
          styleEl = UtilityClass.Setcss(styleEl, `.${this.randomClass}`, banner);
          styleEl = UtilityClass.Setcss(styleEl, `.${this.randomClass} .fill`, banner_fill);
          styleEl = UtilityClass.Setcss(styleEl, `.${this.randomClass} #waveShape`, banner_waveShape);
          

        },
        setFluidLevel() {
          
            // let color = UtilityClass.getObjectFromArray(products, "Name", this.product).Color;
            // this.$refs.water.style.backgroundColor = color;
            
            let percent = this.percent>100?100:this.percent;
            this.setCircleTankCss(percent);
            Jquery(this.$refs.water).animate({
                                                height: percent+"%",
                                                // "background-color": color
                                              }, 1000);
        }
    },
    computed: {
       
    },
    watch:{
      percent(){
        this.setFluidLevel();
      }
    },
    mounted() {
    // var $this = this;
    this.$nextTick(() => {
      this.setFluidLevel();
    });
  },

  beforeDestroy() {
    //Delete the style sheet inserted before, so the dom don't get cloged with unused styles
    this.deleteStyle();
  }
};
</script>
<style type="text/css" scoped name="fool" id="Come-fuck">
.custom-center-style {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color:green;
}
</style>
