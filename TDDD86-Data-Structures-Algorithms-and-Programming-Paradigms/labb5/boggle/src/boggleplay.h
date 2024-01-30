#ifndef BOGGLEPLAY_H
#define BOGGLEPLAY_H

#include "Boggle.h"

void playOneGame(Boggle& boggle);
void printOwnLetters();
void printHumanRound(Boggle& boggle);
void printBoard(Boggle& boggle);
void decideWinner(Boggle& boggle);
void printAIRound(Boggle& boggle);
void notValidBoard();
void printOwnLetters(string &input, int numCubes);
void clearConsole();



#endif // BOGGLEPLAY_H
