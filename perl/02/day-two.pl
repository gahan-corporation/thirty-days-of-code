#!/usr/local/bin/perl

use strict;
use warnings;
use POSIX qw(ceil);

my $meal;
my $tip;
my $tax;
my $total;

alarm(1);
eval {
  local $SIG{ALRM} = sub { 
    $meal = 10.25; 
    die;
  };
  $meal = <STDIN>;
};

alarm(1);
eval {
  local $SIG{ALRM} = sub { 
    $tip = 17; 
    die;
  };
  $tip = <STDIN>;
};

alarm(1);
eval {
  local $SIG{ALRM} = sub { 
    $tax = 5; 
    die;
  };
  $tax = <STDIN>;
};

$tip = $meal * ($tip / 100);
$tax = $meal * ($tax / 100);

$total = ceil($meal + $tip + $tax);

printf("The total meal cost is %i dollars.", $total); 
