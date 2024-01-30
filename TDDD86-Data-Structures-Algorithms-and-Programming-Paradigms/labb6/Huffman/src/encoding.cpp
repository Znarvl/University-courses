// This is the CPP file you will edit and turn in.
// Also remove these comments here and add your own, along with
// comments on every function and on complex code sections.
// TODO: remove this comment header

#include "encoding.h"
#include <functional>
#include <queue>
#include <vector>
#include "iostream"
#include "algorithm"



map<int, int> buildFrequencyTable(istream& input) {
    map<int, int> freqTable;
    int character = input.get();
    while(character != -1){
        int ascii = character;
        if (freqTable.find(ascii) != freqTable.end()){
            ++freqTable[ascii];
        }
        else{
            freqTable.insert(pair<const int,int>(ascii, 1));
        }
        character = input.get();
    }
    freqTable.insert(pair<const int,int>(PSEUDO_EOF,1));

    return freqTable;
}

HuffmanNode* buildEncodingTree(const map<int, int> &freqTable) {
    if (freqTable.size() == 1){
        return nullptr;
    }
    priority_queue<HuffmanNode> queue;

    for(const pair<const int,int>& i: freqTable)
    {
        queue.push(HuffmanNode(i.first, i.second));
    }

    while(queue.size() > 1){
        HuffmanNode* leftNode = new HuffmanNode(queue.top());
        queue.pop();
        HuffmanNode* rightNode = new HuffmanNode(queue.top());
        queue.pop();

        int newCount = leftNode->count + rightNode->count;
        queue.push(HuffmanNode(NOT_A_CHAR, newCount, leftNode, rightNode));
    }
    HuffmanNode* root = new HuffmanNode(queue.top());
    return root;
}

map<int, string> buildEncodingMap(HuffmanNode* encodingTree) {
    map<int, string> encodingMap;
    string path = "";

    if(encodingTree == nullptr)
    {
        return encodingMap;
    }

    mapRecursion(encodingTree, path, encodingMap);
    return encodingMap;
}

void encodeData(istream& input, const map<int, string> &encodingMap, obitstream& output) {
    input.clear();
    input.seekg(0, ios::beg);

    int current = input.get();
    string final;

    while(current != -1)
    {
        string character = encodingMap.at(current);

        for(int l: character){
            output.writeBit(l - '0');
        }
        current = input.get();
    }
    for(int j: encodingMap.at(PSEUDO_EOF)){
        output.writeBit(j - '0');
    }
}

void decodeData(ibitstream& input, HuffmanNode* encodingTree, ostream& output) {
    int curBit = input.readBit();
    HuffmanNode* curNode = encodingTree;

    while(curBit != -1)
    {

        bool foundLeaf = false;

        if(curNode->isLeaf() && curNode->character == PSEUDO_EOF)
        {
            break;
        }
        else if(curNode->isLeaf())
        {

            output.put(char(curNode->character));

            curNode = encodingTree;
            foundLeaf = true;
        }
        else if(curBit == 0)
        {
            curNode = curNode->zero;
        }
        else if(curBit == 1)
        {
            curNode = curNode->one;
        }

        if(!foundLeaf)
        {
            curBit = input.readBit();
        }
    }
}

void compress(istream& input, obitstream& output) {
    string header = "{";
    map<int, int> freqTable = buildFrequencyTable(input);
    HuffmanNode* encodingTree = buildEncodingTree(freqTable);
    map<int, string> encodingMap = buildEncodingMap(encodingTree);

    for(const pair<const int, int>& i : freqTable)
    {
        header += to_string(i.first) + ":" + to_string(i.second) + ", ";
    }
    header = header.substr(0, header.length()-2);
    header += "}";

    for(int c : header)
    {
        output.put(c);
    }
    encodeData(input, encodingMap, output);
    freeTree(encodingTree);
}

void decompress(ibitstream& input, ostream& output) {
    char character = input.get();
    string asciiCode = "";
    string freq = "";
    bool foundSeparatorColon = false;
    bool foundSeparatorComma = false;
    map<int, int> freqTable;
    HuffmanNode* encodingTree;

    while(input.get(character))
    {
        if(character != '}')
        {
            if(!foundSeparatorColon)
            {
                if(character == ':')
                {
                    foundSeparatorColon = true;
                }
                else
                {
                    asciiCode += character;
                }
            }
            else if(foundSeparatorColon && !foundSeparatorComma)
            {
                if(character == ',')
                {
                    foundSeparatorComma = true;
                }
                else
                {
                    freq += character;
                }
            }
            else
            {
                freqTable.insert(pair<const int, int>(stoi(asciiCode), stoi(freq)));

                asciiCode.clear();
                freq.clear();
                foundSeparatorColon = false;
                foundSeparatorComma = false;
            }

        }
        else
        {
            freqTable.insert(pair<const int, int>(PSEUDO_EOF, 1));
            break;
        }
    }


    encodingTree = buildEncodingTree(freqTable);
    decodeData(input, encodingTree, output);
    freeTree(encodingTree);
}

void freeTree(HuffmanNode* node) {
    if(node != nullptr)
    {
        freeTree(node->zero);
        freeTree(node->one);
        delete node;
    }
}

void mapRecursion(HuffmanNode* node, string& path, map<int, string>& encodingMap)
{
    if(node->isLeaf())
    {
        encodingMap.insert(std::make_pair(node->character, path));
    }
    else
    {
        if(node->zero)
        {
            string newPath = path;
            newPath += "0";
            mapRecursion(node->zero, newPath, encodingMap);
        }
        if(node->one)
        {
            string newPath = path;
            newPath += "1";
            mapRecursion(node->one, newPath, encodingMap);
        }
    }
}
