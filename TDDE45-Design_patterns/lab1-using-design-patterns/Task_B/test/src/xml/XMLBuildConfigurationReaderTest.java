package xml;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import domain.Project;

public class XMLBuildConfigurationReaderTest {

	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
	}

	@AfterClass
	public static void tearDownAfterClass() throws Exception {
	}

	private XMLBuildConfigurationReader confReader;

	@Before
	public void setUp() throws Exception {
		confReader = new XMLBuildConfigurationReader("build.xml");
	}

	@After
	public void tearDown() throws Exception {
	}

	@Test
	public final void test() {
		final Project project = confReader.getProject();
		assertNotNull(project);
		assertEquals("MyProject", project.getName());
		assertEquals(".", project.getBasedir());
		//assertNotNull(project.getTargets());
	}

}
