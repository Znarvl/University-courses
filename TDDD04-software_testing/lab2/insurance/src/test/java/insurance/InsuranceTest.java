package insurance;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class InsuranceTest {
	
	
		private insurance.InsuranceCalculator insurance;
		private insurance.Client client;
		private insurance.Car car1;
		private insurance.Car car2;



		@BeforeEach
		public void setUp() {
			insurance = new insurance.InsuranceCalculator();
			client = new Client();
			client.age = 30;
			client.isGoldMember = true;
			client.yearLicence = 5;
			client.numberAccidents = 0;
			car1 = new Car();
			car1.id = 1;
			car1.isRed = false;
			client.cars.add(car1);
			}
		
		
		// getClientDeductible tests
		
		//Invalid tests
		@Test
		public void testDeductibleException1() throws InvalidClientData {		
			client.numberAccidents = -1;
			Assertions.assertThrows(InvalidClientData.class, ()->insurance.getClientDeductible(client));
		}
		@Test
		public void testDeductibleException2() throws InvalidClientData {		
			client.age = 17;
			Assertions.assertThrows(InvalidClientData.class, ()->insurance.getClientDeductible(client));
		}
		
		@Test
		public void testDeductibleException3() throws InvalidClientData {		
			client.yearLicence = -1;
			Assertions.assertThrows(InvalidClientData.class, ()->insurance.getClientDeductible(client));
		}
		@Test
		public void testDeductibleException4() throws InvalidClientData {		
			client.yearLicence = 5;
			client.age = 22;
			Assertions.assertThrows(InvalidClientData.class, ()->insurance.getClientDeductible(client));
		}
		
		
		
		//Valid tests
		@Test
		public void testDeductibleExceptionValid1() throws InvalidClientData {		
			client.yearLicence = 2;
			client.age = 30;
			client.isGoldMember = true;
			client.numberAccidents = 0;
			Assertions.assertTrue(insurance.getClientDeductible(client) == 5000);
		}
		
		@Test
		public void testDeductibleExceptionValid2() throws InvalidClientData {		
			client.yearLicence = 2;
			client.age = 31;
			client.isGoldMember = true;
			client.numberAccidents = 2;
			Assertions.assertTrue(insurance.getClientDeductible(client) == 5000);
		}
		
		@Test
		public void testDeductibleExceptionValid3() throws InvalidClientData {		
			client.yearLicence = 2;
			client.age = 30;
			client.isGoldMember = true;
			client.numberAccidents = 4;
			Assertions.assertTrue(insurance.getClientDeductible(client) == 15000);
		}
		
		@Test
		public void testDeductibleExceptionValid4() throws InvalidClientData {		
			client.yearLicence = 2;
			client.age = 30;
			client.isGoldMember = false;
			client.numberAccidents = 2;
			Assertions.assertTrue(insurance.getClientDeductible(client) == 7500);
		}
		
		@Test
		public void testDeductibleExceptionValid5() throws InvalidClientData {		
			client.yearLicence = 2;
			client.age = 30;
			client.isGoldMember = false;
			client.numberAccidents = 2;
			Assertions.assertTrue(insurance.getClientDeductible(client) == 7500);
		}
		
		@Test
		public void testDeductibleExceptionValid6() throws InvalidClientData {		
			client.yearLicence = 2;
			client.age = 29;
			client.isGoldMember = false;
			client.numberAccidents = 2;
			Assertions.assertTrue(insurance.getClientDeductible(client) == 10500);
		}
		@Test
		public void testDeductibleExceptionValid7() throws InvalidClientData {		
			client.yearLicence = 5;
			client.age = 25;
			client.isGoldMember = false;
			client.numberAccidents = 2;
			Assertions.assertTrue(insurance.getClientDeductible(client) == 7500);
		}
		
		@Test
		public void testDeductibleExceptionValid8() throws InvalidClientData {		
			client.yearLicence = 0;
			client.age = 18;
			client.isGoldMember = true;
			client.numberAccidents = 2;
			Assertions.assertTrue(insurance.getClientDeductible(client) == 8000);
		}
		
		
		
		
		//MonthlyInsuranceCost tests
		//Invalid tests
		@Test
		public void testMonthlyException1() throws InvalidClientData {
			client.age = 17;
			Assertions.assertThrows(InvalidClientData.class, ()->insurance.monthlyInsuranceCost(client));
			
		}
		@Test
		public void testMonthlyException2() throws InvalidClientData {	
			client.yearLicence = -1;
			Assertions.assertThrows(InvalidClientData.class, ()->insurance.monthlyInsuranceCost(client));
			
		}
		@Test
		public void testMonthlyException3() throws InvalidClientData {
			client.cars.remove(car1);
			Assertions.assertThrows(InvalidClientData.class, ()->insurance.monthlyInsuranceCost(client));
			
		}
		@Test
		public void testMonthlyException4() throws InvalidClientData {
			client.yearLastAccident = -1;
			Assertions.assertThrows(InvalidClientData.class, ()->insurance.monthlyInsuranceCost(client));
			
		}
		
		//Valid tests
		@Test
		public void testMonthlyExceptionValid1() throws InvalidClientData {		
			client.age = 25;
			client.yearLicence = 3;
			Assertions.assertTrue(insurance.monthlyInsuranceCost(client) == 720);
		}
		
		//Valid tests
		@Test
		public void testMonthlyExceptionValid2() throws InvalidClientData {		
			client.age = 25;
			client.yearLicence = 3;
			client.isGoldMember = false;
			client.yearLastAccident = 1;
			Assertions.assertTrue(insurance.monthlyInsuranceCost(client) == 800);
		}
		@Test
		public void testMonthlyExceptionValid3() throws InvalidClientData {		
			client.age = 25;
			client.yearLicence = 3;
			client.isGoldMember = false;
			client.yearLastAccident = 1;
			car1.isRed = true;
			Assertions.assertTrue(insurance.monthlyInsuranceCost(client) == 900);
		}
		@Test
		public void testMonthlyExceptionValid4() throws InvalidClientData {		
			client.age = 25;
			client.yearLicence = 3;
			client.isGoldMember = false;
			client.yearLastAccident = 1;
			car2 = new Car();
			car2.id = 2;
			car2.isRed = false;
			client.cars.add(car2);
			Assertions.assertTrue(insurance.monthlyInsuranceCost(client) == 1000);
		}
		
		@Test
		public void testMonthlyExceptionValid5() throws InvalidClientData {		
			client.age = 31;
			client.yearLastAccident = 0;	
			Assertions.assertTrue(insurance.monthlyInsuranceCost(client) == 630);
		}
		@Test
		public void testMonthlyExceptionValid6() throws InvalidClientData {		
			client.age = 31;
			client.yearLastAccident = 0;
			client.isGoldMember = false;
			Assertions.assertTrue(insurance.monthlyInsuranceCost(client) == 630);
		}
		
		@Test
		public void testMonthlyExceptionValid7() throws InvalidClientData {		
			client.age = 31;
			client.yearLastAccident = 1;
			client.isGoldMember = false;
			Assertions.assertTrue(insurance.monthlyInsuranceCost(client) == 700);
		}
		
		@Test
		public void testMonthlyExceptionValid8() throws InvalidClientData {		
			client.age = 31;
			car2 = new Car();
			car2.id = 2;
			car2.isRed = true;
			client.cars.add(car2);
			Assertions.assertTrue(insurance.monthlyInsuranceCost(client) == 900);
		}
		@Test
		public void testMonthlyExceptionValid9() throws InvalidClientData {		
			client.age = 31;
			car2 = new Car();
			car2.id = 2;
			car2.isRed = false;
			client.cars.add(car2);
			Assertions.assertTrue(insurance.monthlyInsuranceCost(client) == 810);
		}
		
		
		

		
		
		
}
