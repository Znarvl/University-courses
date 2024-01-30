all: unicode unicode.exe

unicode: unicode.c
	$(CC) -o $@ $<

unicode.exe: unicode.c
	x86_64-w64-mingw32-gcc -o $@ $<
