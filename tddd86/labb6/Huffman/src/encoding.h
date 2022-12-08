/*
 * TDDD86 Huffman Encoding
 * This file declares the functions that you will need to write in this
 * assignment for your Huffman Encoder in huffmanencoding.cpp.
 *
 * Please do not modify this provided file. Your turned-in files should work
 * with an unmodified version of all provided code files.
 */

#ifndef _encoding_h
#define _encoding_h

#include <iostream>
#include <string>
#include <map>
#include "bitstream.h"
#include "HuffmanNode.h"
using namespace std;

/*
 * See huffmanencoding.cpp for documentation of these functions
 * (which you are supposed to write, based on the spec).
 */

/*
 * builds a table of pairs with ascii letters and how frequent they appear
 */
map<int, int> buildFrequencyTable(istream& input);

/*
 * Creates the huffman tree structure
 */
HuffmanNode* buildEncodingTree(const map<int, int>& freqTable);

/*
 * Creates a table of binary numbers to coresponding ascii letter based on the huffman tree's
 * structure
 */
map<int, string> buildEncodingMap(HuffmanNode* encodingTree);

/*
 * Converts data to binary with help from huffman table
 */
void encodeData(istream& input, const map<int, string>& encodingMap, obitstream& output);

/*
 * Decodes a binary string and retrives the original data
 */
void decodeData(ibitstream& input, HuffmanNode* encodingTree, ostream& output);

/*
 * Creates a compressed version of the specifed data with a header containing
 * the frequency table
 *
 */
void compress(istream& input, obitstream& output);

/*
 * Takes compressed data and restores the data to the original state
 * using the header
 */
void decompress(ibitstream& input, ostream& output);

/*
 * Deletes nodes in a tree until its gone to free up memory
 */
void freeTree(HuffmanNode* node);

/*
 * Recursive function that retrives the trees path to (all) leafs to be used
 */
void mapRecursion(HuffmanNode* node, string& path, map<int, string>& encodingMap);

#endif
