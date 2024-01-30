#include <stdio.h>
#include <locale.h>
#include <libintl.h>
#include <stdlib.h>

void setup(); /* in gettext.c */
void setuplocale();

int main(int argc, char** argv)
{
  setuplocale();
  setup();
  puts(gettext("The current language is the default (C/POSIX)\n"));
  puts(gettext("The horse can run.\n"));
  puts(gettext("How fast can the horse run?\n"));
  puts(gettext("It typically runs at speed of less than 50 km/h.\n"));
  return 0;
}
