#!/usr/local/bin/perl

use strict;
use warnings;

my $i = 4;
my $d = 4.0;
my $s = 'HackerRank ';

# Declare second integer, double, and String variables.
my $int = 0;
my $dec = 0.0;
my $str = "";

# Read and save an integer, double, and String to your variables.
alarm(5);
eval {
  local $SIG{ALRM} = sub { die };
  $int = <STDIN>;
};

alarm(5);
eval {
  local $SIG{ALRM} = sub { die };
  $dec = <STDIN>;
};

alarm(5);
eval {
  local $SIG{ALRM} = sub { die };
  $str = <STDIN>;
};

# Print the sum of both integer variables on a new line.
$int = $i + $int;
print $int."\n";

# Print the sum of the double variables on a new line.
$dec = $d + $dec;
printf("%.1f\n", $dec);

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print $s.$str;
