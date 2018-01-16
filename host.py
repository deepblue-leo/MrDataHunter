from file import File
import json

class Host(object):
    """the mapping to the individual node in hosts.json"""

    def __init__(self, hostname, ip, username, password, file_name, remote_path, local_path):
        self._hostname = hostname
        self._ip = ip
        self._username = username
        self._password = password
        self._file = File(file_name, remote_path, local_path)

    def connect(self):
        pass

    def disconnect(self):
        pass

    def __repr__(self):
        return repr((self.hostname, self.ip, self.username, self.password, self._file.file_name, self._file.remote_path, self._file.local_path))

    @property
    def hostname(self):
        return self._hostname

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        if not isinstance(value, str):
            raise TypeError("ip value must be a string!")
        self._ip = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise TypeError("login_name value must be a string!")
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("password value must be a string!")
        self._hostname = value




if __name__ == '__main__':
    hosts = [
        Host('bjt01', '10.190.130.91', 'sdc', 'adw2.0', '123.txt', '/usr/g/bin/', '/usr/MrDataHunter/store/'),
        Host('bjt02', '10.190.130.92', 'sdc', 'adw2.0', '456.txt', '/usr/g/bin/', '/usr/MrDataHunter/store/'),
        Host('bjt03', '10.190.130.93', 'sdc', 'adw2.0', '789.txt', '/usr/g/bin/', '/usr/MrDataHunter/store/'),
    ]

    json_str = json.dumps(hosts, default = lambda o: o.__dict__, sort_keys=True, indent=1)
    print  json_str

    new_hosts_rebuild = json.loads(json_str)
    print new_hosts_rebuild[1]['_ip']

    new_host = Host(new_hosts_rebuild[0]['_hostname'], new_hosts_rebuild[0]['_ip'], new_hosts_rebuild[0]['_username'], new_hosts_rebuild[0]['_password'],
                    new_hosts_rebuild[0]['_file']['_file_name'], new_hosts_rebuild[0]['_file']['_remote_path'], new_hosts_rebuild[0]['_file']['_local_path'])
    new_host.ip = "10.190.130.99"
    print new_host