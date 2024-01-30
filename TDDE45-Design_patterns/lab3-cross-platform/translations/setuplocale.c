#include <stdlib.h>
#include <stdio.h>
#include <locale.h>

void setuplocale()
{
  /* Usually, the locale is taken from the user's environment.
   * We have hard-coded a locale for purposes of this lab.
   */
  char *newlocale, *targetLocale = "sv_SE.utf8";
  setenv("LANGUAGE", targetLocale, 1);
  setenv("LANG", targetLocale, 1);
  setenv("LC_MESSAGES", targetLocale, 1);
  newlocale = setlocale(LC_MESSAGES, targetLocale);
  if (newlocale == NULL) {
    fprintf(stderr, "Error: %s locale not installed (perhaps use a different hard-coded locale as a work-around)\n", targetLocale);
    exit(1);
  }
  printf("Set locale to: %s\n", newlocale);
}
