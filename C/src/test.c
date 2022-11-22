#include <stdio.h>

void green(){
    printf("\033[0;32m");
}
void red(){
    printf("\033[0;31m");
}
void reset(){
    printf("\033[0m");
}
int main ()
{
    red();
    printf("Hello, world!\n");
    green();
    printf("Hello, world!\n");
    reset();
    printf("Hello, world!\n");
    return 0;
}