/* In case the C++-compiler is too old for std::filesystem */
#if __has_include(<filesystem>)
#include <filesystem>
namespace filesystem = std::filesystem;
#else
#include <experimental/filesystem>
namespace filesystem = std::experimental::filesystem;
#endif
#include <assert.h>

int main(int argc, char** argv)
{
  assert(argc==2); /* argv[1] is the destination file */
  filesystem::path p = filesystem::u8path(u8"马Häst马.txt");
  filesystem::path p2 = filesystem::u8path(argv[1]);// changed after semi now using argv for new path


  filesystem::copy(p,p2);

  return 0;
}
