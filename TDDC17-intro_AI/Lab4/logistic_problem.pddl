;; This is a small problem instance for the standard Logistics domain,
;; as defined in "logistic.pddl".

(define (problem train)
  (:domain logistics)
  (:objects
   city1 city2 city3 city4 city5          ;; there are five cities,
   truck1 truck2 truck3 truck4 truck5      ;; one truck in each city,
   airplane1                  ;; only one airplane,
   train1                       ;;Only one train
   office1 office2 office3 office4 office5   ;; offices are "non-airport" locations
   airport1 airport2 airport3 ;; airports, only 3 so does not cover all cities
   station1 station2 station3 ;;stations, one connected with airport, two without
   packet1 packet2 packet3           ;; three packages to be delivered
   )
  (:init
   ;; Type declarations:
   (object packet1) (object packet2) (object packet3)

   ;; all vehicles must be declared as both "vehicle" and their
   ;; appropriate subtype,
   (vehicle truck1) (vehicle truck2) (vehicle truck3) (vehicle airplane1)
   (truck truck1) (truck truck2) (truck truck3) (airplane airplane1)
   (vehicle truck4) (vehicle truck5) (truck truck4) (truck truck5)
   (vehicle train1)
   (train train1)

   ;; likewise, airports must be declared both as "location" and as
   ;; the subtype "airport",
   (location office1) (location office2) (location office3) (location office4) (location office5)
   (location airport1) (location airport2) (location airport3)
   (location station1) (location station2) (location station3)
   (airport airport1) (airport airport2) (airport airport3)
   (station station1) (station station2) (station station3)
   (city city1) (city city2) (city city3) (city city4) (city city5)

   ;; "loc" defines the topology of the problem,
   (loc office1 city1) (loc airport1 city1) (loc office2 city2)
   (loc airport2 city2) (loc office3 city3) (loc airport3 city3) (loc station1 city3)
   (loc office4 city4) (loc station2 city4)
   (loc office5 city5) (loc station3 city5)

   ;; The actual initial state of the problem, which specifies the
   ;; initial locations of all packages and all vehicles:
   (at packet1 office1)
   (at packet2 office3)
   (at packet3 office5)
   (at truck1 airport1)
   (at truck2 airport2)
   (at truck3 office3)
   (at truck4 office4)
   (at truck5 station3)
   (at airplane1 airport1)
   (at train1 station1)
   )

  ;; The goal is to have both packages delivered to their destinations:
  (:goal (and (at packet1 office4) (at packet2 office4) (at packet3 office4)))
  )
