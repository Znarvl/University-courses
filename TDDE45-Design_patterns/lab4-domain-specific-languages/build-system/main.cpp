int main(int argc, char **argv)
{
  /* TODO: dlopen does not exist on Windows and the filename will not be .so. */
  void *ptr = dlopen("libcopyfile.so", RTLD_LAZY);
  double d = cos(1.5);
}
