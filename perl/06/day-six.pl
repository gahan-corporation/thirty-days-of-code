#!/usr/local/bin/perl

use strict;
use warnings;

my $t;
my $i;
my $k;

alarm(1);
eval {
  local $SIG{ALRM} = sub { 
    my @s = qw(
      I firmly believe that any man's finest hour, the greatest fulfillment of all that he holds dear, is that moment when he has worked his heart out in a good cause and lies exhausted on the field of battle - victorious.
      There's no replacement for displacement.
    ); 
    die;
  };
  $integer = <STDIN>;
};

for ($i = 1; $i < 11; $i++) {
  $k = $i * $integer;
  print $integer . " x " . $i . " = " . $k . "\n";
}
