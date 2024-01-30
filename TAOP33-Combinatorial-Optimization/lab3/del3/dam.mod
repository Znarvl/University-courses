param m := 8;
param n := 8;

var board{ 1..n, 1..m } binary;

maximize z: sum{i in 1..n} sum{j in 1..m} board[i,j];

subject to const1{ i in 1..n}:
    sum{ j in 1..m } board[i,j] <= 1;

subject to const2{ j in 1..m}:
    sum{ i in 1..n } board[i,j] <= 1;

subject to const3{k in 0..6}:
    sum{i in 1..(8-k)} board[i+k,i] <=1;

subject to const4{k in 1..6}:
    sum{i in 1..(8-k)} board[i,i+k] <=1;

subject to const6{k in 1..6}:
    sum{i in 1..(8-k)} board[i,9-k-i] <=1;

subject to const7{k in 0..6}:
    sum{i in 1..(8-k)} board[i+k,9-1] <=1;

solve;
