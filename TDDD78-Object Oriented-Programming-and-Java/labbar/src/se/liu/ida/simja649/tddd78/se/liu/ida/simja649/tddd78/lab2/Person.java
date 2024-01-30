package se.liu.ida.simja649.tddd78.se.liu.ida.simja649.tddd78.lab2;

import java.time.LocalDate;
import java.time.Period;

public class Person
{
    private String name;
    private LocalDate birthDay;

    public Person(String name, LocalDate birthDay) {
	this.name = name;
	this.birthDay = birthDay;
    }

    private int getAge() {
	LocalDate now = LocalDate.now();
	return Period.between(birthDay, now).getYears();
    }

    public static void main(String[] args) {
	Person Simon = new Person("Simon", LocalDate.of(1996, 3, 25));
	Person Dennis = new Person("Dennis", LocalDate.of(1992, 5, 30));
	System.out.println(Simon);
	System.out.println(Dennis);

    }


    @Override public String toString() {
	return name + " " + getAge();
    }
}


