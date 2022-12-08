/*
 * TDDD86 Tour
 * Contains the Tour structure and its members.
 * See Tour.cpp for code implementation
 */

#ifndef TOUR_H
#define TOUR_H

#include "Node.h"
#include "Point.h"

class Tour {
public:

    Tour(Point a);                              // Debug constructor
    Tour(Point a, Point b);                     // Debug constructor
    Tour(Point a, Point b, Point c, Point d);   // Debug constructor
    Tour();                                     // Constructor
    ~Tour();                                    // Destructor
    void show();                                // print the tour to standard output
    void draw(QGraphicsScene* scene);           // draw the tour on scene
    int size();                                 // number of points on tour
    double distance();                          // return the total distance of the tour
    void insertNearest(Point p);                // insert p using nearest neighbor heuristic
    void insertSmallest(Point p);               // insert p using smallest increase heuristic

private:
    Node* firstPoint = nullptr;                 // Pointer to Node class, defined as nullptr
};

#endif // TOUR_H
