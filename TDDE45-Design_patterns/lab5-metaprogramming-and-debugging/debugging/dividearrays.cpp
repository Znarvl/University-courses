#include <random>

int main(int argc, char **argv)
{
  std::random_device generator;
  std::uniform_int_distribution<int> intdist(0,50);
  double res[1024];

  for (int i=0; i<1024; i++) {
    int nom = intdist(generator);
    int denom = intdist(generator);
    res[i] = nom / denom;
  }
  return 0;
}
