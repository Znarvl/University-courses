/*
 * Adds coordinates and creates a linked node list
 * containing this coordinates
 * Using heureistiskt to find different paths
 * in a file containing points
 */

#include <iostream>
#include "Tour.h"
#include "Node.h"
#include "Point.h"

Tour::Tour()
{

}

Tour::~Tour()
{
    Node* currentNode = firstPoint;
    Node* nextNode = nullptr;
    // Destructs second node first, iterates over all and deletes first last
    while(nextNode != firstPoint)
    {
        nextNode = currentNode->next;
        delete currentNode;
        currentNode = nextNode;
    }
}

void Tour::show()
{
    Node* currentNode = firstPoint;
    while(currentNode != nullptr && currentNode->next != firstPoint)
    {
        cout << currentNode->point << endl;
        currentNode = currentNode->next;
    };
}

void Tour::draw(QGraphicsScene *scene)
{
    Node* currentNode = firstPoint;
    while(currentNode != nullptr && currentNode->next != firstPoint)
    {
        currentNode->point.drawTo(currentNode->next->point, scene);
        currentNode = currentNode->next;
    };
}

int Tour::size()
{
    Node* currentNode = firstPoint;
    int size = 0;

    while(currentNode != nullptr && currentNode->next != firstPoint)
    {
        size++;
        currentNode = currentNode ->next;
    };

    return size;
}


double Tour::distance()
{
    Node* currentNode = firstPoint;
    double distance = 0;

    while (currentNode != nullptr && currentNode->next != firstPoint)
    {
       distance += currentNode->point.distanceTo(currentNode->next->point);
       currentNode = currentNode->next;
    };

    return distance;
}

void Tour::insertNearest(Point p)
{
    Node* currentNode = firstPoint;
    Node* shortestNode = nullptr;
    Node* nextNode = nullptr;
    double shortestDist = numeric_limits<double>::infinity();
    double calcDist = 0;

    if(firstPoint == nullptr)
    {
        firstPoint = new Node(p);
        currentNode = firstPoint;
    }

    // Iterates over nodes to find the shortest path from node standing on
    // using first shortestDist as infinty to know that there are no bigger
    while(currentNode != nullptr && currentNode->next != firstPoint)
    {
        calcDist = currentNode->point.distanceTo(p);
        if(calcDist < shortestDist)
        {
            shortestDist = calcDist;
            shortestNode = currentNode;
            nextNode = currentNode->next;
        }
        currentNode = currentNode->next;
    }

    /*
     * Makes the linked node list circular on the first iteration
     * after the first point is inserted.
     */
    if(nextNode == nullptr)
    {
        nextNode = firstPoint;
    }

    shortestNode->next = new Node(p, nextNode);
}

void Tour::insertSmallest(Point p)
{
    Node* currentNode = firstPoint;
    Node* shortestNode = nullptr;
    Node* nextNode = nullptr;
    double shortestDist = numeric_limits<double>::infinity();

    if(firstPoint == nullptr)
    {
        firstPoint = new Node(p);
        currentNode = firstPoint;
    }

    while(currentNode != nullptr && currentNode->next != firstPoint)
    {
        double calcDist = 0;
        double incDist = 0;
        double orgDist = 0;

        /*
         * If more than 1 node exist it calculates the increase
         * in total distance from inserting the point between P1 and P2.
         */
        if(currentNode->next != nullptr)
        {
            orgDist = currentNode->point.distanceTo(currentNode->next->point);
            calcDist += currentNode->point.distanceTo(p);
            calcDist += p.distanceTo(currentNode->next->point);
        }

        incDist = calcDist - orgDist;

        if(incDist < shortestDist)
        {
            shortestDist = incDist;
            shortestNode = currentNode;
            nextNode = currentNode->next;
        }
        currentNode = currentNode->next;
    }

    // Makes the linked node list circular on the first iteration
    // after the first point is inserted.
    if(nextNode == nullptr)
    {
        nextNode = firstPoint;
    }

    shortestNode->next = new Node(p, nextNode);
}
