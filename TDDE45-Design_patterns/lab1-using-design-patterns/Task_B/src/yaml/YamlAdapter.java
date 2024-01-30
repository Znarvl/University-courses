package yaml;

import domain.Adapter;
import domain.BuildConfig;
import yaml.Compile;
import yaml.YamlBuildConfigurationReader;

public class YamlAdapter implements Adapter {
    private String fileName;

    public YamlAdapter(String fileName) {
        this.fileName = fileName;
    }


    @Override
    public void buildTarget(String targetName) {
        // yaml
        YamlBuildConfigurationReader yamlConfigReader = new YamlBuildConfigurationReader(this.fileName);
        final BuildConfig yamlBuildConfig = yamlConfigReader.getBuildConfig();
        Compile compile = new Compile(yamlBuildConfig, targetName);
        compile.build(1);
    }
}
