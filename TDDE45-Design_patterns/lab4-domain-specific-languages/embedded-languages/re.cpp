#include <fstream>
#include <iostream>
#include <regex>


void cpp_grep() {
  std::ifstream in1("file1.txt");
  std::string str;
  // TODO: Create a regular expression object; you don't want to create a new
  // object in each iteration of the loop
  std::regex re("[0-9]{7},([1]?[9]|2[2]?[0-3]),.*memory.*");

  while (std::getline(in1, str)) {
    // Print the lines matching the first regular expression
    std::smatch m;
    if (std::regex_search(str,m, re))
      std::cout << str << std::endl;
  }
}

void cpp_sed(std::string name, std::string rep) {
  std::ifstream in1("file2.txt");
  std::string str;
  // TODO: Create a regular expression object; you don't want to create a new
  // object in each iteration of the loop
  std::string expression = ".*"+ name + ".*";
  //std::regex re(expression);

  while (std::getline(in1, str)) {
    // Print the lines matching the first regular expression
    str = std::regex_replace(str, std::regex(expression), rep);
    std::cout << str << std::endl;

  }
}


int main(int argc, char** argv)
{
    cpp_grep();
    cpp_sed("Diana", "\"Diana\";2;U;");
    cpp_sed("Carl", "\"Carl\";2;U;");

}
