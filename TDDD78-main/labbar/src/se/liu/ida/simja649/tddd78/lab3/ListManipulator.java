package se.liu.ida.simja649.tddd78.lab3;

import se.liu.ida.simja649.tddd78.se.liu.ida.simja649.tddd78.lab2.Person;

import java.util.ArrayList;
import java.util.List;

public abstract class ListManipulator
{
    protected List<Person> elements = new ArrayList<Person>();

    public ListManipulator() {elements = new ArrayList<>();}

    public boolean isEmpty() {return elements.isEmpty();}

    public int size() {return elements.size();}

    public boolean contains(final Object o) {return elements.contains(o);}

    public void clear() {elements.clear();}
}
