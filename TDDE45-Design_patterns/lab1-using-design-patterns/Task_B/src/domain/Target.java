package domain;

import java.text.MessageFormat;
import java.util.ArrayList;
import java.util.List;

public class Target {

	private String name;
	private String description;
	private List<Target> depends;
	private String tstamp;

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public List<Target> getDepends() {
		return depends;
	}

	public void setDepends(List<Target> depends) {
		this.depends = depends;
	}

	public String getTstamp() {
		return tstamp;
	}

	public void setTstamp(String tstamp) {
		this.tstamp = tstamp;
	}

	public void addDependency(Target targetDependency) {
		if (depends == null) {
			depends = new ArrayList<Target>();
		}
		depends.add(targetDependency);
	}
	
	@Override
	public String toString() {
		return MessageFormat.format("Target {0}, Deps: {1}", name, depends);
	}

}
