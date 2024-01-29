import TankClass from '@/Models/TankClass';
import store from '@/store/index';

import UserSession from '@/MyClasses/UserSession';

class ManipulateTank extends TankClass{

	/* jshint ignore:start */
	ReOrderedUsers = []
	active = 1
	inactive = 0
	/* jshint ignore:end */

	formatAllTanks(tanklist){

		var $this = this;
		var NewList = [];
		
		tanklist.forEach(function(element) {
			if (!element.Site){
				//console.log(element);
			}
			let holder = {};
			let Final;
			holder.Name = element.Name;
			holder["Controller Polling Address"] = element.Controller_polling_address;
			holder["Tank Index"] = element.Tank_index;
			holder["Tank Shape"] = $this.findSHAPE(element.Shape);
			holder["Tank Capacity"] = element.Capacity;
			holder["Unit of Measurement"] = $this.findUOM(element.UOM);
			holder["Re-order level"] = element.Reorder;
			holder['Site Name']= element.Site.Name;
			holder['Controller Type']= element.Tank_controller;
			holder["Tank Status"] = $this.formartTankStatus(element.Status);

			//var Company = $this.CompanyClass.retriveAcompany(element.Site.Company);
			holder.Company= element.Site.Company.Name
			// ? element.Site.Company.Name: "none";
			holder["Date Created"] = element.Created_at;
			
			/* jshint ignore:start */
			//Sublime jshint does not notices spread operators
			Final = {...holder,...element};
			/* jshint ignore:end */
		  NewList.push(Final);
		});
		// console.log(this.ReOrderedUsers);
		//return tanklist;

		return NewList;

	}




	TableFields(){
	var keys =   [
			        {key: 'Name'},
			        {key: 'Controller Polling Address'},
			        {key: 'Tank Index'},
			        {key: 'Tank Capacity'},
			        {key: 'Controller Type'},
			        {key: 'Unit of Measurement'},
			        {key: 'Re-order level'},
			        {key: 'Company'},
			        {key: 'Site Name'},
			        {key: 'Date Created'},
					{key: 'Tank Status'},
			       
		      ];

        //Allow users to only edit or deactivate if they are super admins
		if (UserSession.ISsuperadmin() || UserSession.IScompanyadmin()||UserSession.ISE360admin()) {
			let added = {key: 'Actions'};
			keys.push(added);
		}

		return keys;
	}


	formartStatus(status){
		if (status == 1) {
			return 'active';
		}else{
			return 'in-active';
		}
	}

	formartTankStatus(status){
		if (status) {
			return 'active';
		}else{
			return 'in-active';
		}
	}
}

export default ManipulateTank;