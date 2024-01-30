package xml;

import java.text.MessageFormat;
import java.util.List;
import java.util.Optional;

import domain.Project;
import domain.Target;

public class Build {

	private Project project;
	
	public Build(Project xmlProject) {
		project = xmlProject;
	}

	public void build(int debuglevel, String targetName) {
		if (debuglevel > 0) {
			System.out.println(MessageFormat.format("Building {0}", project.getName()));			
		}
		Optional<Target> target = project.getTargetByName(targetName);
		if (target.isPresent()) {
			final Target actualTarget = target.get();
			buildRecursively(debuglevel, actualTarget);
		} else {
			System.err.println(MessageFormat.format("Invalid target {0}", targetName));
		}
	}

	private void buildRecursively(int debuglevel, final Target actualTarget) {
		List<Target> deps = actualTarget.getDepends();
		if (deps != null) {
			deps.forEach(t -> buildRecursively(debuglevel, t));
		}
		build(debuglevel, actualTarget);
	}

	private void build(int debuglevel, Target t) {
		if (debuglevel > 0) {
	  		System.out.println(MessageFormat.format("Building target {0}",t.getName()));
	 	}	
	}
	
}
