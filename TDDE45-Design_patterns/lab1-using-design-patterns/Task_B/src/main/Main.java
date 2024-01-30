package main;

import domain.Factory;
import xml.XMLFactory;
import yaml.YAMLFactory;


public class Main {
	
	public static void main(String[] args) {

		final String target = "dist";

		Factory factory = new Factory();

		XMLFactory xml = factory.xml("build.xml");
		xml.buildTarget(target);

		YAMLFactory yaml = factory.yaml("build.yaml");
		yaml.buildTarget(target);


	}
}


