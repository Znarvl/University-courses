#include <stdio.h>
#include <string.h>
#include <stdlib.h>

namespace std {

static void getline(char *line, FILE *fin)
{
  int c = '\0', cur = 0;
  while (c != '\n' && (c = fgetc(fin)) != EOF) {
    line[cur++] = c;
  }
  line[cur] = '\0';
}

}

using namespace std;

int main(int argc, char **argv)
{
  int cur = 0;
  char *lines[65536];// made larger, to not get overflow 
  char line[1024]; // made larger, to not get overflow 
  // Fix num lines, num columns, strdup-1
  // FILE *fin = fopen("bi﻿ble.txt", "r+"); // bad char in file name, has ha byte order mark 
  FILE *fin = fopen("bible.txt", "r");
  while (!feof(fin)) {
    getline(line, fin);
    //lines[cur] = (char*) malloc(strlen(line)+1);
    lines[cur] = strdup(line);
    strcpy(lines[cur], line);
    cur++;
  }
  fclose(fin);
  FILE *fout = fopen("copy.txt", "w");
  for (int i=0; i<cur; i++) {
	  fputs(lines[i], fout);
    free(lines[i]); // free mem when done 
  }   
  fclose(fout);

  return 0;
}


// The point of the exercies is not to copy the file. So this is wrong 
int not_main(){  
  FILE *fin = fopen("bible.txt", "r");
  FILE *fout = fopen("copy.txt", "w");
  char cha; 
  if (fin != NULL){
    while((cha = fgetc(fin))!=EOF)
      fputc(cha, fout);
  }
  return 0;
}
