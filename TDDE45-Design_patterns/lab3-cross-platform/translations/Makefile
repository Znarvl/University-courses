.PHONY: qt-linguist

all: gettext-main.c linguist-main.cpp gettext qt-linguist

gettext: gettext-main.c setuplocale.c gettext.c

qt-linguist: Makefile.linguist
	$(MAKE) -f Makefile.linguist

Makefile.linguist: Linguist.pro
	qmake -o $@ $<
