#include <stdio.h>
int main(int argc, char *argv[])
{
    int i, sum;
    sum = 0;
    for (i = 0; i < 1000; i ++)
    {
        if (i % 3 == 0 || i % 5 == 0)
        {
            sum += i;
        }
    }
    printf("%d", sum);
    return 0;
}
