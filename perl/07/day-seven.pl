#!/usr/local/bin/perl

use strict;
use warnings;
use Data::Dumper qw(Dumper);

my $i;
my $k;
my $s;
my $t;

alarm(1);
eval {
  local $SIG{ALRM} = sub { 
    $t = 10;

    $s = "8 2 0 1 5 8 6 1 9 2";

    die;
  };
  $t = <STDIN>;

  for ($i = 0; $i < $t; $i++) {
    @s[$i] = <STDIN>; 
  }
};

