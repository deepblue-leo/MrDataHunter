#!/usr/bin/python

import paramiko


class DataHunter(object):
    def __init__(self, hostname, ip, port, username, password):
        self.__hostname = hostname
        self._ip = ip
        self._port = port
        self._username = username
        self._password = password
        self.connector = None

    def connect(self):
        if self.connector is None:
            try:
                self.connector = paramiko.SSHClient()
                self.connector.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.connector.connect(self._ip, self._port, self._username, self._password)
                print 'connector setup'
            except Exception as e:
                print("Connect error: %s" % e.message())

        #return self.connector

    def put(self, local_file, remote_dir):
        try:
            sftp = paramiko.SFTPClient.from_transport(self.connector.get_transport())
            sftp.put(local_file, remote_dir)
            print('put %s to %s ok' % (local_file, remote_dir))
        except Exception as e:
            print("put error: %s" % e.message)

    def get(self, remote_file, local_dir):
        try:
            sftp = paramiko.SFTPClient.from_transport(self.connector.get_transport())
            sftp.get(remote_file, local_dir)
            print('get %s from %s ok' % (local_dir, remote_file))
        except Exception as e:
            print("get error: %s" % e.message)

    def close(self):
        if self.connector is not None:
            self.connector.close()
            print 'connector closed'


if __name__ == "__main__":
    datahunter = DataHunter('bjt01', '10.189.130.181', 22, 'sdc', 'adw2.0')
    datahunter.connect()
    datahunter.get('/export/home/sdc/imcomb.tar.Z', 'c:/temp/imcomb.tar.Z.123')
    datahunter.put('c:/temp/imcomb.tar.Z.123', '/export/home/sdc/123.sample')
    datahunter.close()