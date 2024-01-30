

import java.util.Collection;
import java.util.Iterator;

public class Enumerable<T> implements Iterable<T> {

	private Iterator<T> iterator;

	public Enumerable(Collection<T> collection) {
		this.iterator = collection.iterator();
	}

	Enumerable<T> where(IPredicate<T> predicate) {
		Iterator<T> oldIterator = iterator;
		this.iterator = new Iterator<T>() {

			@Override
			public boolean hasNext() {
				return oldIterator.hasNext();
			}

			@Override
			public T next() {
				T item = oldIterator.hasNext() ? oldIterator.next() : null;
				while (oldIterator.hasNext() && !predicate.accept(item)) {
					item = oldIterator.next();
				}
				return item;
			}
		};
		return this;
	}

	@Override
	public Iterator<T> iterator() {
		return iterator;
	}

	void forEach(IAction<T> action) {
		while (iterator.hasNext()) {
			T t = (T) iterator.next();
			action.perform(t);
		}
	}

}
