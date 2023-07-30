#include <stdio.h>
#include <stdlib.h>
 
int main(int argc, char *argv[]) {
  FILE *cipher = fopen(argv[1], "rb");
  FILE *plain = fopen(argv[2], "wb");
  unsigned int seed = atoi(argv[3]);
  int c;
 
  srand(seed);
  c = (fgetc(cipher) & 0xff) ^ (rand() & 0xff);
  while (!feof(cipher)) {
    fputc(c, plain);
    c = (fgetc(cipher) & 0xff) ^ (rand() & 0xff);
  }
  fclose(plain);
  fclose(cipher);
}