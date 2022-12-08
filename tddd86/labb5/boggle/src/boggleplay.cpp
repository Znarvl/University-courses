

#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <sstream>
#include "Boggle.h"
#include "bogglemain.h"
#include "strlib.h"
#include "algorithm"

void printBoard(Boggle &boggle);
void printHumanRound(Boggle &boggle);
void decideWinner(Boggle& boggle);
void printAIRound(Boggle &boggle);

/*
 * Plays one game of Boggle using the given boggle game state object.
 */
void playOneGame(Boggle& boggle) {
    boggle.initDirections();
    boggle.initLexicon();
    boggle.initGame();

    printBoard(boggle);
    cout << boggle.typeWord << endl;
    getline(cin, boggle.guess);


    while(boggle.guess.length() != 0)
    {
        clearConsole();
        printBoard(boggle);

        transform(boggle.guess.begin(), boggle.guess.end(), boggle.guess.begin(), ::toupper);
        if(!boggle.isValidGuess())
        {
            cout << boggle.testGuess() << endl;
        }
        else
        {
            boggle.humanTurn();
            cout << boggle.foundWord() << endl;
            printHumanRound(boggle); // fix couts
        }
        cout << boggle.typeWord << endl;
        getline(cin, boggle.guess);
    }

    boggle.AIWordFinder();
    printAIRound(boggle);
    decideWinner(boggle);
}

/*
 * prints a string and gets input
 */
void printOwnLetters(string& input, int numCubes){
     std::cout<<"Enter a string of "<< numCubes << " letters (A-Z)"<<std::endl;
     getline(cin, input);
}

/*
 * Prints a string
 */
void notValidBoard(){
    cout << "That is not a valid 16-letter board String. Try again." << endl;

}

/*
 * prints the result of the human player after each round
 */
void printHumanRound(Boggle& boggle)
{
    string words = "{";

    std::cout << "Your words (" << boggle.humanLex.size() << "): ";
    foreach(string word in boggle.humanLex)
    {
        words = words + "\"" + word + "\", ";
    }

    words = words.substr(0, words.length()-2);
    words += "}";

    std::cout << words << std::endl;
    std::cout << "Your score: " << boggle.humanScore << std::endl;
}

/*
 * prints the board
 */
void printBoard(Boggle& boggle)
{
    std::cout << std::endl;
    for (int i = 0; i < boggle.playArea.nRows; i++)
    {
        for (int j = 0; j < boggle.playArea.nCols; j++)
        {
            std::cout << boggle.playArea[i][j].chosenSide;
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

/*
 * Decides the winner based on points.
 */
void decideWinner(Boggle& boggle)
{
    if(boggle.AIScore > boggle.humanScore)
    {
        cout << "Ha ha ha, I destroyed you." << endl << "Better luck next time, puny human!" << endl;
    }
    else
    {
        cout << "The human managed to hack Skynet!" << endl << "The Humans survive this round!" << endl;
    }
}

/*
 * Prints the result from the AI round
 */
void printAIRound(Boggle& boggle)
{
    string words = "{";
    std::cout << "It's my turn!" << std::endl;
    std::cout << "My words (" << boggle.AILexicon.size() << "): ";

    foreach(string word in boggle.AILexicon)
    {
        words = words + "\"" + word + "\", ";
    }

    words = words.substr(0, words.length()-2);
    words += "}";

    std::cout << words << std::endl;
    std::cout << "My score: " << boggle.AIScore << std::endl;
}

/*
 * Erases all currently visible text from the output console.
 */
void clearConsole() {
#if defined(_WIN32) || defined(_WIN64)
    std::system("CLS");
#else
    std::system("clear");
#endif
}
