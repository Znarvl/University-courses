param m := 8;
param n := 8;

var board{ 1..n, 1..m } binary;

maximize z: sum{i in 1..n} sum{j in 1..m} board[i,j];

subject to const1{ i in 1..n}:
    sum{ j in 1..m } board[i,j] <= 1;

subject to const2{ j in 1..m}:
    sum{ i in 1..n } board[i,j] <= 1;

solve;