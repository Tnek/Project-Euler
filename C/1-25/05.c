#include <stdio.h>
int check(int x) 
{
    int i;
    for (i = 11; i <= 20; i++)
    {
        if (x % i != 0) {
            return 0;
        }
    }
    return 1;
}
int main(int argc, char *argv[])
{
    int i = 2520;
    while (check(i) != 1)
    {
        i += 2520;
    }
    printf("%d", i);
    return 0;
}
