package polymorphism;

public class PolymorphismTest {

	public static void main(String[] args) {
		ABaseClass base = new ABaseClass();
		ASubClass sub = new ASubClass();
		ABaseClass subAsBase = new ASubClass();
//		base.aMethod(sub);
		base.aMethod(subAsBase); // The runtime type of subAsBase does not matter here ... 
//		base.aMethod(base);
//		sub.aMethod(sub);
		sub.aMethod(subAsBase);
//		sub.aMethod(base);
		subAsBase.aMethod(sub);		// but it matters here. Why?
//		subAsBase.aMethod(subAsBase);
//		subAsBase.aMethod(base);
		
	}

}
