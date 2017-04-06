#!/usr/local/bin/perl
use strict;
use warnings;

print "Hello, World.\n";

my $text;
alarm(1);
eval {
  local $SIG{ALRM} = sub { die };
  $text = <STDIN>;
};

print $text;
