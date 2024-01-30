package domain;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class Project {

	private String description;
	private String name;
	private Target defaultTarget;
	private String basedir;
	private List<Property> properties;
	private List<Target> targets;
	private String src;
	private String build;
	private String dist;


	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public String getSrc() {
		return src;
	}

	public void setSrc(String src) {
		this.src = src;
	}

	public String getBuild() {
		return build;
	}

	public void setBuild(String build) {
		this.build = build;
	}

	public String getDist() {
		return dist;
	}

	public void setDist(String dist) {
		this.dist = dist;
	}

	public List<Target> getTargets() {
		return targets;
	}

	public void setTargets(List<Target> targets) {
		this.targets = targets;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Target getDefaultTarget() {
		return defaultTarget;
	}

	public void setDefaultTarget(Target defaultTarget) {
		this.defaultTarget = defaultTarget;
	}

	public String getBasedir() {
		return basedir;
	}

	public void setBasedir(String basedir) {
		this.basedir = basedir;
	}

	public List<Property> getProperties() {
		return properties;
	}

	public void setProperties(List<Property> properties) {
		this.properties = properties;
	}

	@Override
	public String toString() {
		return "[Project: "+getName()+"]";
	}

	public Optional<Target> getTargetByName(String nodeName) {
		return targets.stream().filter(t -> t.getName().equals(nodeName)).findFirst();
	}

	public void addTarget(Target target) {
		if (targets == null) {
			targets = new ArrayList<Target>();
		}
		targets.add(target);
	}
	
}
