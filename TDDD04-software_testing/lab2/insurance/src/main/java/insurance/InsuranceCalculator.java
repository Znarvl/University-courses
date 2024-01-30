package insurance;

public class InsuranceCalculator {
	/**
	 * Calculate the deductible for the client
	 * Base cost is 5000 SEK if the client is above 30 or has had a driving licence for more that 5 years and 8000 SEK otherwise
	 * With every accident for that calendar the deductible increases:
	 * 1 accident 	: by 1000 SEK
	 * 2 accidents  : by 2500 SEK
	 * 3 accidents	: by 4000 SEK
	 * 4 accidents and more by : 10000 SEK
	 * If the client if a gold member, then for the first 2 accidents, there is no increase
	 * but for 3 accidents and more normal rates apply
	 * 
	 * @param clientId
	 * @return the ammount of the deductible
	 * @throws InvalidClientData 
	 */
	int getClientDeductible (Client cl) throws InvalidClientData {
		int deductible;

		if (cl.age >= 30 || cl.yearLicence >= 5 ) {
			deductible = 5000;

		}
		else {
			deductible = 8000;
		}
		// Got to be an easier way to find EC
		if (!cl.isGoldMember) {
				if (cl.numberAccidents == 1) {
					deductible += 1000;
					
				}
				else if (cl.numberAccidents == 2) {
					deductible += 2500;
					
				}
			}
		
		if (cl.numberAccidents == 3) {
			deductible += 4000;
			
		}
		else if (cl.numberAccidents >= 4) {
			deductible += 10000;
			
		}
		
		if (cl.numberAccidents < 0)
			throw new InvalidClientData();
		
		if (cl.age < 18)
			throw new InvalidClientData();
		
		if (cl.yearLicence < 0)
			throw new InvalidClientData();
		
		if (cl.yearLicence >= 5 && cl.age < 23)
			throw new InvalidClientData();
		
		
		return deductible;
	}
	
	
	/**
	 * Calculate the monthly cost for the service for the client
	 * First year rate is 500SEK if the client is above 30 or has had a driving licence for more that 5 years and 600 SEK otherwise
	 * If the car is red the cost goes up by 100SEK
	 * Each additional car adds 200 SEK unless it is red then it adds 300SEK
	 * After the first year, there is a 10% discount if there were 0 accidents that year or if the client is a gold member
	 * @param clientId
	 * @return monthCostInt
	 * @throws InvalidClientData 
	 */
	int monthlyInsuranceCost(Client cl) throws InvalidClientData {
		double monthCost;
		if (cl.yearLicence >=5 || cl.age >= 30) {
			monthCost = 500;	
		}
		else {
			monthCost = 600;
		}
		for (int i = 0; i < cl.cars.size() ; i++) {

			if (cl.cars.get(i).isRed) {
				monthCost += 300;
			}
			else {
				monthCost += 200;
			}
		}
		if (cl.yearLastAccident == 0 || cl.isGoldMember) {
			monthCost = Math.floor(monthCost * 0.9);
		}

		if (cl.age < 18)
			throw new InvalidClientData();
		if (cl.yearLicence < 0)
			throw new InvalidClientData();
		if (cl.yearLastAccident < 0)
			throw new InvalidClientData();
		if (cl.cars.size() < 1)
			throw new InvalidClientData();
		
		int monthCostInt = (int)monthCost; //recast to int because multiply with 0.9 converts to double	
		return monthCostInt;
	}
}
