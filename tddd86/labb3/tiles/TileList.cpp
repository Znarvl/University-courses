#include "TileList.h"

TileList::TileList()
{
    tileList = new Tile[10];
    maxCapacity += 10;
    cout << "I asked the guy in the store where is the Terminator DVD..." << endl;
}

TileList::~TileList()
{
    delete[] tileList;
    cout << "He responded, “Aisle B, Back”" << endl;
}

void TileList::addTile(const Tile& tile)
{
    if(nextFreeI == maxCapacity){
        expandList();
    }

    tileList[nextFreeI] = tile;
    nextFreeI++;
}

void TileList::drawAll(QGraphicsScene* scene)
{
    for(int i = 0; i < nextFreeI; i++)
    {
        tileList[i].draw(scene);
    }
}

int TileList::indexOfTopTile(int x, int y)
{
    int topTile = -1;
    for(int i = 0; i < nextFreeI; i++)
    {
        if(tileList[i].contains(x, y))
        {
            topTile = i;
        }
    }
    return topTile;
}

void TileList::raise(int x, int y)
{
    int startIndex = indexOfTopTile(x, y);

    if(startIndex != -1 && startIndex != nextFreeI - 1){
        Tile tempTile = tileList[startIndex];

        tileList[nextFreeI] = tileList[startIndex];

        for(int i = startIndex; i < nextFreeI; i++)
        {
            tileList[i] = tileList[i+1];
        }
        tileList[nextFreeI] = tempTile;
    }
}

void TileList::lower(int x, int y)
{
    int startIndex = indexOfTopTile(x, y);

    if(startIndex > 0){
        Tile tempTile = tileList[startIndex];

        for(int i = startIndex; i > 0; i--)
        {
            tileList[i] = tileList[i-1];
        }
        tileList[0] = tempTile;
    }
}

void TileList::remove(int x, int y)
{
    int startIndex = indexOfTopTile(x, y);

    if(startIndex >= 0){
        for(int i = startIndex; i < nextFreeI; i++)
        {
            tileList[i] = tileList[i+1];
        }
        nextFreeI--;
    }
}

void TileList::removeAll(int x, int y)
{
    for(int i = 0; i < nextFreeI; i++)
    {
        remove(x, y);
    }
}

void TileList::expandList()
{
    maxCapacity = maxCapacity * 2;
    Tile* oldList = tileList;
    tileList = new Tile[maxCapacity];

    for(int i = 0; i < nextFreeI; i++)
    {
        tileList[i] = oldList[i];
    }
    delete[] oldList;
}

void TileList::printDebug()
{
    cout << "DEBUG:" << endl;
    for(int i = 0; i < maxCapacity; i++)
    {
        cout << i << ": " << tileList[i].toString() << endl;
    }
    cout << endl;
}
