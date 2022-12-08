#include <QCoreApplication>
#include <map>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
    map<string, vector<string>> myMap;
    //vector<string> myVector;

    //myMap.insert(pair<string, vector<string>>("foo", vector<string>()));


    if(myMap["foo"].empty()) {
        myMap.insert(pair<string, vector<string>>("foo", vector<string>()));
    }

    myMap["foo"].push_back("bar");
    myMap["foo"].push_back("bar");
    myMap["foo"].push_back("bar");
    myMap["foo"].push_back("bar");

    for (vector<string>::const_iterator i = myMap["foo"].begin(); i != myMap["foo"].end(); i++) {
        cout << *i + "\n";
    }

    //cout << myMap["foo"][0];

//    myVector.push_back("bar");
//    myMap["foo"] = myVector;

//    myVector.push_back("baz");
//    myMap["foo"] = myVector;

//    for(vector<string>::const_iterator i = myVector.begin(); i != myVector.end(); i++) {
//        cout << myVector[i];
//        cout << *i << ' ';
//    }

//    for (int i = 0; i != myVector.size(); i++) {
//        cout << myVector[i] + " ";
//    }
//    //cout << myMap["foo"];
}
