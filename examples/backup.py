#!/usr/bin/python

import sys

from ib.shellsupport import CommandFailed, sh

def notify(nagioshost):
    sh("/usr/sbin/send_nsca -H monitor.host.tld -c /etc/send_nsca.cfg",
        stdin="%s\tbackup\t0\tOK:backup completed\n" % nagioshost)

def rsync(source, destination, excludes, logfile, rsyncoptions=None):
    if rsyncoptions is None:
        rsyncoptions = "-a -c -v --delete --stats"
    excludeoptions = "--exclude=".join(['%s ' %  x for x in (('',) + excludes)])
    fp = open(logfile, 'w')
    try:
        sh("rsync %s %s %s %s" % (rsyncoptions,
            excludeoptions, source, destination), stdout=fp)
    except CommandFailed, e:
        if e.code!=24:
            raise
    finally:
        fp.close()

def backup(source, destination, excludes, logfile, nagioshost):
    try:
        rsync(source, destination, excludes, logfile)
    except CommandFailed, e:
        print >>sys.stderr, "Rsync failed for %s with code %d" % (nagioshost, e.code)
        return False
    notify(nagioshost)
    return True

backup('/var/lib/vservers/X/', '/var/backups/nfsmount/vservers/X/',
    ('tmp/', 'var/tmp/'), '/var/log/backuplogs/X-rsync-backup.log', 'X')
