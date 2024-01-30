param n;
param m;

#floor plates
var x{1..n} binary;

# a = 1 if pipe
param a{1..m,1..n};

minimize asbest: sum{i in 1..n} x[i];

subject to const1{i in 1..m}:
    sum{j in 1..n} a[i,j] * x[j] >=1;


solve;
