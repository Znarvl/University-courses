Problem:    lp2
Rows:       24
Columns:    18
Non-zeros:  81
Status:     OPTIMAL
Objective:  v = 3880 (MINimum)

   No.   Row name   St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 v            B           3880                             
     2 const1[1]    B              0                          -0 
     3 const1[2]    B            -64                          -0 
     4 const1[3]    B              0                          -0 
     5 const2[1]    NS            92            92             =            14 
     6 const2[2]    NS            82            82             =            11 
     7 const2[3]    NS            83            83             =            26 
     8 const2[4]    NS            69            69             =            24 
     9 const2[5]    NS            74            74             =             6 
    10 const3[1,1]  B            -92                          -0 
    11 const3[1,2]  NU             0                          -0            -6 
    12 const3[1,3]  NU             0                          -0           -20 
    13 const3[1,4]  B            -69                          -0 
    14 const3[1,5]  B              0                          -0 
    15 const3[2,1]  NU             0                          -0            -5 
    16 const3[2,2]  B            -82                          -0 
    17 const3[2,3]  B            -83                          -0 
    18 const3[2,4]  NU             0                          -0           -19 
    19 const3[2,5]  B            -74                          -0 
    20 const3[3,1]  NU             0                          -0      -6.92391 
    21 const3[3,2]  B              0                          -0 
    22 const3[3,3]  NU             0                          -0            -3 
    23 const3[3,4]  B              0                          -0 
    24 const3[3,5]  B              0                          -0 

   No. Column name  St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 x[1,1]       B              0             0               
     2 x[1,2]       B             82             0               
     3 x[1,3]       B             83             0               
     4 x[1,4]       B              0             0               
     5 x[1,5]       B             74             0               
     6 x[2,1]       B             92             0               
     7 x[2,2]       NL             0             0                          11 
     8 x[2,3]       B              0             0               
     9 x[2,4]       B             69             0               
    10 x[2,5]       NL             0             0                          15 
    11 x[3,1]       NL             0             0                     8.92391 
    12 x[3,2]       B              0             0               
    13 x[3,3]       B              0             0               
    14 x[3,4]       NL             0             0                           4 
    15 x[3,5]       NL             0             0                          18 
    16 y[1]         NU             1                           1         -1563 
    17 y[2]         NU             1                           1         -1005 
    18 y[3]         B              0                           1 

Karush-Kuhn-Tucker optimality conditions:

KKT.PE: max.abs.err = 2.84e-14 on row 3
        max.rel.err = 2.04e-14 on row 20
        High quality

KKT.PB: max.abs.err = 2.84e-14 on row 2
        max.rel.err = 2.84e-14 on row 2
        High quality

KKT.DE: max.abs.err = 3.55e-15 on column 8
        max.rel.err = 7.25e-17 on column 9
        High quality

KKT.DB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

End of output
