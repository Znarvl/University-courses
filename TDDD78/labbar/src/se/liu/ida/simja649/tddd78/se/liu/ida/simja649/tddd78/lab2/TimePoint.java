package se.liu.ida.simja649.tddd78.se.liu.ida.simja649.tddd78.lab2;

public class TimePoint
{
    private int hour;
    private int minute;

    public TimePoint(int hour, int minute) {
	this.hour = hour;
	this.minute = minute;
    }

    public int getHour() {
	return hour;
    }

    public int getMinute() {
	return minute;
    }

    @Override public String toString() {
        return String.format("%02d:%02d", this.getHour(), this.getMinute());
    }

}
