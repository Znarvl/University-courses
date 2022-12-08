package se.liu.ida.simja649.tddd78.lab3;

import se.liu.ida.simja649.tddd78.se.liu.ida.simja649.tddd78.lab2.Person;

public class Queue extends ListManipulator
{
    //ArrayList<Person> index;

    public Queue() {
	super();
    }


    public void enqueue(Person p) {
	elements.add(p);
    }

    public Person dequeue() {
	int index = 0;
	return elements.remove(index);
    }

}
