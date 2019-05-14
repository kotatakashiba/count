#!/usr/bin/perl
use strict;
use warnings;
use autodie;
my $count_file = "test.dat";

##カウントファイルを読み込み
##ロックをかけるclose時にロックは解除される
open (my $fh, "<", $count_file);
flock ($fh,1);
$file_count = <$fh>;
close $fh;

$file_count++;

##カウントファイルへかける
##ロックをかけるclose時にロックは解除される
open (my $fh2, ">", $count_file);
flock ($fh2,2);
print $fh2 $file_count;
close $fh2;

print <<DOC;
Content-type:text/html; charset=utf-8;

<HTML>
<HEAD>
<TITLE>counter</TITLE>
</HEAD>
<BODY>
<h1>アクセスカウンター</h1>
アクセスカウンタ $file_count
</BODY>
</HTML>
DOC
exit;
