#!/usr/bin/perl
sub prime
{
    for (my $i = 3; $i < sqrt($_[0]) + 1; $i++) {
        if ($_[0] % $i == 0) { return 0; }
    }
    return 1;
}
my $pcount = 1, $n = 3;
while ($pcount < 10001) {
    if (prime($n)) { $pcount++; }
    $n += 2;
}
print $n - 2;
