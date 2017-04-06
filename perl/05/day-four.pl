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

if ($integer % 2 != 0) {
  print "Weird"
} elsif ($integer % 2 == 0 && $integer > 1 && $integer < 6) {
  print "Not Weird"
} elsif ($integer % 2 == 0 && $integer > 5 && $integer < 21) {
  print "Weird"
} elsif ($integer % 2 == 0 && $integer > 20) {
  print "Not Weird"
}
