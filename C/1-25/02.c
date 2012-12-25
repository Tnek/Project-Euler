#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[])
{
    printf("%f", (((pow(((1 + sqrt(5)) / 2), 35) + pow(((1 - sqrt(5))/2), 35)) / sqrt(5)) - 1) / 2);
    return 0;
}
