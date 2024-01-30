package se.liu.ida.tdde45.house;

public class Bedroom {
	private final Bed bed;
	private final Dresser dresser;
	
	public Bedroom(Bed bed, Dresser dresser) {
		this.bed = bed;
		this.dresser = dresser;
	}

	public Bed getBed() {
		return bed;
	}
	
	public Dresser getDresser() {
		return dresser;
	}
}
