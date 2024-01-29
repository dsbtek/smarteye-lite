import TankClass from '@/Models/TankClass';

class EditTankNoteClass extends TankClass{
    _Tank_Note;
    _Tank_id;
  
    get Tank_Note() {
      return this._Tank_Note;
    }

    get Tank_id() {
        return this._Tank_id;
      }
  
    set Tank_Note(value) {
        this._Tank_Note = value;
    }

    set Tank_id(value) {

        if (value) {
          this._Tank_id = value;
        } else {
    
          Notify.error("Tank_id Selection Input is empty");
          this._Reorder = '';
        }
    
      }
  
    ProceedToSubmitnote() {
  
      var data = {
        Tank_id: this._Tank_id,
        Tank_Note:this._Tank_Note,
  
      };
    
      return this.EditTankDB(data);
  
    }
  
  }

export default EditTankNoteClass;