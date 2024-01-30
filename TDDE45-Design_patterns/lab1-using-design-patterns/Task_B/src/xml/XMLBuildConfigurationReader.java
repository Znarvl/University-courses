package xml;

import java.io.File;
import java.io.IOException;
import java.util.Iterator;
import java.util.Optional;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import domain.Project;
import domain.Target;

public class XMLBuildConfigurationReader {

	
	private final class NodeIterator implements Iterator<Node> {
		private final NodeList childNodes;
		int i = 0;

		private NodeIterator(NodeList childNodes) {
			this.childNodes = childNodes;
		}

		@Override
		public boolean hasNext() {
			return i < childNodes.getLength();
		}

		@Override
		public Node next() {
			Node n = childNodes.item(i);
			i++;
			return n;
		}
	}

	private Element docElement;

	
	public XMLBuildConfigurationReader(String fileName) {
		DocumentBuilderFactory f = DocumentBuilderFactory.newInstance();
		try {
			DocumentBuilder docBuilder = f.newDocumentBuilder();
			Document doc = docBuilder.parse(new File(fileName));
			docElement = doc.getDocumentElement();
		} catch (ParserConfigurationException | SAXException | IOException e) {
			e.printStackTrace();
		}
	}

	private String getAttributeValue(Element elt, String attributeName) {
		return elt.getAttributes().getNamedItem(attributeName).getNodeValue();
	}
	
	public Project getProject() {
		Project project = new Project();
		project.setName(getAttributeValue(docElement,"name"));
		project.setBasedir(getAttributeValue(docElement,"basedir"));
		NodeList childNodes = docElement.getChildNodes();
		for (int i = 0; i < childNodes.getLength(); i++) {
			Node node = childNodes.item(i);
			if (node.getNodeName().equals("target")) {
				Target target = new Target();
				target.setName(node.getAttributes().getNamedItem("name").getNodeValue());
				Node dep = node.getAttributes().getNamedItem("depends");
				project.addTarget(target);
				if (dep != null) {
					Optional<Target> optionalDep = project.getTargetByName(dep.getNodeValue());
					if (optionalDep.isPresent()) {
						Target targetDependency = optionalDep.get();
						target.addDependency(targetDependency);
					} else {
						System.err.println("invalid target: "+dep.getLocalName());
					}
				}
			}
		}
		return project;
	}
}
