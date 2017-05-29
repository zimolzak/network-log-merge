Network admin's ad-hoc tools
========================

Pull things from the web interface of a consumer Netgear router. Two
main scripts: `net-admin.pl` and `whos_attached.py`.

whos_attached.py
--------

Find out what devices are attached to the router. This Netgear router
for some reason generates an html doc with static JavaScript inside
it, which then gets run inside the browser to generate a table.

Usage:
    python3 whos_attached.py

net-admin.pl
--------

Merge my router's log (accessed via its internal Web server) with my
Linux auth.log.

I want to see which villains on the Internet are connecting through my
router, but I also need see what happens on the server *after* they
connect through the router.

I accomplish this by this process:

* Retrieve HTML log from the router.
* Keep only the log part of it; discard HTML.
* Parse this log so there's a date at beginning of each line.
* Open auth.log and keep anything relevant to sshd.
* Append those auth.log lines (which already have date) to router log.
* Sort. Result is somewhat nicely interleaved log lines.

Usage:

    ./net-admin.pl > log.txt
