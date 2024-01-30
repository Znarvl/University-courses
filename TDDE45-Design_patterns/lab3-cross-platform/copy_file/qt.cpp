#include <assert.h>
#include <QTextCodec>
#include <QFile>
#include <QIODevice>
#include <QString>


int main(int argc, char** argv)
{
  /* Make sure we use UTF-8 for file names; this is needed for the IDA labs */
  QTextCodec::setCodecForLocale(QTextCodec::codecForName("UTF-8"));
  // QTextCodec::setCodecForCStrings(QTextCodec::codecForName("UTF-8")); // Use this in Qt4
  assert(argc==2); /* argv[1] is the destination file */
  /* Your code here */
  QString p = QString::fromUtf8("马Häst马.txt");
  QString p2 = QString::fromUtf8(argv[1]); // changed after semi now using argv for new path


  QFile::copy(p, p2);

  return 0;
}
