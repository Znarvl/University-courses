#include <sstream>
#include "Boggle.h"
#include "bogglemain.h"
#include "boggleplay.h"
#include "random.h"
#include "shuffle.h"
#include "strlib.h"
#include "algorithm"
#include "grid.h"

static const int NUM_CUBES = 16;   // the number of cubes in the game
static const int CUBE_SIDES = 6;   // the number of sides on each cube
static string CUBES[NUM_CUBES] = {        // the letters on all 6 sides of every cube
   "AAEEGN", "ABBJOO", "ACHOPS", "AFFKPS",
   "AOOTTW", "CIMOTU", "DEILRX", "DELRVY",
   "DISTTY", "EEGHNW", "EEINSU", "EHRTVW",
   "EIOSST", "ELRTTY", "HIMNQU", "HLNNRZ"
};

const pair <const int, const int> LEFT(0, -1);
const pair <const int, const int> RIGHT(0, 1);
const pair <const int, const int> UP(-1, 0);
const pair <const int, const int> DOWN(1, 0);
const pair <const int, const int> UPPER_LEFT(-1, -1);
const pair <const int, const int> UPPER_RIGHT(-1, 1);
const pair <const int, const int> LOWER_RIGHT(1, 1);
const pair <const int, const int> LOWER_LEFT(1, -1);

void Boggle::initRandomBoard(){
    int curDice = 0;

    for (int i = 0; i < dice.size(); i++)
    {
        dice[i].chosenSide = dice[i].cubeSides[randomInteger(0, CUBE_SIDES-1)];
    }

    for (int i = 0; i < playArea.numRows(); i++)
    {
        for (int j = 0; j < playArea.numCols(); j++)
        {
            playArea[i][j] = dice[curDice];
            curDice++;
        }
    }
    shuffle(playArea);

};

void Boggle::initCubes(){
    dice.resize(NUM_CUBES);
    for (int i = 0; i < dice.size(); i++)
    {
        for (int j = 0; j < CUBE_SIDES; j++) {
            dice[i].cubeSides.reserve(CUBE_SIDES);
            dice[i].cubeSides.push_back(CUBES[i][j]);
        }
    }
}


void Boggle::initPlayerBoard()
{
    failedString:
    bool okString = false;
    string userInput = "";

    while(!okString)
    {
        printOwnLetters(userInput, NUM_CUBES);
        if(userInput.length() == NUM_CUBES)
        {
            transform(userInput.begin(), userInput.end(), userInput.begin(), ::toupper);
            for (int i = 0; i < NUM_CUBES; i++)
            {
                //Ascii codes for capital letters A-Z
                if(!(userInput[i] >= 65 && userInput[i] <= 90))
                {
                    notValidBoard();
                    goto failedString;
                }
                else
                {
                    okString = true;
                }
            }
        }
        else{
            notValidBoard();
        }
    }

    int counter = 0;
    for (int i = 0; i < playArea.nRows; i++)
    {
        for (int j = 0; j < playArea.nCols; j++)
        {
            playArea[i][j].chosenSide = userInput[counter];
            counter++;
        }
    }
}

void Boggle::initGame()
{
    initCubes();
    humanScore = 0;
    AIScore = 0;
    humanLex.clear();
    AILexicon.clear();

    if (yesOrNo("Do you want to generate a random board? (Y/N)? "))
    {
        initRandomBoard();
    }
    else {
        initPlayerBoard();
    }

    for (int i = 0; i < playArea.numRows(); i++)
    {
        for (int j = 0; j < playArea.numCols(); j++)
        {
            playArea[i][j].x = i;
            playArea[i][j].y = j;
        }
    }
}

void Boggle::initLexicon()
{
    engLexicon.addWordsFromFile(DICTIONARY_FILE);
}

void Boggle::humanTurn()
{
    for (int i = 0; i < playArea.nRows; i++)
    {
        for (int j  = 0; j < playArea.nCols; j++)
        {
            if(playArea[i][j].chosenSide == guess[0])
            {
                if(humanWordFinder(guess, playArea[i][j]))
                {
                    canFormWord = true;
                    humanLex.add(guess);
                    humanScore += max(1, int(guess.length())-3);
                    playArea[i][j].visited = false;
                    goto theEnd;
                }
            }
        }
    }
    canFormWord = false;
    theEnd:;
}


bool Boggle::humanWordFinder(string remaining, Dice &cube)
{
    if(remaining.length() == 0)
    {
        return true;
    }
    else if(remaining[0] == cube.chosenSide)
    {
        cube.visited = true;
        remaining = remaining.substr(1, remaining.size());

        for(const pair<const int, const int>& dir : directions)
        {
            if(playArea.inBounds(cube.x + dir.first, cube.y + dir.second) &&
                    !playArea[cube.x + dir.first][cube.y + dir.second].visited)
            {
                Dice &nextCube = playArea[cube.x + dir.first][cube.y + dir.second];
                if(humanWordFinder(remaining, nextCube))
                 {
                     cube.visited = false;
                     return true;
                 }
            }
        }
        cube.visited = false;
        return false;
    }
    else
    {
        cube.visited = false;
        return false;
    }
}

void Boggle::initDirections()
{
    directions.reserve(ADJACENT_CUBES);
    directions.push_back(LEFT);
    directions.push_back(UPPER_LEFT);
    directions.push_back(UP);
    directions.push_back(UPPER_RIGHT);
    directions.push_back(RIGHT);
    directions.push_back(LOWER_RIGHT);
    directions.push_back(DOWN);
    directions.push_back(LOWER_LEFT);
}



void Boggle::AIWordFinder()
{
    for (int i = 0; i < playArea.numRows(); i++)
    {
        for (int j = 0; j < playArea.numRows(); j++)
        {
            string chosen = "";
            chosen = playArea[i][j].chosenSide;
            (AIRecursion(chosen, playArea[i][j]));
        }
    }
}

void Boggle::AIRecursion(string &chosen, Dice &curCube)
{
    curCube.visited = true;

    if(engLexicon.containsPrefix(chosen))
    {
        for(pair<int, int> dir : directions)
        {
            if(playArea.inBounds(curCube.x + dir.first, curCube.y + dir.second) &&
                    !playArea[curCube.x + dir.first][curCube.y + dir.second].visited)
            {
                Dice &nextCube = playArea[curCube.x + dir.first][curCube.y + dir.second];
                string nextWord = chosen + nextCube.chosenSide;
                AIRecursion(nextWord, nextCube);
            }
        }
    }
    if(chosen.length() >= 4 && !AILexicon.contains(chosen) &&
            engLexicon.contains(chosen) && !humanLex.contains(chosen))
    {
        AILexicon.add(chosen);
        AIScore += max(1, int(chosen.length() - 3));
    }
    curCube.visited = false;
}



string Boggle::testGuess()
{
    if(guess.length() < 4 && guess.length() > 0)
    {
        return "The word is to short!\nIt needs to be four or more characters long.";
    }
    else if (humanLex.contains(guess))
    {
        return "You've already recieved score for this word.\nTry another one.";
    }
    else if (!engLexicon.contains(guess))
    {
        return "Your guess is not part of the English dictionary!\nTry again!";
    }
    else
    {
        return "";
    }
}

bool Boggle::isValidGuess()
{
    if(guess.length() >= 4 && !humanLex.contains(guess) && engLexicon.contains(guess))
    {
        return true;
    }
    else
    {
        return false;
    }
}

string Boggle::foundWord()
{
    switch (canFormWord)
    {
    case true :
        return "You found a new word! \"" + guess + "\"";
    case false :
        return "That word can't be formed on this board.";
    }
}
