#include <windows.h>
#include <assert.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  assert(argc==1);

  wchar_t * src =  L"马Häst马.txt";
  wchar_t * dest = L"win32.txt";


  CopyFileW(src, dest, FALSE);

  return 0;
}
