#!/usr/bin/perl
sub div 
{
    for (my $i = 11; $i <= 20; $i++) {
        if ($_[0] % $i != 0) { return 1; }
    }
    return 0;
}
my $n = 2520;
while (&div($n) ) { $n += 2520; }
print "$n";
