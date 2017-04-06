#!/usr/local/bin/perl

use strict;
use warnings;

my $meal;
my $tip;
my $tax;
my $total;

alarm(1);
eval {
  local $SIG{ALRM} = sub { 
    $meal = 100; 
    die;
  };
  $meal = <STDIN>;
};

alarm(1);
eval {
  local $SIG{ALRM} = sub { 
    $tip = 100; 
    die;
  };
  $tip = <STDIN>;
};

alarm(1);
eval {
  local $SIG{ALRM} = sub { 
    $tax = 9; 
    die;
  };
  $tax = <STDIN>;
};

$tip = $tip / 100;
$tax = $tax / 100;

print $tip;
print $tax;

