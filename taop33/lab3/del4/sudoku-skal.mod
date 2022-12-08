# Sudoku

# x[i,j,k] = 1 if pos (i,j) contains digit k.
var x{1..9,1..9,1..9} binary;

param given{1..9,1..9};

# write model here ....
set N:= 1..9;

#rad
subject to const1{i in N, k in N}:
    sum{j in N} x[i,j,k] = 1;

#kol
subject to const2{j in N, k in N}:
      sum{i in N} x[i,j,k] = 1;

#en siffra i pos
subject to const3{i in N, j in N}:
    sum{k in N} x[i,j,k] = 1;

#kvadrant
subject to const4{k in N, p in 1..3, q in 1..3}:
    sum{i in (3*p-2..3*p)} sum {j in 3*q-2..3*q} x[i,j,k] = 1;

# Assign given digits
subject to fix{i in 1..9, j in 1..9: given[i,j]>0}: x[i,j,given[i,j]]=1;

solve;
    
# Display the result
printf("\nSudoku solution:\n");
for{i in 1..9} {
  for{j in 1..9} {
    printf "%2d",sum{k in 1..9} k*x[i,j,k];
  }
  printf "\n";
}
printf "\n";

end;
