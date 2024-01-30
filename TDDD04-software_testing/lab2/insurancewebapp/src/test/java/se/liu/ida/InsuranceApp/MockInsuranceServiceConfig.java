package se.liu.ida.InsuranceApp;



import org.mockito.Mockito;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.context.annotation.Profile;

import se.liu.ida.InsuranceApp.data.ClientProfile;
import se.liu.ida.InsuranceApp.services.InsuranceService;

@Profile("mockInsuranceService")
@Configuration
public class MockInsuranceServiceConfig {
	
	@Bean
	@Primary
	public InsuranceService insuranceService() {
		InsuranceService is =  Mockito.mock(InsuranceService.class);
		ClientProfile client = new ClientProfile(1,"Doe", "John", 1990, 2020);
			
	    
		/** Add mocked behavior */
		 Mockito.when(is.clientNumber())
	       	.thenReturn(1);
		 
		 Mockito.when(is.isClientGoldMember(1)).thenReturn(false);
		 
		 Mockito.when(is.registerNewMember("Doe", "Johan", 1999, 2020)).thenReturn(true);
		 
		 Mockito.when(is.addNewCarToMember(1, "Red", 1990)).thenReturn(true);
		 
		 Mockito.when(is.getClientProfile(1)).thenReturn(client);
		 
		 Mockito.when(is.registerNewAccident(1)).thenReturn(0);
		 
		 Mockito.when(is.getClientDeductible(1)).thenReturn(7000);
		 
		 Mockito.when(is.MonthlyInsuranceCost(1)).thenReturn(500);
	 
		 return is;
	}

}
