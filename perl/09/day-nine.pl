#!/usr/local/bin/perl

use strict;
use warnings;
use Data::Dumper qw(Dumper);

my $n;

alarm(1);
eval {
  local $SIG{ALRM} = sub { 
    $n = 3;

    die;
  };
  $n = <STDIN>;
};

my $f;

sub factorial {
  my $n = pop(@_);

  if ($n == 1) {
    return $n;
  }

  $f = factorial($n-1) * $n; 
  return $f;
}

my $r = &factorial($n);
print $r
