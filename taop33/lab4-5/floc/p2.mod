param n;
param m;
param s{1..m};
param d{1..n};
param f{1..m};
param c{1..m, 1..n};
param e := 1;

var x{1..m, 1..n} >= 0;
var y{1..m} binary;

minimize v: sum{i in 1..m, j in 1..n} c[i,j] * x[i,j] + sum{i in 1..m} e * f[i]*y[i];

subject to const1 {i in 1..m}:
    sum{j in 1..n} x[i,j] <= s[i] * y[i];

subject to const2 {j in 1..n}:
    sum{i in 1..m} x[i,j] = d[j];

subject to const3 {i in 1..m, j in 1..n}:
    x[i,j] <= d[j] * y[i];

solve;