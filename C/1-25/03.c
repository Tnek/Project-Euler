#include <stdio.h>
#include <math.h>

int prime_check(int n)
{
    int i;
    for (i = 3; i <= sqrt(n); i += 2) 
        if (n % i == 0) 
            return 0;
    return 1;
}

int main(int argc, char *argv[])
{
    long n = 600851475143;
    long i;
    for (i = sqrt(n) - 1; i > 3; i -= 2) 
        if (n % i == 0 && prime_check(i)) {
            printf("%d", i);
            break;
    }
    return 0;
}
