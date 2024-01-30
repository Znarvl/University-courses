package xml;

import domain.Adapter;
import domain.Project;


public class XMLAdapter implements Adapter {
    private String fileName;

    public XMLAdapter(String fileName) {
        this.fileName = fileName;
    }

    @Override
    public void buildTarget(String targetName){
        //XML
        XMLBuildConfigurationReader buildConfigurationReader = new XMLBuildConfigurationReader(this.fileName);
        final Project xmlProject = buildConfigurationReader.getProject();
        Build build = new Build(xmlProject);
        build.build(1, targetName);
    }

}
