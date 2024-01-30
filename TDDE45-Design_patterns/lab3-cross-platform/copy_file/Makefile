SOURCE=马Häst马.txt

all: cpp-linux.txt win32.txt cpp-win32.txt qt.txt
	ls -lh $^

win32.txt: win32.exe $(SOURCE)
	rm -f $@
	wine $<
	test -f $@

win32.exe: win32.c
	x86_64-w64-mingw32-gcc -o $@ $<

cpp-win32.txt: cpp-win32.exe $(SOURCE)
	rm -f $@
	wine $< $@
	test -f $@

cpp-win32.exe: cpp17.cpp
	x86_64-w64-mingw32-g++ -o $@ -std=c++17 cpp17.cpp -static -lstdc++fs

cpp-linux.txt: cpp-linux $(SOURCE)
	rm -f $@
	./$< $@

cpp-linux: cpp17.cpp
	clang++ -Wall -std=c++17 -o $@ $< -lstdc++fs

qt.txt: QtCopyFile
	rm -f $@
	./$< $@

QtCopyFile: Makefile.qt qt.cpp
	$(MAKE) -f Makefile.qt

Makefile.qt: Qt.pro
	qmake -o $@ $<
