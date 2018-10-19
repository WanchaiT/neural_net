#include <stdio.h>
void ee(char d); // prototype , parameter profile
int main(int argc, char const *argv[]) {
    ee('f');
    return 0;                  
}
void ee(char d){
    printf("%c\n",d );
}
