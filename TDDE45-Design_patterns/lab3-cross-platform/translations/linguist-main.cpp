#include <stdio.h>
#include <QCoreApplication>
#include <QTranslator>
#include <QObject>


extern "C" void setuplocale();

class TestTranslation : public QCoreApplication /* an application without GUI */
{
public:
  TestTranslation(int argc, char** argv) : QCoreApplication(argc, argv)
  {
    /* Install a translator */
    /* Mark strings for translation and use linguist to create translation files.
     * Output the translated strings
     *  */

     QCoreApplication app(argc, argv);
     QTranslator translator;

     translator.load("example_sv", ".");
     app.installTranslator(&translator);



     puts(QObject::tr("The current language is the default (C/POSIX)\n").toUtf8());
     puts(QObject::tr("The horse can run.\n").toUtf8());
     puts(QObject::tr("How fast can the horse run?\n").toUtf8());
     puts(QObject::tr("It typically runs at speed of less than 50 km/h.\n").toUtf8());
  }
};

int main(int argc, char** argv)
{
  setuplocale();
  TestTranslation test(argc, argv);
  return 0;
}
