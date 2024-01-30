#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#include "lua.h"
#include "lualib.h"
#include "lauxlib.h"

static double fromC(double v)
{
  return -v;
}

static int fromCLuaWrapper(lua_State* L)
{
  // this function wrapps the fromC function
  // so that it will interact with the lua API
  double v = luaL_checknumber(L,1);
  lua_pushnumber(L, fromC(v));
  return 1;
}


int main ( int argc, char *argv[] )
{
    int status, result;

    lua_State *L;

    /* initialize Lua */
    L = luaL_newstate();

    /* load Lua base libraries */
    luaL_openlibs(L);

    /* TODO: load and run the test.lua file */


    luaL_dofile(L, "test.lua");

    lua_pushcfunction(L, fromCLuaWrapper);
    lua_setglobal(L, "fromC");

    /* TODO: Call the lua version of the addFromC function from test.lua */
    lua_getglobal(L, "addFromC");
    lua_pushnumber(L, 41);
    lua_pushnumber(L, 22);
    lua_call(L, 2, 1);

    int res = (int)lua_tointeger(L, -1);
    printf("%i\n", res);
    lua_pop(L, 1);

    /* cleanup Lua */
    lua_close(L);

    return 0;
}
