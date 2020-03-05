#include <stdio.h>
#include <string.h> 

void test1(int c[]) 
{
  c[0] = 9;
}

void test2(int c)
{
  c = 9;
}

int main (int argc, char *argv[]) 
{
  //////////////////////////////////////////////////////////////
  // C does not exist string, it is the same thing as byte array.
  // Look at this
  char cArr[] = {'a','b','c','d'};
  char sArr[] = "abcd";

  // sizeof is not a function, it's operator. 
  printf("cArr's length is %d\n", sizeof(cArr));
  printf("sArr's length is %d\n", sizeof(sArr));

  printf("cArr's length is %d\n", strlen(cArr));
  printf("sArr's length is %d\n", strlen(sArr));

  printf("cArr is %s\n", cArr);
  printf("cArr[0] is %c\n",cArr[0]);
  printf("sArr is %s\n", sArr);
  // the sArr sizeof isn't 4,because sArr is a string, it will
  // add a '\0' at the end.
  //////////////////////////////////////////////////////////////

  //////////////////////////////////////////////////////////////
  int a[3] = {10,0,0};
  int b[3] = {10,0,0};
  // put a not put a[0],so u can see the difference
  test1(a);
  test2(b[0]);

  printf("a[0] is %d\n",a[0]);
  printf("b[0] is %d\n",b[0]);

  //////////////////////////////////////////////////////////////
  
  /////////////////////////////////////////////////////////////
  // u must know why #include and the *.h file how to build
  // #include "" and #include <>
  // compile,link,and final create a executable
  /////////////////////////////////////////////////////////////



  return 0;


}
