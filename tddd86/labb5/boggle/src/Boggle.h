// This is the .h file you will edit and turn in.
// We have provided a minimal skeleton for you,
// but you must finish it as described in the spec.
// Also remove these comments here and add your own, as well as on the members.
// TODO: remove this comment header and replace it with your own

#ifndef _boggle_h
#define _boggle_h

#include <iostream>
#include <string>
#include <grid.h>
#include <lexicon.h>
#include "dice.h"
#include <utility>

using namespace std;

class Boggle {
public:
    const string DICTIONARY_FILE = "EnglishWords.dat";
    const int MIN_WORD_LENGTH = 4;
    const int BOARD_SIZE = 4;
    const int ADJACENT_CUBES = 8;

    Grid<Dice> playArea = Grid<Dice>(BOARD_SIZE, BOARD_SIZE);
    vector<Dice> dice;
    Lexicon engLexicon;
    Lexicon AILexicon;
    Lexicon humanLex;
    vector<pair<const int, const int>> directions;
    string guess = "";
    string typeWord = "Type a word (or press Enter to end your turn):";
    bool canFormWord = false;

    int humanScore = 0;
    int AIScore = 0;



    /*
     * initializes a random board
     */
    void initRandomBoard();

    /*
     * initializes dice cubes
     */
    void initCubes();

    /*
     * initializes the gamestate by resetting variables
     * and generating a board
     */
    void initGame();

    /*
     * Takes a string (A-Z) and creates a board from it
     */
    void initPlayerBoard();

    /*
     * initializes the English lexicon
     */
    void initLexicon();

    /*
     * Plays a round for the human
     */
    void humanTurn();



    /*
     * Recursive function for finding the guessed word.
     * Visits the cubes next to the current one, removing one letter
     * at the time, trying to find a path to the guessed word
     */
    bool humanWordFinder(string remaining, Dice& cube);

    /*
     * Loops over the board and call recursion for each letter
     * to find all the words on the board
     */
    void AIWordFinder();

    /*
     * Recursive function, checks adjacent cubes of the current one
     * trying to find a path to build a word.
     */
    void AIRecursion(string& chosen, Dice& curCube);

    /*
     * initializes directions used for finding adjacent cubes
     */
    void initDirections();

    string testGuess();

    bool isValidGuess();

    string foundWord();

private:

};

#endif
