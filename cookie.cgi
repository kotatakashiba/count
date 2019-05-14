#!/usr/bin/perl

use strict;
use warnings;
use autodie;

my $COOKIENAME = "count";
my $COOKIELIFE = 10;
my $count = 0;

# クッキーデータ取り込み
foreach $cookie_line (split(/;\s*/, $ENV{'HTTP_COOKIE'})) {
    my ($name, $cookie) = split(/=/, $cookie_line);
    if($name eq $COOKIENAME) {
        $count = $cookie;
        last;
    }
}
# クッキーデータ作成
$count++; 
my @mon = qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec);
my @wdy = qw(Sun Mon Tue Wed Thu Fri Sat);
my $life = $COOKIELIFE * 24 * 60 * 60;
($sec, $min, $hour, $day, $mon, $year, $wday) = gmtime(time + $life);
my $expires = sprintf("%s, %02d-%s-%04d %02d:%02d:%02d GMT", $wdy[$wday], $day, $mon[$mon], $year + 1900, $hour, $min, $sec);

# HTML出力
print "Content-type: text/html; charset=utf-8\n";
print "Set-Cookie: $COOKIENAME=$count; expires=$expires;\n\n";
print "<html>\n";
print "<head>\n";
print "<title>訪問回数</title>\n";
print "</head>\n";
print "<body>\n";
print " $count回目の訪問です<br>\n";
print "</body>\n";
print "</html>\n";
