package se.liu.ida.simja649.tddd78.se.liu.ida.simja649.tddd78.lab2;

public class TimeSpan
{
    private TimePoint start;
    private TimePoint end;

    public TimeSpan(TimePoint start, TimePoint end) {
	this.start = start;
	this.end = end;
    }

    public TimePoint getStart() {
	return start;
    }

    public TimePoint getEnd() {
	return end;
    }

    @Override public String toString() {
	return this.start + " | " + this.end;
    }
}

