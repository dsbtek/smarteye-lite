import Notify from '@/MyClasses/Notify';
import HttpAgent from '@/MyClasses/HttpAgent';
import UtilityClass from '@/MyClasses/UtilityClass';
import TankClass from '@/Models/TankClass';

class RegisterTank extends TankClass {

  /* jshint ignore:start */
  _Name;
  _Product;
  _Controller_polling_address;
  _Site;
  _Tank_index;
  _Capacity;
  _UOM;
  _Shape;
  _LL_Level;
  _L_Level;
  _HH_Level;
  _H_Level;
  _Reorder;
  _Leak;
  _Status;
  _ControlMode;
  _ControllerType;
  _calibrationChart;
  _offset;
  _po4;
  _Density;
  _Tank_height;
  _Anomaly_volume;
  _Anomaly_period;
  _Tank_Note;

  compulsory_prop = [
    'Name',
    'Product',
    'Controller_polling_address',
    'Site',
    'Tank_index',
    'Capacity',
    'UOM',
    'Shape',
    'ControllerType'
  ];
  /* jshint ignore:end */
  get po4() {
    return this._po4;
  }
  get Density() {
    return this._Density;
  }
  get Tank_height() {
    return this._Tank_height;
  }
  get Tank_Note() {
    return this._Tank_Note;
  }
  get Anomaly_volume() {
    return this._Anomaly_volume;
  }
  get Anomaly_period() {
    return this._Anomaly_period;
  }
  get calibrationChart() {
    return this._calibrationChart;
  }

  get offset() {
    return this._offset;
  }

  get Controller_polling_address() {
    return this._Controller_polling_address;
  }

  get Site() {
    return this._Site;
  }
  get Name() {
    return this._Name;
  }

  get Product() {
    return this._Product;
  }


  get Tank_index() {
    return this._Tank_index;
  }

  get Capacity() {
    return this._Capacity;
  }

  get UOM() {
    return this._UOM;
  }

  get Shape() {
    return this._Shape;
  }

  get LL_Level() {
    return this._LL_Level;
  }

  get L_Level() {
    return this._L_Level;
  }

  get HH_Level() {
    return this._HH_Level;
  }

  get H_Level() {
    return this._H_Level;
  }

  get Reorder() {
    return this._Reorder;
  }

  get Leak() {
    return this._Leak;
  }

  get ControllerType() {
    return this._ControllerType;
  }

  get ControlMode() {
    return this._ControlMode;
  }


  ProceedTosubmit() {

    var messedUp;
    var $this = this;

    var result = $this.compulsory_prop.every(function(currentValue) {

      if (!$this['_' + currentValue]) {
        messedUp = currentValue;
        return false;
      } else {
        return true;
      }

    });

    if (!result) {

      Notify.error(messedUp + " Validation flagged an error");
      return;
    }


    var data = {
      Name: this._Name,
      Product: this._Product,
      Tank_index: this._Tank_index,
      Capacity: this._Capacity,
      UOM: this._UOM,
      Shape: this._Shape,
      LL_Level: this._LL_Level,
      L_Level: this._L_Level,
      HH_Level: this._HH_Level,
      H_Level: this._H_Level,
      Leak: this._Leak,
      Reorder: this._Reorder,
      Controller_polling_address: this._Controller_polling_address,
      Site_id: this._Site,
      Tank_controller: this._ControllerType,
      Control_mode: this._ControlMode,
      // CalibrationChart: this._calibrationChart,
      Offset: this._offset,
      Po4: this._po4,
      Density: this._Density,
      Anomaly_period: this._Anomaly_period,
      Anomaly_volume: this._Anomaly_volume,
      Tank_height: this._Tank_height,
      Tank_Note:this._Tank_Note,
    };
    if(this._calibrationChart){
      data['CalibrationChart'] = this._calibrationChart;
    }
    return this.CreateTank(data);

  }

  set po4(value) {
    if (value) {

      this._po4 = value;

    }
  }

  set Density(value) {
    if (value) {

      this._Density = value;

    }
  }

  set Anomaly_volume(value) {
    if (value) {

      this._Anomaly_volume = value;

    }
  }

  set Anomaly_period(value) {
    if (value) {

      this._Anomaly_period = value;

    }
  }

  set Tank_height(value) {
    if (value) {

      this._Tank_height = value;

    }
  }

  set Tank_Note(value) {
    if (value) {

      this._Tank_Note = value;

    }
  }

  set calibrationChart(value) {
    if (value) {

      this._calibrationChart = value;

    }
  }

  set offset(value) {
    if (value) {

      this._offset = parseFloat(value);

    }

  }

  set Name(value) {
    value = value.trim();
    if (value) {

      this._Name = value;

    } else {

      Notify.error(" Name Input is empty");
      this._Name = '';
    }

  }

  set Product(value) {

    if (UtilityClass.isObjectLike(value)) {
      this._Product = value.Product_id;
    } else {

      Notify.error("Product Selection Input is empty");
      this._Product = '';
    }

  }



  set Tank_index(value) {

    if (value) {
      this._Tank_index = value;
    } else {

      Notify.error("Tank_index Selection Input is empty");
      this._Tank_index = '';
    }

  }



  set Capacity(value) {

    if (value) {
      this._Capacity = value;
    } else {

      Notify.error("Capacity Selection Input is empty");
      this._Capacity = '';
    }

  }

  set UOM(value) {

    if (UtilityClass.isObjectLike(value)) {
      this._UOM = value.id;
    } else {

      Notify.error("UOM Selection Input is empty");
      this._UOM = '';
    }

  }


  set Shape(value) {

    if (UtilityClass.isObjectLike(value)) {
      this._Shape = value.id;
    } else {

      Notify.error("Shape Selection Input is empty");
      this._Shape = '';
    }

  }


  set LL_Level(value) {

    if (value) {
      this._LL_Level = value;
    } else {

      Notify.error("LL_Level Selection Input is empty");
      this._LL_Level = '';
    }

  }


  set L_Level(value) {

    if (value) {
      this._L_Level = value;
    } else {

      Notify.error("L_Level Selection Input is empty");
      this._L_Level = '';
    }

  }

  set HH_Level(value) {

    if (value) {
      this._HH_Level = value;
    } else {

      Notify.error("HH_Level Selection Input is empty");
      this._HH_Level = '';
    }

  }


  set H_Level(value) {

    if (value) {
      this._H_Level = value;
    } else {

      Notify.error("H_Level Selection Input is empty");
      this._H_Level = '';
    }

  }

  set Reorder(value) {

    if (value) {
      this._Reorder = value;
    } else {

      Notify.error("Reorder Selection Input is empty");
      this._Reorder = '';
    }

  }

  set Leak(value) {

    if (value) {
      this._Leak = value;
    } else {

      Notify.error("Leak Selection Input is empty");
      this._Leak = '';
    }

  }

  set Controller_polling_address(value) {

    if (value && (value != 0)) {
      this._Controller_polling_address = value;
    } else {

      Notify.error("Controller polling address Selection Input is empty");
      this._Controller_polling_address = '';
    }

  }



  set Site(value) {

    if (UtilityClass.isObjectLike(value)) {
      this._Site = value.Site_id;
    } else {

      Notify.error("Site Selection Input is empty");
      this._Site = '';
    }

  }

  set ControllerType(value) {

    if (UtilityClass.isObjectLike(value)) {
      if (value.hasOwnProperty('slug')) {
        this._ControllerType = value.slug;
      }else{
        this._ControllerType = value.id;
      }
    } else {

      Notify.error("ControllerType Selection Input is empty");
      this._ControllerType = '';
    }

  }

  set ControlMode(value) {

    if (UtilityClass.isObjectLike(value)) {
      this._ControlMode = value.id;
    } else {

      Notify.error("Control mode Selection Input is empty");
      this._ControlMode = '';
    }

  }



}

export default RegisterTank;
