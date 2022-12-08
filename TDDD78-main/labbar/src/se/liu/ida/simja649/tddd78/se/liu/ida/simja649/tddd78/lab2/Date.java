package se.liu.ida.simja649.tddd78.se.liu.ida.simja649.tddd78.lab2;

public class Date
{
    private int year;
    private Month month;
    private int day;

    public Date(int year, Month month, int day) {
	this.year = year;
	this.month = month;
	this.day = day;
    }


    public int getYear() {
	return year;
    }

    public Month getMonth() {
	return month;
    }

    public int getDay() {
	return day;
    }

    @Override public String toString() {
	return " Datum " + this.day + " Månad " + this.month + " År " + this.year;
    }
}
