#include <stdio.h>

int main(void)
{
    int c;
    scanf("%d", &c);

    int co = 0;

    co = co + c / 25;
    c = c % 25;

    co = co + c / 10;
    c = c % 10;

    co = co + c / 5;
    c = c % 5;

    co = co + c / 1;
    c = c % 1;

    printf("%d\n", co);
}
