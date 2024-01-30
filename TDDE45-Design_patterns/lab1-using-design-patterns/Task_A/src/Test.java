

import java.text.MessageFormat;
import java.util.ArrayList;

public class Test {

	public static void main(String[] args) {
		final ArrayList<Integer> arrayList = new ArrayList<Integer>();
		arrayList.add(2);
		arrayList.add(4);
		arrayList.add(5);
		arrayList.add(7);

		Enumerable<Integer> enumerable = new Enumerable<>(arrayList);
		Enumerable<Integer> evenNumbers = enumerable
				.where(new IPredicate<Integer>() {

					@Override
					public boolean accept(Integer element) {
						return element % 2 == 0;
					}
				});

		Enumerable<Integer> oddNumbers = enumerable
				.where(new IPredicate<Integer>() {

					@Override
					public boolean accept(Integer element) {
						return element % 2 == 1;
					}
				});
		
		evenNumbers.forEach(new IAction<Integer>() {
			
			@Override
			public void perform(Integer t) {
				System.out.println(MessageFormat.format("Even number {0}", t));
			}
		});
		
		oddNumbers.forEach(new IAction<Integer>() {

			@Override
			public void perform(Integer t) {
				System.out.println(MessageFormat.format("Odd number{0}", t));				
			}
		});
	}

}
