/**
 * Creates a list of Tiles, which has the functionality
 * to add, delete, move up and lower Tiles
 * in the list
 */

#ifndef TILELIST_H
#define TILELIST_H

#include <QGraphicsScene>
#include "Tile.h"

class TileList {
public:
    TileList();
    ~TileList();
    void addTile(const Tile& tile);      //add a tile object to the tile list
    void drawAll(QGraphicsScene* scene); // renders all tiles in list
    int indexOfTopTile(int x, int y);    // Returns the index of a specific tile at x,y coord
    void lower(int x, int y);            // sets a specific tile at x,y coord to first in array (lowest index)
    void raise(int x, int y);            // Sets a specific tile at x,y coord last in array (highest index)
    void remove(int x, int y);           // Removes tile from array at specific x,y coord
    void removeAll(int x, int y);        // Removes all tiles at a specific x,y coord
    /*
     * Copies the old list and creates a new list of double size.
     * Copies the old elements to the new expanded list.
     */
    void expandList();
    void printDebug(); // Prints info about all the Tiles located in the TileList.

private:
    Tile* tileList;
    int maxCapacity = 0;
    int nextFreeI = maxCapacity;


};

#endif // TILELIST_H
