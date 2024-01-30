#include <stdio.h>
#include <assert.h>
#include <errno.h>
#include <string.h>
#if defined(__MINGW32__) || defined(_MSC_VER)
#include <windows.h>
#endif
/*!
  Opens a file

  \param str a UTF8-encoded filename
  \param mode the mode argument of fopen
*/
FILE* my_fopen(char *filename, char *mode)
{
#if defined(_MSC_VER) || defined(__MINGW32__)
  /* Hint: You want to modify this code */
     int filename_len = strlen(filename);
     int mode_len  = strlen(mode);

     if(filename_len==0) return NULL;
     if(mode_len==0)return NULL;

     wchar_t path[256];
     wchar_t wmode[256];

     int new_file_len = MultiByteToWideChar(CP_UTF8, 0, filename, filename_len, path, filename_len);
     if(new_file_len>=256) return NULL;
     path[new_file_len] = L'\0';

     int new_mode_len = MultiByteToWideChar(CP_UTF8, 0, mode, mode_len, wmode, mode_len);
     if(new_mode_len>=256) return NULL;
     wmode[new_mode_len] = L'\0';

     return _wfopen(path, wmode);
#else
  /* Linux handles UTF-8 by default */

  return fopen(filename, mode);
#endif
}

int main(int argc, char **argv)
{
  FILE *f0, *f1, *f2;
  char *name1 = "teståäö", *name2 = NULL, *str = "Test\n";
  char buffer[256] = {0};
  size_t n;
  f0 = fopen("fileWithFileName", "r");
  assert(f0);
  assert(fgets(buffer, 255, f0));
  if (buffer[strlen(buffer)-1] == '\n') {
    buffer[strlen(buffer)-1] = '\0';
  }
  /* Should contain UTF-8 "马Häst马.txt" and no possibility to become a UTF-16 string by accident */
  name2 = strdup(buffer);
  fclose(f0);
  f1 = my_fopen(name1, "w");
  assert(f1);
  assert(fputs(str, f1) >= 0);
  fclose(f1);
  printf("%s now contains the string:\n%s", name1, str);

  f2 = my_fopen(name2, "r");
  if (!f2) {
    fprintf(stderr, "Failed to open file %s: %s\n", name2, strerror(errno));
    return 1;

  }
  n = fread(buffer, 1, 256, f2);
  printf("Read %ld units of 1 byte\n", (long) n);
  assert(n == 109);
  assert(0 == strncmp("Häst", buffer, 4));
  puts("The test file starts with the string \"Häst\"");
  return 0;
}
