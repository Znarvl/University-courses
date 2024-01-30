public class StateAndReward {

	
	/* State discretization function for the angle controller */
	public static String getStateAngle(double angle, double vx, double vy) {

		/* TODO: IMPLEMENT THIS FUNCTION */

		String state = "Angle: " +  discretize(angle, 15, -Math.PI, Math.PI);
		System.out.println(state);
		
		return state;
	}

	/* Reward function for the angle controller */
	public static double getRewardAngle(double angle, double vx, double vy) {

		/* TODO: IMPLEMENT THIS FUNCTION */
		
		double reward = discretize(angle, 70, -Math.PI, Math.PI) -  discretize(angle, 70, 0, Math.PI);
		System.out.println("Reward: " + reward);
		
		return reward;
	}

	/* State discretization function for the full hover controller */
	public static String getStateHover(double angle, double vx, double vy) {

		/* TODO: IMPLEMENT THIS FUNCTION */

		String state = "Angle: " +  discretize(angle, 15, -Math.PI, Math.PI) +
				"X-Velocity: " + discretize(vx, 10, -10, 10) + 
				"Y-Velocity: " + discretize(vy, 15, -5, 15) ;
		
		return state;
	}

	/* Reward function for the full hover controller */
	public static double getRewardHover(double angle, double vx, double vy) {

		/* TODO: IMPLEMENT THIS FUNCTION */
		double rewardAngle = 0;
		if (Math.abs(angle) >= 0.5) {
		
			rewardAngle = discretize(angle, 40, -Math.PI, Math.PI) -  discretize(angle, 40, 0, Math.PI);
		}
		else {
			rewardAngle = 40;
		}
		
		double rewardXVelocity = 0;
		
		if (Math.abs(vx) >= 0.5) {
			rewardXVelocity = 5 - Math.abs(vx);
		}
		else {
			rewardXVelocity = 30;
		}
		
		double rewardYVelocity = 0;
		if (Math.abs(vy) >= 1) {
			if (vy > 0) {
				rewardYVelocity = 25 / vy;
			}
			else {
				rewardYVelocity = vy * 4;
			}
		}
		else {
			rewardYVelocity = 40;
		}
		
		
		
		
		double reward = rewardAngle + rewardXVelocity + rewardYVelocity;
		
		System.out.println(vy);
		System.out.println("RA: " + rewardAngle + "  RX: " + rewardXVelocity + "  RY: " + rewardYVelocity + "  Rtot: " + reward);

		return reward;
	}

	// ///////////////////////////////////////////////////////////
	// discretize() performs a uniform discretization of the
	// value parameter.
	// It returns an integer between 0 and nrValues-1.
	// The min and max parameters are used to specify the interval
	// for the discretization.
	// If the value is lower than min, 0 is returned
	// If the value is higher than min, nrValues-1 is returned
	// otherwise a value between 1 and nrValues-2 is returned.
	//
	// Use discretize2() if you want a discretization method that does
	// not handle values lower than min and higher than max.
	// ///////////////////////////////////////////////////////////
	public static int discretize(double value, int nrValues, double min,
			double max) {
		if (nrValues < 2) {
			return 0;
		}

		double diff = max - min;

		if (value < min) {
			return 0;
		}
		if (value > max) {
			return nrValues - 1;
		}

		double tempValue = value - min;
		double ratio = tempValue / diff;

		return (int) (ratio * (nrValues - 2)) + 1;
	}

	// ///////////////////////////////////////////////////////////
	// discretize2() performs a uniform discretization of the
	// value parameter.
	// It returns an integer between 0 and nrValues-1.
	// The min and max parameters are used to specify the interval
	// for the discretization.
	// If the value is lower than min, 0 is returned
	// If the value is higher than min, nrValues-1 is returned
	// otherwise a value between 0 and nrValues-1 is returned.
	// ///////////////////////////////////////////////////////////
	public static int discretize2(double value, int nrValues, double min,
			double max) {
		double diff = max - min;

		if (value < min) {
			return 0;
		}
		if (value > max) {
			return nrValues - 1;
		}

		double tempValue = value - min;
		double ratio = tempValue / diff;

		return (int) (ratio * nrValues);
	}

}
