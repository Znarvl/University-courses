#ifndef DICE_H
#define DICE_H

#include <vector>
using namespace std;

class Dice
{
public:
    Dice() = default;
    ~Dice() = default;

    char chosenSide;
    vector<char> cubeSides;
    bool visited = false;
    int x;
    int y;
};

#endif // DICE_H
