Problem:    kdiet
Rows:       15
Columns:    9
Non-zeros:  125
Status:     OPTIMAL
Objective:  totalpris = 14.8557377 (MINimum)

   No.   Row name   St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 totalpris    B        14.8557                             
     2 minnytta[Cal]
                    B        3965.37          2000               
     3 minnytta[Carbo]
                    NL           350           350                   0.0277049 
     4 minnytta[Protein]
                    B        172.029            55               
     5 minnytta[VitA]
                    NL           100           100                   0.0267541 
     6 minnytta[VitC]
                    B        132.213           100               
     7 minnytta[Calc]
                    B        234.221           100               
     8 minnytta[Iron]
                    NL           100           100                   0.0248361 
     9 maxnytta[Cal]
                    B        3965.37                       99999 
    10 maxnytta[Carbo]
                    B            350                         375 
    11 maxnytta[Protein]
                    B        172.029                       99999 
    12 maxnytta[VitA]
                    B            100                       99999 
    13 maxnytta[VitC]
                    B        132.213                       99999 
    14 maxnytta[Calc]
                    B        234.221                       99999 
    15 maxnytta[Iron]
                    B            100                       99999 

   No. Column name  St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 port['Quarter Pounder w/ Cheese']
                    B        4.38525             0           100 
     2 port['McLean Deluxe w/ Cheese']
                    NL             0             0           100      0.322295 
     3 port['Big Mac']
                    NL             0             0           100     0.0191475 
     4 port[Filet-O-Fish]
                    NL             0             0           100     0.0853443 
     5 port['McGrilled Chicken']
                    NL             0             0           100      0.713672 
     6 port['Fries, small']
                    B        6.14754             0           100 
     7 port['Sausage McMuffin']
                    NL             0             0           100     0.0624098 
     8 port['1% Lowfat Milk']
                    B        3.42213             0           100 
     9 port['Orange Juice']
                    NL             0             0           100     0.0627213 

Karush-Kuhn-Tucker optimality conditions:

KKT.PE: max.abs.err = 1.42e-14 on row 8
        max.rel.err = 7.07e-17 on row 8
        High quality

KKT.PB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

KKT.DE: max.abs.err = 1.11e-16 on column 6
        max.rel.err = 5.05e-17 on column 8
        High quality

KKT.DB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

End of output
