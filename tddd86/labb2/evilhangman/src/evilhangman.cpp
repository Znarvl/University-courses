/** A game that creates a hangman game that tries to cheat the player by
  * making the word not constant, it is instead a dynamic word that builds
  * from the biggest equivalence class of the word guessed
  *
  *
  */

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <list>
#include <set>
using namespace std;

const string ALPHABET  = "abcdefghijklmnopqrstuvwxyz";

void buildDictionary(int wordLength, vector<string>& possibleWords) {

    string dictionaryFile = "dictionary.txt";
    ifstream reader;
    reader.open(dictionaryFile);
    string line;

    while(getline(reader, line)) {
        if(line.length() == wordLength) {
            possibleWords.push_back(line);
        }
    }
    reader.close();
}

/**
 * Iterates over all the possible words building their equivalence class on the form "----" depending on the length.
 *  Where '-' is replaced by the guessed letter if it exists.
 * Returns a map with the equvalence classes as keys and a vector containing the words in that class.
*/
void buildEqClasses(const string& guessedLetter, map<string, vector<string>>& eqClass, vector<string>& possibleWords){
    size_t found;
    eqClass.clear();

    for(unsigned i = 0; i < possibleWords.size(); i++) {
            string eqKey = "";
            for (unsigned j = 0; j < possibleWords[i].size(); j++){
                found = guessedLetter.find(possibleWords[i][j]);
                if (found != guessedLetter.npos){
                    eqKey += guessedLetter;
                }
                else{
                    eqKey += "-";
                }
            }

            if(eqClass[eqKey].empty()){
                eqClass.insert(pair<string, vector<string>>(eqKey, vector<string>()));
            }
            eqClass[eqKey].push_back(possibleWords[i]);
    }
}

string updatePossibleWords(map<string, vector<string>>& eqClasses, vector<string>& possibleWords) {
    int largestSize = -1;
    string largestKey;

    // iterates over the keys in the map and finds the largest one.
    for (auto const& x : eqClasses) {

        if(largestSize == -1 || largestSize < eqClasses[x.first].size()) {
            largestSize = eqClasses[x.first].size();
            largestKey = x.first;
        }
    }

    possibleWords = eqClasses[largestKey];

    return largestKey;
}

void printDebug(vector<string>& possibleWords){
    cout << "There are: " << possibleWords.size() << " words left" << endl;
    cout << "They are: " << endl;
    for(string word : possibleWords) {
        cout << word << " ";
    }
    cout << endl;
}

void printGameState(int triesLeft, set<string>& usedLetters, string& correctWord) {
    cout << "You have: " << triesLeft << " tries left\n";
    cout << "You have guessed on the following letters:";

    for (auto it = usedLetters.begin(); it != usedLetters.end(); ++it) {
        cout << " " << *it;
    }
    cout << endl;
    cout << "The correct word is: " << correctWord << endl;
}

int updateGameState(string& correctWord, const string& eqKey, int triesLeft) {
    string oldWord = correctWord;

    for(unsigned i = 0; i < correctWord.length(); i++) {
        if(correctWord[i] == '-' && eqKey[i] != '-') {
            correctWord[i] = eqKey[i];
        }
    }

    if(!oldWord.compare(correctWord)) {
        triesLeft--;
    }
    cout << "The correct word has the following syntax: " << correctWord << endl;
    return triesLeft;
}

int getInputInt(const string& question) {
    int input;
    while(true) {
        //executes loop if the input fails (e.g., no characters were read)
        // Borrowed from: https://stackoverflow.com/questions/10349857/how-to-handle-wrong-data-type-input
        while (cout << question && !(cin >> input)) {
            cin.clear(); //clear bad input flag
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); //discard input
            cout << "Invalid input; please re-enter.\n";
        }
        return input;
    }
}

// Control so that the user enters a valid number of guesses
int initTries() {
    string question = "How many tries do you want\n";
    return getInputInt(question);
}

string toLowerCase(const string& wordIn) {
    string wordOut;
    for(unsigned i = 0; i < wordIn.length(); i++) {
        wordOut += tolower(wordIn[i]);
    }
    return wordOut;
}

bool setDebug() {
    string answer;
    cout << "Do you want to activate debug software? (y/n)\n";
    cout << "This prints the number of words left after each guess." << endl;
    cin >> answer;

    if(toLowerCase(answer) == "y") {
        return true;
    }
    else {
        return false;
    }
}

int setWordLength(vector<string>& possibleWords) {
    int wordLength;
    string question = "How long word do you want?\n";

    wordLength = getInputInt(question);

    buildDictionary(wordLength, possibleWords);

    if(!possibleWords.empty()) {
        return wordLength;
    }
    else {
        cout << "There exists no words of this length, try another word length.\n";
    }
}

// Sets the initial correct word to dashes of the set length.
string setInitialCorrectWord(int wordLength) {
    string correctWord;
    for(int i = 0; i < wordLength; i++) {
        correctWord += "-";
    }
    return correctWord;
}

string takeGuess(set<string>& usedLetters) {
    string guess;
    while(true) {
        cout << "Guess on a letter.\n";
        cin >> guess;

        size_t found = ALPHABET.find(guess);

        if(guess.length() == 1 && found != ALPHABET.npos) {
            set<std::string>::const_iterator got = usedLetters.find(guess);

            if(got == usedLetters.end()) {
                usedLetters.insert(guess);
                return guess;
            }
            else {
                cout << "Letter already used, choose a new letter\n";
            }
        }
        else {
            cout << "Enter a single character\n";
        }
    }
}

bool checkEndGame(const string& correctWord, int triesLeft) {
    size_t found = correctWord.find('-');

    if(found == correctWord.npos) {
        cout << "Congratulations! You won the unbeatable game!" << endl;
        return true;
    }
    else if(triesLeft == 0) {
        cout << "Sorry, you lost!\n";
        return true;
    }
    return false;
}

bool playAgain() {
    string answer;

    cout << "Do you wanna play again? (y/n)" << endl;
    cin >> answer;

    if(toLowerCase(answer) == "y") {
        return true;
    }
    return false;
}

int main() {
    bool restart = false;

    do{
        int wordLength;
        int triesLeft;
        bool debug;
        bool victory = false;
        string guessedLetter;
        string correctWord;
        string largestEqclass;

        map<string, vector<string>> wordEq;
        vector<string> possibleWords;
        set<string> usedLetters;

        cout << "Welcome to Hangman." << endl;

        wordLength = setWordLength(possibleWords);
        correctWord = setInitialCorrectWord(wordLength);
        triesLeft = initTries();
        debug = setDebug();

        while(!victory) {
            printGameState(triesLeft, usedLetters, correctWord);
            if (debug) {
                printDebug(possibleWords);
            }

            guessedLetter = takeGuess(usedLetters);

            buildEqClasses(guessedLetter, wordEq, possibleWords);
            largestEqclass = updatePossibleWords(wordEq, possibleWords);
            triesLeft = updateGameState(correctWord, largestEqclass, triesLeft);
            victory = checkEndGame(correctWord, triesLeft);
        }
        restart = playAgain();
    }
    while(restart);

    return 0;
}
