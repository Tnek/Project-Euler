#!/usr/bin/perl
my $x = 0;
for ($i = 1; $i < 100; $i++) {
    $x += $i**2;
}
print $x - 5050**2;
