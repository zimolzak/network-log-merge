#!/usr/bin/perl -w

# Merge my router log with my Linux (ssh) auth log.
# usage: ./net-admin.pl > log.txt

use strict;

open(CURL, "curl --silent --user admin 'http://routerlogin.net/FW_log.htm' | ") || die "can't run curl: $!";

# Note that the only useful data in FW_log.htm is guaranteed to be in
# a readonly textarea where the useful lines start with a square
# bracket.

open(AUTHLOG, "< /var/log/auth.log") || die "can't open auth.log: $!";

open(OUTPUT, "| sort ") || die "can't set up output pipeline: $!";

my $curl_lines = 0;
while(<CURL>){
    warn "Probably bad password!" if /unauth\.cgi/;
    next if not /\[/;
    next if /\[0/; # skip lines with JavaScript that contains bracket
    s/.*(\[.*)/$1/; # just gets rid of html tags and whitespace
    my @commasep = split(/,/);
    my $monthdate = $commasep[-2];
    my $yeartime = $commasep[-1];
    chomp $yeartime;
    $monthdate =~ s/ (...)\S* (\d+)/$1 $2/; # " August 13" --> "Aug 13"
    $yeartime =~ s/\d+ (\S+)/$1/; # "2015 19:45:43" --> "19:45:43"
    print OUTPUT "$monthdate $yeartime $_";
    $curl_lines++;
}

warn "Only $curl_lines good lines recd from router. Bad password?" if $curl_lines < 5;

while(<AUTHLOG>){
    print OUTPUT if /sshd/;
}
