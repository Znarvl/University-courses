package se.liu.ida.simja649.tddd78.lab3;

import se.liu.ida.simja649.tddd78.se.liu.ida.simja649.tddd78.lab2.Person;

import java.time.LocalDate;

public class TestQueueStack
{
    public static void main(String[] args) {
	Stack s1 = new Stack();
	Person Simon = new Person("Simon", LocalDate.of(1996, 3, 25));
	Person Dennis = new Person("Dennis", LocalDate.of(1992, 5, 30));
	Person Erik = new Person("Erik", LocalDate.of(1992, 5, 30));
	Person Kalle = new Person("Kalle", LocalDate.of(1992, 5, 30));
	Person Markus = new Person("Markus", LocalDate.of(1992, 5, 30));
	s1.push(Simon);
	s1.push(Dennis);
	s1.push(Erik);
	s1.push(Kalle);
	s1.push(Markus);
	while (s1.isEmpty() == false) {
	    System.out.println(s1.pop());


	}
    }


}
