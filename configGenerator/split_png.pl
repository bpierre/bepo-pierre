use diagnostics;
use utf8;
use warnings;
use strict;

use Config::IniHash;

# Usage: split_png.pl
my $origPng = 'results/layout.png';
my $layout = ReadINI 'results/layout.ini';

# And set these values
my $x0 = 14;
my $y0 = 212;
my $height = 102;
my $width = 296;
my $dist = 14;

# And these, too
my @states = split /:/, $layout->{global}->{shiftstates};
my $isExtendMode = (( $layout->{global}->{extend_key} ) ? 1 : 0 );
my $deadkeys = 20; # it is too much, but easier to delete, than count every time...


my @filenames;
foreach (@states) {
	push @filenames, 'state'.$_ if $_ != 2;
}
push @filenames, 'extend' if $isExtendMode;
foreach (1..$deadkeys)
{
	push @filenames, 'deadkey'.$_;
	push @filenames, 'deadkey'.$_.'sh';
}

unless ( $origPng ) {
	foreach ( <*.png> ) {
		if ( $origPng ) {
			die 'Two png files!';
		} else {
			$origPng = $_;
		}
	}
	unless ( $origPng ) {
		die 'There is no png file!';
	}
}

my $count = scalar @filenames;
foreach ( 0..@filenames-1 ) {
	my $filename = $filenames[$_];
	my $y = $y0 + ( $_ ) * ( $dist + $height );
	my $newPng = 'results/' . $filename . '.png';
	my $cmd = '"convert.exe" '.$origPng ." -crop ${width}x${height}+$x0+$y " . $newPng;
	print $filename."\n";
	system($cmd);
	if ( -s $newPng < 3000 ) {
		unlink $newPng;
		last;
	}
}
