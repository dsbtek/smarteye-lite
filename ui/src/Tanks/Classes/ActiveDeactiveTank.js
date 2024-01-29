
import Notify from '@/MyClasses/Notify';
import TankClass from '@/Models/TankClass';
class ActiveDeactiveTank extends TankClass{

	Toggle(tank_id){
			if (!tank_id) {
				Notify.error("Tank Id must be available");
				return;
			}
		
			return this.ToggleTank(tank_id);


	}

}

export default ActiveDeactiveTank;