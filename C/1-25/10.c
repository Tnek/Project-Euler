#include <stdio.h>
#include <math.h>
int main(int argc, char *argv[])
{
    unsigned long int i, j, limit = 2000000, sum=0;
    int bool_list[limit];
    for (i=2; i < limit; i++)
        bool_list[i] = 1;
    for (i=2; i < sqrt(limit); i++) 
        if (bool_list[i])
            for (j=i*i; j <= limit; j += i)
                bool_list[j] = 0;
    for (i=2; i < limit; i++)
        if (bool_list[i])
            sum += i;
    printf("%lu", sum);
    return 0;
}
