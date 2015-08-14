#!/usr/bin/perl -w

# Merge my router log with my Linux (ssh) auth log.

use strict;

open(CURL, "curl --user admin 'http://routerlogin.net/FW_log.htm' | ") || die "can't run curl: $!";

# Note that the only useful data in FW_log.htm is guaranteed to be in
# a readonly textarea where the useful lines start with a square
# bracket.

open(AUTHLOG, "< /var/log/auth.log") || die "can't open auth.log: $!";

open(OUTPUT, "| cat ") || die "can't set up output pipeline: $!"; # swap out cat for something better

while(<CURL>){
    next if not /\[/;
    s/.*(\[.*)/$1/; # just gets rid of html tags and whitespace
    print OUTPUT;
}

while(<AUTHLOG>){
    print OUTPUT if /sshd/;
}
