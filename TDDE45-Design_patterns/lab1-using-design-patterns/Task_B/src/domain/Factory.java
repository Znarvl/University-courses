package domain;

import xml.XMLFactory;
import yaml.YAMLFactory;

public class Factory {

    public XMLFactory xml(String fileName){
        return new XMLFactory(fileName);
    }

    public YAMLFactory yaml(String fileName){
        return new YAMLFactory(fileName);
    }

}
