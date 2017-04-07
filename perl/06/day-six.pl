#!/usr/local/bin/perl

use strict;
use warnings;
use Data::Dumper qw(Dumper);

my $even;
my $i;
my $k;
my $odd;
my @s;
my $t;

alarm(1);
eval {
  local $SIG{ALRM} = sub { 
    $t = 2;

    @s[0] = "I firmly believe that any man's finest hour, the greatest fulfillment of all that he holds dear, is that moment when he has worked his heart out in a good cause and lies exhausted on the field of battle - victorious.";
    @s[1] = "There's no replacement for displacement.";

    die;
  };
  $t = <STDIN>;

  for ($i = 0; $i < $t; $i++) {
    @s[$i] = <STDIN>; 
  }
};

for ($i = 0; $i < $t; $i++) {
  my @v = split //, $s[$i];

  for (my $j = 0; $j < @v; $j++) {
    if ($j % 2 == 0) {
      $even = $even . $v[$j];
    } else {
      $odd = $odd . $v[$j];
    }
  }
  printf("%s %s\n", $even, $odd);
}
