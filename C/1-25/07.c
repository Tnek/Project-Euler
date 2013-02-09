#include <stdio.h>
#include <math.h>
int prime(int n)
{
    int i;
    for (i = 3; i < sqrt(n) + 1; i+= 2)
        if (n % i == 0)
            return 0;
    return 1;
}

int main(int argc, char *argv[])
{
    unsigned long long int i, pcount = 1;
    for (i = 3; pcount < 10001; i += 2)
        if (prime(i))
            pcount++;
   printf("%d\n", i-2);
}
