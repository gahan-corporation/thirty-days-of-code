#!/usr/local/bin/perl

use strict;
use warnings;
use Data::Dumper qw(Dumper);

my $i;
my $k;
my @s;
my $t;

alarm(1);
eval {
  local $SIG{ALRM} = sub { 
    $t = 10;

    push(@s, "sam 99912222");
    push(@s, "tom 11122222");
    push(@s, "harry 12299933");
    push(@s, "sam");
    push(@s, "edward");
    push(@s, "harry"); 

    die;
  };
  $t = <STDIN>;

  while (1) {
    $i = <STDIN>;
    
    push(@s, $i);

    last if $i eq '';
  }
};

print Dumper (\@s);
