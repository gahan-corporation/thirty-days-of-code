#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
  int read_int = 4;
  double read_dec = 8;
  char read_str[] = "Run's house";

  double add_int; 
  double add_dec;
  char add_str[];

  scanf("%[^\n]", read_int); 
  scanf("%[^\n]", read_dec); 
  scanf("%[^\n]", read_str); 

  add_int = read_int + add_int;
  printf("%\n", add_int);

  add_dec = read_dec + add_dec;
  printf("%\n", add_dec);

  add_str = strcat(read_str, " is the best place to learn and practice coding!";
  printf("%\n", add_str);

  return 0;
}
