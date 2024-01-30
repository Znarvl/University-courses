package sample.plugin;


import org.apache.maven.plugin.AbstractMojo;
import org.apache.maven.plugin.MojoExecutionException;

import org.apache.maven.plugins.annotations.LifecyclePhase;
import org.apache.maven.plugins.annotations.Mojo;
import org.apache.maven.plugins.annotations.Parameter;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;


/**
 * Goal which touches a timestamp file.
 */
@Mojo( name = "create-file", defaultPhase = LifecyclePhase.COMPILE )
public class MyMojo
    extends AbstractMojo
{
    /**
     * Location of the file.
     */
    @Parameter( defaultValue = "${project.build.directory}", property = "outputDir", required = true )
    private File outputDirectory;

    @Parameter( defaultValue = "something.txt", property = "create-file-write", required = true )
    private String name;

    

    public void execute()
        throws MojoExecutionException
    {
        File f = outputDirectory;

        if ( !f.exists() )
        {
            f.mkdirs();
        }

        File touch = new File( f, name );

        FileWriter w = null;

        try
        {
            w = new FileWriter( touch );

            w.write( "I have created a plugin that creates a file and writes to it" );
           
        }
        
        catch ( IOException e )
        {
            throw new MojoExecutionException( "Error creating or reading file " + touch, e );
        }

        finally
        {
            if ( w != null )
            {
                try
                {
                    w.close();
                    
                }
                catch ( IOException e )
                {
                    // ignore
                }
            }
        }
    }
}
