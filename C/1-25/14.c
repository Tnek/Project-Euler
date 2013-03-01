#include <stdio.h>
long int seq(long int n, long int c)
{
    if (n == 1)
        return c;
    if (n % 2 == 0) {
        return seq(n/2, ++c);
    } else
        return seq(3*n + 1, ++c);
}


int main(int argc, char *argv[])
{
    long int i, temp, maxnum, maxseq=10;
    for (i = 2; i < 1000000; i++)
    {
        temp = seq(i, 0);
        if (temp > maxseq) {
            maxnum = i;
            maxseq = temp;
        }
    }
    printf("%d", maxnum);
    return 0;
}
