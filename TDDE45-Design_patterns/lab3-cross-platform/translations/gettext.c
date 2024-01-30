#include <libintl.h>
#include <locale.h>

void setup()
{
  /* Your code here. Setup a domain for gettext. */
  /* Use UTF-8 or gettext prints question marks for your Swedish letters */
  setlocale(LC_MESSAGES, "sv_SE.utf8");
  bindtextdomain("messages", "."); //
  bind_textdomain_codeset("messages", "utf8");
  textdomain("messages");
}
