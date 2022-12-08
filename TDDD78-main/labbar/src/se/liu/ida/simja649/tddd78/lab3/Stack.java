package se.liu.ida.simja649.tddd78.lab3;

import se.liu.ida.simja649.tddd78.se.liu.ida.simja649.tddd78.lab2.Person;

public class Stack extends ListManipulator
{
    //ArrayList<Person> index;

    public Stack() {
	super();
    }

    public void push(Person p) {
	elements.add(p);
    }

    public Person pop() {
	int index = elements.size() - 1;
	return elements.remove(index);
    }


}
