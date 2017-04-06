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
