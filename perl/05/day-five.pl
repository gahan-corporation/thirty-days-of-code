#!/usr/local/bin/perl

use strict;
use warnings;

my $integer;

alarm(1);
eval {
  local $SIG{ALRM} = sub { 
    $integer = 20; 
    die;
  };
  $integer = <STDIN>;
};

for ($i = 1; $i < 11; $i++) {
  $k = $i * $integer;
  print $integer . " x " . $i . " = " . $k;
}
