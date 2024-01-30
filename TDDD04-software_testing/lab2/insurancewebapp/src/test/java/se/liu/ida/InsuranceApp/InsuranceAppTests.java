package se.liu.ida.InsuranceApp;

import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.hamcrest.CoreMatchers.containsString;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import se.liu.ida.InsuranceApp.services.ClientDataManagementService;
import se.liu.ida.InsuranceApp.services.InsuranceServiceImpl;

@SpringBootTest
@ExtendWith(MockitoExtension.class)
@ActiveProfiles("mockInsuranceService") // we can choose between different test configurations for different layers
@AutoConfigureMockMvc
public class InsuranceAppTests {
	
	/**
	 * We are going to mock the mvc layer to simplify the setup
	 */
	@Autowired
	private MockMvc mvc;
	
	@Autowired
	private InsuranceController ic; 

	@Autowired
	private ClientDataManagementService cm;
	
	@BeforeEach
    public void setup() {
        this.mvc = MockMvcBuilders.standaloneSetup(ic).build();
    }
	
	@Test
	public void test_getClientNumber() throws Exception {
		mvc.perform(
				MockMvcRequestBuilders.get("/getClientNumber")).andExpect(status().isOk());
				
	}
	
	@Test 
	public void test_getClientInfo() throws Exception {
		mvc.perform(
				MockMvcRequestBuilders.get("/getClientData", 2)).andExpect(status().isOk());
				
	}
	
	@Test 
	public void test_getMothnlyRate() throws Exception {
		mvc.perform(
				MockMvcRequestBuilders.get("/getClientMonthlyRate", 2)).andExpect(status().isOk()).andExpect(content().string(containsString("0")));
				
	}
	@Test 
	public void test_getClientDeductible() throws Exception {
		mvc.perform(
				MockMvcRequestBuilders.get("/getClientDeductible", 2)).andExpect(status().isOk()).andExpect(content().string(containsString("0")));
				
	}

}
