package se.liu.ida.simja649.tddd78.lab3;

import se.liu.ida.simja649.tddd78.se.liu.ida.simja649.tddd78.lab2.Person;

import java.time.LocalDate;

public class TestQueue
{
    public static void main(String[] args) {
	Queue q1 = new Queue();
	Person Simon = new Person("Simon", LocalDate.of(1996, 3, 25));
	Person Dennis = new Person("Dennis", LocalDate.of(1992, 5, 30));
	Person Erik = new Person("Erik", LocalDate.of(1992, 5, 30));
	Person Kalle = new Person("Kalle", LocalDate.of(1992, 5, 30));
	Person Markus = new Person("Markus", LocalDate.of(1992, 5, 30));
	q1.enqueue(Simon);
	q1.enqueue(Dennis);
	q1.enqueue(Erik);
	q1.enqueue(Kalle);
	q1.enqueue(Markus);
	while (q1.isEmpty() == false) {
	    System.out.println(q1.dequeue());

	}
    }
}
