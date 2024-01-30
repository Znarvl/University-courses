

## Problem 1

//x: = [−oo, +oo]
L1. x:= 0
//x: ⊥
L2. x:= x + 1
//x: ⊥
L3. nop
//x: ⊥
L4. if x < 10 goto L2
//x: ⊥
L5. end
----
//x: = [−oo, +oo]
L1. x:= 0
//x: [] widening [0,0]
L2. x:= x + 1
//x: [] widening [1,1]
L3. nop
//x: []
L4. if x < 10 goto L2
//x: []
L5. end
----
//x: = [−oo, +oo]
L1. x:= 0
//x: [0,0] widening [1,1]
L2. x:= x + 1
//x: [1,1] widening [2,2]
L3. nop
//x: []
L4. if x < 10 goto L2
//x: []
L5. end
----
//x: = [−oo, +oo]
L1. x:= 0
//x: [0,+oo]
L2. x:= x + 1
//x: [1,+oo] 
L3. nop
//x: []
L4. if x < 10 goto L2
//x: [] 
L5. end

----
//x: = [−oo, +oo]
L1. x:= 0
//x: [0,+oo]
L2. x:= x + 1
//x: [1,+oo] 
L3. nop
//x: [1, +oo]
L4. if x < 10 goto L2
//x: [] widening [10,+oo]
L5. end

----
//x: = [−oo, +oo]
L1. x:= 0
//x: [0,+oo]
L2. x:= x + 1
//x: [1,+oo] 
L3. nop
//x: [1, +oo]
L4. if x < 10 goto L2
//x:[10,+oo]
L5. end

----
## Problem 2

### 1

We saw that the @ symbols in abstractions.txt corresponded to the nodes in the example from Report.html. 

### 2

We wrote the lock.c file and used the specified predicate abstraction to verify the code.c

Command:
./scripts/cpa.sh -config ./config/predicateAnalysis-PredAbsRefiner-SBE.properties ./ourcode/lock.c 

### 3

We used the normal predicateAnalysis.properties on vardep.c. The analysis returned TRUE with the normal code and FALSE if we changed the values in vardep.c.

Command:
./scripts/cpa.sh -config ./config/predicateAnalysis.properties ./ourcode/vardep.c