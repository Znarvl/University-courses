package se.liu.ida.simja649.tddd78.se.liu.ida.simja649.tddd78.lab2;

import java.util.ArrayList;
import java.util.List;

public class Calendar
{
    private List<Appointment> appointments;

    public Calendar() {
	appointments = new ArrayList<>();
    }

    public void show() {
	//Print out all appointments
	for (Appointment appointment : appointments) {
	    System.out.println(appointment);
	}
    }

    public void book(int year, String month, int day, int startHour, int startMinute, int endHour, int endMinute,
		     String subject)
    {
	//If outside requirements throw error
	if (year < 1970) {
	    throw new IllegalArgumentException("Not valid year");
	} else if (startHour > 23 || startHour < 0 || startMinute > 59 || startMinute < 0) {
	    throw new IllegalArgumentException("Not valid time");

	} else if (startHour >= endHour && startMinute > endMinute) {
	    throw new IllegalArgumentException("Can't travel in time");
	} else if (endHour > 23 || endHour < 0 || endMinute > 59 || endMinute < 0) {
	    throw new IllegalArgumentException("Not valid time");
	} else if (Month.getMonthDays(month) < day || day < 0) {
	    throw new IllegalArgumentException("Not valid day");

	} else if (Month.getMonthNumber(month) == -1) {
	    throw new IllegalArgumentException("Not valid month");
	} else {
	    Month month1 = new Month(month, Month.getMonthNumber(month), Month.getMonthDays(month));
	    Date date = new Date(year, month1, day);
	    TimePoint start = new TimePoint(startHour, startMinute);
	    TimePoint end = new TimePoint(endHour, endMinute);
	    TimeSpan timeSpan = new TimeSpan(start, end);
	    Appointment appointment = new Appointment(subject, date, timeSpan);
	    this.appointments.add(appointment);
	}

    }

    public static void main(String[] args) {
	Calendar book1 = new Calendar();
	book1.book(2005, "Januari", 31, 14, 30, 14, 20, " Äta mat");
	book1.book(2006, "Februari", 25, 13, 30, 20, 30, " Något");
	book1.book(2100, "Mars", 31, 9, 30, 10, 30, " Simma");
	book1.book(2000, "Oktober", 10, 14, 30, 15, 30, " Kåda");
	book1.book(2025, "December", 2, 21, 25, 22, 30, " Spela spel");
	book1.show();


    }
}

