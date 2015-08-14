#!/usr/bin/perl -w
use strict;

open(CURL, "curl --user admin 'http://routerlogin.net/FW_log.htm' | ") || die "can't run curl: $!";

open(AUTHLOG, "< /var/log/auth.log") || die "can't open auth.log: $!";

open(OUTPUT, "| cat ") || die "can't set up output pipeline: $!"; # swap out cat for something better

while(<CURL>){
    print OUTPUT if s/.*(\[.*)/$1/;
}

while(<AUTHLOG>){
    print OUTPUT if /sshd/;
}
