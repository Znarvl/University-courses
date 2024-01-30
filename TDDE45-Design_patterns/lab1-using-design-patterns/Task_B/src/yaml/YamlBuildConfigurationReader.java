package yaml;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;

import net.sourceforge.yamlbeans.YamlException;
import net.sourceforge.yamlbeans.YamlReader;
import domain.BuildConfig;
import domain.Project;

public class YamlBuildConfigurationReader  {

	private YamlReader yamlReader;

	public YamlBuildConfigurationReader(String fileName) {
		try {
			yamlReader = new YamlReader(new FileReader(new File(fileName)));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
	}

	public BuildConfig getBuildConfig() {
		BuildConfig config = null;
		try {
			config = yamlReader.read(BuildConfig.class);
			
		} catch (YamlException e) {
			e.printStackTrace();
		}

		return config;
	}

}
