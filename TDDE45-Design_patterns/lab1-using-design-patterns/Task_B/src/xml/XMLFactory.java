package xml;

import domain.Adapter;

public class XMLFactory {

    private String fileName;

    public  XMLFactory(String fileName){
        this.fileName = fileName;
    }

    public  void buildTarget(String targetName){
        Adapter xml = new XMLAdapter(this.fileName);
        xml.buildTarget(targetName);
    }

}
