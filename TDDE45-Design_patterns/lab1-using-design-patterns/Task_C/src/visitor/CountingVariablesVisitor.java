package visitor;

public class CountingVariablesVisitor extends Visitor {

	int count;

	
	public int getCount() {
		return count;
	}


	@Override
	public void visit(Number exp) {
		// TODO Auto-generated method stub
		
	}


	@Override
	public void visit(Variable exp) {
		count++;
	}


	@Override
	public void visit(Sum exp) {
		// TODO Auto-generated method stub
		
	}


	@Override
	public void visit(Minus exp) {
		// TODO Auto-generated method stub
		
	}


	

}
