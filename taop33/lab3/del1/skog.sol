Problem:    kdiet
Rows:       9
Columns:    14
Non-zeros:  124
Status:     OPTIMAL
Objective:  totalpris = 8.827245331 (MINimum)

   No.   Row name   St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 totalpris    B        8.82725                             
     2 minnytta[energi]
                    NL          2050          2050                 0.000593783 
     3 minnytta[protein]
                    NL            55            55                   0.0113962 
     4 minnytta[fett]
                    B         139.67            80               
     5 minnytta[kolhyd]
                    NL           142           142                   0.0491774 
     6 maxnytta[energi]
                    B           2050                       1e+07 
     7 maxnytta[protein]
                    B             55                       1e+07 
     8 maxnytta[fett]
                    B         139.67                       1e+07 
     9 maxnytta[kolhyd]
                    B            142                       1e+07 

   No. Column name  St   Activity     Lower bound   Upper bound    Marginal
------ ------------ -- ------------- ------------- ------------- -------------
     1 port[spenat] NL             0             0         1e+07      0.626851 
     2 port[fronGHM]
                    NL             0             0         1e+07      0.166068 
     3 port[hassel] B        2.11775             0         1e+07 
     4 port[jordgubbar]
                    NL             0             0         1e+07      0.562271 
     5 port[loktrav]
                    NL             0             0         1e+07       0.45816 
     6 port[smultron]
                    NL             0             0         1e+07      0.562271 
     7 port[graslok]
                    NL             0             0         1e+07        0.8681 
     8 port[bjornbar]
                    NL             0             0         1e+07      0.646183 
     9 port[vin]    NL             0             0         1e+07      0.175403 
    10 port[barhaggmispe]
                    B        5.36268             0         1e+07 
    11 port[havtorn]
                    NL             0             0         1e+07      0.630961 
    12 port[rosenkvitten]
                    NL             0             0         1e+07      0.313571 
    13 port[sibirisk]
                    B        1.34681             0         1e+07 
    14 port[apple]  NL             0             0         1e+07       0.45126 

Karush-Kuhn-Tucker optimality conditions:

KKT.PE: max.abs.err = 9.09e-13 on row 2
        max.rel.err = 2.22e-16 on row 2
        High quality

KKT.PB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

KKT.DE: max.abs.err = 7.77e-16 on column 13
        max.rel.err = 2.59e-16 on column 13
        High quality

KKT.DB: max.abs.err = 0.00e+00 on row 0
        max.rel.err = 0.00e+00 on row 0
        High quality

End of output
