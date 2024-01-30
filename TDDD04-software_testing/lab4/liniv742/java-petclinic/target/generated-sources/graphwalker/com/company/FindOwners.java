// Generated by GraphWalker (http://www.graphwalker.org)
package com.company;

import org.graphwalker.java.annotation.Model;
import org.graphwalker.java.annotation.Vertex;
import org.graphwalker.java.annotation.Edge;

@Model(file = "com/company/PetClinic.json")
public interface FindOwners {

    @Vertex()
    void v_Owners();

    @Edge()
    void e_AddOwner();

    @Vertex()
    void v_FindOwners();

    @Edge()
    void e_Search();

    @Edge()
    void e_FindOwners();

    @Vertex()
    void v_NewOwner();
}
