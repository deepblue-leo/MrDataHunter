import argparse
import getpass

import paramiko

SOURCE = "/Users/leo/SogouQ.mini.tar.gz"
DESTINATION = "/Users/leo/tmp/SogouQ.mini.tar.gz"


def copy_file(hostname, port, username, password, src, dst):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print "Connecting to %s \n with username %s...\n" % (hostname, username)
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    print "Copying file: %s to path: %s" % (src, dst)
    sftp.put(src, dst)
    sftp.close()
    t.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remote file copy')
    parser.add_argument('--host', action="store", dest="host", default='localhost')
    parser.add_argument('--port', action='store', dest="port", default=22, type=int)
    parser.add_argument('--src', action='store', dest="src", default=SOURCE)
    parser.add_argument('--dst', action="store", dest="dst", default=DESTINATION)

    given_args = parser.parse_args()

    hostname, port = given_args.host, given_args.port
    src, dst = given_args.src, given_args.dst
    username = raw_input("Enter your username:")
    password = getpass.getpass("Enter password for %s: " % username)

    copy_file(hostname, port, username, password, src, dst)
