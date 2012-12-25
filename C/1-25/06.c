#include <stdio.h>
#include <math.h>
int main(int argc, char *argv[])
{
    int sqsum = 0, sumsq = 0, i, ans;
    for (i = 1; i <= 100; i++)
    {
        sqsum += i;
        sumsq += pow(i, 2);
    }
    ans = pow(sqsum, 2) - sumsq;
    printf("%d", ans);
}
