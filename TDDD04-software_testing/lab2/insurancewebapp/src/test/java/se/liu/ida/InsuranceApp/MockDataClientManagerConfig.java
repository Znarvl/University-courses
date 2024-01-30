package se.liu.ida.InsuranceApp;

import java.util.HashMap;
import java.util.Vector;

import org.mockito.Mockito;
import org.mockito.invocation.InvocationOnMock;
import org.mockito.stubbing.Answer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.context.annotation.Profile;

import se.liu.ida.InsuranceApp.data.ClientProfile;
import se.liu.ida.InsuranceApp.services.ClientDataManagementService;

@Profile("mockClientManager")
@Configuration
public class MockDataClientManagerConfig {
	
	@Bean
	@Primary
	public ClientDataManagementService clientDataManagementService() {
		ClientDataManagementService cs =  Mockito.mock(ClientDataManagementService.class);	
		ClientProfile client = new ClientProfile(1, "Doe", "John", 1999, 2020);
	    
		/** Add mocked behavior */
		 Mockito.when(cs.findById(1))
	       	.thenReturn(client);
		 
		 Mockito.when(cs.updateClientProfile(1, client)).thenReturn(true);
		 
		 Mockito.when(cs.addClientProfile(client)).thenReturn(true);		 
		 //add more
		 
		 Mockito.when(cs.removeClientProfile(1))
		 	.thenReturn(true);
		 
		 return cs;
	}

}
