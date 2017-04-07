#!/usr/local/bin/perl

use strict;
use warnings;
use Data::Dumper qw(Dumper);

my $t;

alarm(1);
eval {
  local $SIG{ALRM} = sub { 
    $t = 10;

    die;
  };

  $t = <STDIN>;

};

