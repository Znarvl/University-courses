all: lua-dsl re

lua-dsl: lua.c
	gcc -o $@ -Wall -I/usr/include/lua5.2 $< -llua5.2

re: re.cpp

clean:
	rm -f lua-dsl
