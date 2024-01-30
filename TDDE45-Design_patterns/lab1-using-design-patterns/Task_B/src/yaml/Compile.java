package yaml;

import java.text.MessageFormat;
import java.util.List;
import java.util.Optional;

import domain.BuildConfig;
import domain.Project;
import domain.Target;

public class Compile {

	private Project project;
	private String targetName;

	public Compile(BuildConfig yamlBuildConfig, String targetName) {
		project = yamlBuildConfig.getProject();
		this.targetName = targetName;
	}

	public void build(int debuglevel) {
		if (debuglevel > 0) {
			System.out.println(project.getDescription());
		}
		Optional<Target> target = project.getTargetByName(targetName);
		int indent = 0;
		if (target.isPresent()) {
			final Target actualTarget = target.get();
			buildRecursively(debuglevel, actualTarget, indent);
		} else {
			System.err.println(MessageFormat.format("Invalid target {0}",
					targetName));
		}
	}

	private void buildRecursively(int debuglevel, final Target actualTarget, int indent) {
		List<Target> deps = actualTarget.getDepends();
		if (deps != null) {
			deps.forEach(t -> buildRecursively(debuglevel, t, indent+1));
		}
		build(debuglevel, actualTarget, indent);
	}

	private void build(int debuglevel, Target t, int indent) {
		for (int i = 0; i < indent; i++) {
			System.out.print(" ");
		}
		if (debuglevel > 0) {
			System.out.println(MessageFormat.format("Building target {0}: ",
					t.getName(), t.getDescription()));
		}
	}

}
