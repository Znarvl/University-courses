/** Program applies two words
  *  and makes the shortest valid word route from the first word
  * to the other, building a chain of words
  */

#include <fstream>
#include <iostream>
#include <string>
#include <queue>
#include <stack>
#include <unordered_set>
using namespace std;

const string ALPHABET  = "abcdefghijklmnopqrstuvwxyz";
unordered_set<string> dictionary;
unordered_set<string> usedWords;

void buildDictionary();
void wordChain(const string& w1, const string& w2);

int main() {
    buildDictionary();
    string w1, w2;

    cout << "Welcome to TDDD86 Word Chain." << endl;
    cout << "If you give me two English words, I will transform the" << endl;
    cout << "first into the second by changing one letter at a time." << endl;
    cout << endl;

    cout << "Please type two words: ";
    cin >> w1 >> w2;

    wordChain(w1, w2);

    cout << "Have a nice day!\n";

    return 0;
}

void buildDictionary() {
    string dictionaryFile = "dictionary.txt";
    ifstream reader;
    reader.open(dictionaryFile);
    string line;

    while(getline(reader, line)) {
        dictionary.insert(line);
    }
    reader.close();
}

bool dictLookUp(const string& word) {
    unordered_set<string>::const_iterator got = dictionary.find (word);

    if (got != dictionary.end()) {
        return true;
    }
    return false;
}

bool usedWordLookUp(const string& word) {
    unordered_set<string>::const_iterator got = usedWords.find (word);

    if (got != usedWords.end()) {
        return true;
    }
    return false;
}

void wordChain(const string& w1, const string& w2) {
    queue<stack<string>> wordQueue;
    stack<string> wordStack;
    wordStack.push(w1);
    wordQueue.push(wordStack);

    // Put both words in front to be checked
    while(!wordQueue.empty()) {
        auto currentStack = wordQueue.front();
        auto currentWord = currentStack.top();

        //If equal, pop all words that have been used in chain
        if(currentWord.compare(w2) == 0) {
            cout << "Chain from data back to code:\n";
            while(!currentStack.empty()) {
                cout << currentStack.top() + " ";
                currentStack.pop();
            }
            cout << "\n";
            break;
        }
        else {
           // Comparing new letters if they are words in dic
            usedWords.insert(currentWord);
            for(unsigned i = 0; i < ALPHABET.length(); i++) {
                for(unsigned j = 0; j < currentWord.size(); j++) {
                    string testWord = currentWord;
                    testWord[j] = ALPHABET[i];

                    //If they are ok, put in stack and queue and try new word
                    if(dictLookUp(testWord) && !usedWordLookUp(testWord)) {
                        stack<string> newStack = currentStack;
                        newStack.push(testWord);
                        wordQueue.push(newStack);
                    }
                }
            }
            wordQueue.pop();
        }
    }
}
