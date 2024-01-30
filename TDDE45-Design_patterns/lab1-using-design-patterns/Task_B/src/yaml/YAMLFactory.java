package yaml;

import domain.Adapter;

public class YAMLFactory {
    private String fileName;

    public YAMLFactory(String fileName){
        this.fileName = fileName;
    }
    public void buildTarget(String targetName){
       Adapter yaml = new YamlAdapter(this.fileName);
       yaml.buildTarget(targetName);

    }
}
