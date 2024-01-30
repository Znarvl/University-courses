/**
  * Creates a game where we kill and breed cells in a 2d grid
  * if there are too many, the cells will die (marked by -)
  * and if there is right amount they will expand (marked by X)
  *
  * Auhtors:
  *     Simon Jakobsson - simja649
  *     Dennis Berntsson -denbe829
  */

#include <iostream>
#include "grid.h"
#include "lifeutil.h"
#include <string>
#include <fstream>

Grid<char> createGrid() {
    return Grid<char>();
}

// Reads a text file and populates the grid with either living or dead cells.
void initGrid(Grid<char>& originalGrid, std::string inputFile) {
    std::ifstream textFile;
    int rows, columns;

    textFile.open(inputFile);
    textFile >> rows >> columns;

    originalGrid.resize(rows, columns);

    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < columns; j++) {
            textFile >> originalGrid[i][j];
        }
    }
    textFile.close();
}

void printGrid(const Grid<char>& printGrid){
    for (int i = 0; i < printGrid.nRows; i++){
        for (int j = 0; j < printGrid.nCols; j++){
            std::cout << printGrid[i][j];
        }
        std::cout << "\n";
    }
}

// Takes a coordinate and iterates over a 3x3 matrix.
// Returns the total number of living cells in this matrix.
// Does not count its own coordinate.
int testNeighbour(int x, int y, const Grid<char>& myGrid) {
    int counter = 0;
    char livingCell = 'X';

    for(int row = -1; row < 2; row++){
        for(int col = -1; col < 2; col++) {
            if ((row != 0 || col != 0) && myGrid.inBounds(y+row, x+col)) {
                if (myGrid.get(y+row, x+col) == livingCell) {
                    counter++;
                }
            }
        }
    }
    return counter;
}

// Copies the original grid to a new one, coordinates from the new grid is sent to testNeighbour().
// Depending on the result cells are updated to be either living or dead cells.
void nextGen(Grid<char>& updateGrid ) {
    Grid<char> newGrid = updateGrid;
    char livingCell = 'X';
    char deadCell = '-';
    int livingNeighbours = 0;

    for (int y = 0; y < newGrid.nRows; y++){
        for (int x = 0; x < newGrid.nCols; x++){

            // Checks locations around current cell
            livingNeighbours = testNeighbour(x, y, newGrid);

            // logic for updating cells
            if (livingNeighbours < 2){
                updateGrid.set(y, x, deadCell);
            }
            else if (livingNeighbours == 2){
                updateGrid.set(y, x, newGrid.get(y, x));
            }
            else if (livingNeighbours == 3){
                updateGrid.set(y, x, livingCell);
            }
            else if (livingNeighbours >= 4){
                updateGrid.set(y, x, deadCell);
            }

            livingNeighbours = 0;
        }
    }
}

// Creates a non-ending loop that displays the next generation of cells with a delay of 100 ms.
void animate(const Grid<char>& animateGrid){
    while(true){
        clearConsole();
        nextGen(animateGrid);
        printGrid(animateGrid);
        pause(100);
    }
}

// Displays a welcome message and asks the user for a text file to build the grid from.
// Then present a menu for the user to move forward with the game of life!
int main() {
    std::string welcome_msg = "Welcome to the TDDD86 Game of Life,\n"
                              "a simulation of the lifecycle of a bacteria colony.\n"
                              "Cells (X) live and die by the following rules:\n"
                              " - A cell with 1 or fewer neighbours dies.\n"
                              " - Locations with 2 neighbours remain stable.\n"
                              " - Locations with 3 neighbours will create life.\n"
                              " - A cell with 4 or more neighbours dies.\n";
    std::string inputFile;
    std::cout << welcome_msg << std::endl;
    std::cout << "Grid input filename? ";
    std::getline(std::cin, inputFile);

    Grid<char> originalGrid = createGrid();
    initGrid(originalGrid, inputFile);
    printGrid(originalGrid);

    std::string ans;

    while (true){
        std::cout << "a)nimate t)ick q)uit: ";
        std::cin >> ans;

        if (ans == "a"){
            animate(originalGrid);
        }
        else if (ans == "t"){
            clearConsole();
            nextGen(originalGrid);
            printGrid(originalGrid);
       }
        else if (ans == "q"){
            clearConsole();
            std::cout << "Have a nice Life! "  << std::endl; // good bye message
            break;
        }
        else {
            std::cout << "Wrong input try again\n";
        }
    }
    return 0;
}
