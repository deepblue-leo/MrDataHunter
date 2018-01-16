import json

class File:
    def __init__(self, file_name, remote_path, local_path):
        self.file_name = file_name
        self.remote_path = remote_path
        self.local_path = local_path

    def __repr__(self):
        return repr((self.file_name, self.remote_path, self.local_path))

class Host:
    def __init__(self, hostname, ip, username, password, file_name, remote_path, local_path):
        self.hostname = hostname
        self.ip = ip
        self.username = username
        self.password = password
        self.file = File(file_name, remote_path, local_path)

    def connect():
        pass

    def disconnect():
        pass

    def __repr__(self):
        return repr((self.hostname, self.ip, self.username, self.password, self.file.file_name, self.file.remote_path, self.file.local_path))


if __name__ == '__main__':
    hosts = [
        Host('bjt01', '10.190.130.91', 'sdc', 'adw2.0', '123.txt', '/usr/g/bin/', '/usr/MrDataHunter/store/'),
        Host('bjt02', '10.190.130.92', 'sdc', 'adw2.0', '456.txt', '/usr/g/bin/', '/usr/MrDataHunter/store/'),
        Host('bjt03', '10.190.130.93', 'sdc', 'adw2.0', '789.txt', '/usr/g/bin/', '/usr/MrDataHunter/store/'),
    ]

    json_str = json.dumps(hosts, default = lambda o: o.__dict__, sort_keys=True, indent=1)
    print  json_str

    new_hosts_rebuild = json.loads(json_str)
    print new_hosts_rebuild[1]['ip']

    new_host = Host(new_hosts_rebuild[0]['hostname'], new_hosts_rebuild[0]['ip'], new_hosts_rebuild[0]['username'], new_hosts_rebuild[0]['password'],
                    new_hosts_rebuild[0]['file']['file_name'], new_hosts_rebuild[0]['file']['remote_path'], new_hosts_rebuild[0]['file']['local_path'])
    new_host.hostname = 'bjt05'
    print new_host

