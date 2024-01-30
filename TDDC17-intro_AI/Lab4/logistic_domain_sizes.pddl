;; This is a plain STRIPS formulation of the standard Logistics domain.

;; In this domain, there are 12 different types of objects: "object"
;; and "bigobject" (the packages to be transported), "truck", "bigtruck",
;; "airplane", "train" and their common supertype "vehicle", "bigvehicle",
;; "location" and the subtypes "airport", "station" and finally "city".
;; Types are defined by static (in the sense that there are no operators 
;; that change their truth value) unary predicates.
;; The types of objects in a problem instance must be defined by including
;; the appropriate typing predicates in the initial state.

;; A binary static predicate called "loc" describes the topology of the
;; problem instance: "(loc ?l ?c)" is true iff the location ?l is in city
;; ?c.

(define (domain logistics)
  (:requirements :strips)
  (:predicates

   ;; Static predicates:
   ;; Here we need to add the new objects we use
   (object ?o) (bigobject ?b) (truck ?t) (bigtruck ?i) (airplane ?p) (train ?r)
   (vehicle ?v) (location ?l) (airport ?a) (station ?s) (city ?c) (loc ?l ?c)
   (bigvehicle ?g)

   ;; Non-static predicates:
   ;; We do not need to add any new no-static predicates
   (at ?x ?l) ;; ?x (package or vehicle) is at location ?l
   (in ?p ?v) ;; package ?p is in vehicle ?v
   )

  ;; Actions for loading and unloading packages.
  ;; By declaring all trucks and airplanes to be also "vehicle", we
  ;; can use the same load/unload operator for both (otherwise we
  ;; would need one for each subtype of vehicle).
  ;; Here we changed to get to types of loading actions, one big load
  ;; for big objects, and one small load for small objects.
  (:action load_small
    :parameters (?o ?v ?l)
    :precondition (and (object ?o) (vehicle ?v) (location ?l)
		       (at ?v ?l) (at ?o ?l))
    :effect (and (in ?o ?v) (not (at ?o ?l))))

  (:action unload_small
    :parameters (?o ?v ?l)
    :precondition (and (object ?o) (vehicle ?v) (location ?l)
		       (at ?v ?l) (in ?o ?v))
    :effect (and (at ?o ?l) (not (in ?o ?v))))

  (:action load_big
    :parameters (?b ?g ?l)
    :precondition (and (bigobject ?b) (bigvehicle ?g) (location ?l)
		       (at ?g ?l) (at ?b ?l))
    :effect (and (in ?b ?g) (not (at ?b ?l))))

  (:action unload_big
    :parameters (?b ?g ?l)
    :precondition (and (bigobject ?b) (bigvehicle ?g) (location ?l)
		       (at ?g ?l) (in ?b ?g))
    :effect (and (at ?b ?l) (not (in ?b ?g))))

  ;; Drive a truck between two locations in the same city. Or a 
  ;; plane/train between cities.
  ;; By declaring all locations, including airports, to be of type
  ;; "location", we can use only one driving operator (otherwise,
  ;; we would again need one for each case, i.e. one for from-location-
  ;; to-airport, one for from-location-to-location, etc. Very
  ;; unnecessay).
  ;; Here we need to add the big truck as well, which works in the same
  ;; way as the truck.
  (:action drive_small
    :parameters (?t ?l1 ?l2 ?c)
    :precondition (and (truck ?t) (location ?l1) (location ?l2) (city ?c)
		       (at ?t ?l1) (loc ?l1 ?c) (loc ?l2 ?c))
    :effect (and (at ?t ?l2) (not (at ?t ?l1))))

  (:action drive_big
    :parameters (?i ?l1 ?l2 ?c)
    :precondition (and (bigtruck ?i) (location ?l1) (location ?l2) (city ?c)
		       (at ?i ?l1) (loc ?l1 ?c) (loc ?l2 ?c))
    :effect (and (at ?i ?l2) (not (at ?i ?l1))))

  ;; Fly an airplane between two airports.
  (:action fly
    :parameters (?p ?a1 ?a2)
    :precondition (and (airplane ?p) (airport ?a1) (airport ?a2)
		       (at ?p ?a1))
    :effect (and (at ?p ?a2) (not (at ?p ?a1))))

    ;; A train travels between cities.
    ;; This works the same way as the airplane, but the train can only travel
    ;; between stations and have different loading capabilities compared to
    ;; airplanes, but theese are defined in the problem file.
    (:action travel
      :parameters (?r ?s1 ?s2)
      :precondition (and (train ?r) (station ?s1) (station ?s2)
  		       (at ?r ?s1))
      :effect (and (at ?r ?s2) (not (at ?r ?s1))))
  )
