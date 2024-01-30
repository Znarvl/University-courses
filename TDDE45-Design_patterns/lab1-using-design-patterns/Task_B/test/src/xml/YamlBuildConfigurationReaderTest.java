package xml;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import static org.junit.Assert.*;

import yaml.YamlBuildConfigurationReader;
import domain.BuildConfig;

public class YamlBuildConfigurationReaderTest {

	@BeforeClass
	public static void setUpBeforeClass() throws Exception {
	}

	@AfterClass
	public static void tearDownAfterClass() throws Exception {
	}

	private YamlBuildConfigurationReader yamlReader;

	@Before
	public void setUp() throws Exception {
		yamlReader = new YamlBuildConfigurationReader("build.yaml");
	}

	@After
	public void tearDown() throws Exception {
	}

	@Test
	public final void test() {
		BuildConfig buildConfig = yamlReader.getBuildConfig();
		assertEquals("MyProject", buildConfig.getProject().getName());
	}

}
