package se.liu.ida.simja649.tddd78.se.liu.ida.simja649.tddd78.lab2;

public class Appointment
{
    private String subject;
    private Date date;
    private TimeSpan timeSpan;

    public Appointment(String subject, Date date, TimeSpan timeSpan) {
	this.subject = subject;
	this.date = date;
	this.timeSpan = timeSpan;
    }

    public String getSubject() {
	return subject;
    }

    public Date getDate() {
	return date;
    }

    public TimeSpan getTimeSpan() {
	return timeSpan;
    }

    @Override public String toString() {
	return "Bokning: " + this.timeSpan + this.date + this.subject;
    }
}
