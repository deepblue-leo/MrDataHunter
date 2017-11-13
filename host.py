
class Host(object):
    """the mapping to the individual node in hosts.json"""

    def _init_(self, hostname, ip, username, password, file_dict):
        """init host with parameters, file_dict.key is hunting_file, file_dict.value is store_location"""
        self._hostname = hostname
        self._ip = ip
        self._username = username
        self._password = password

        self._file_dict = {}
        self._file_dict = file_dict

    @property
    def hostname(self):
    """hostname is a readonly property"""
        return self._hostname

    # @hostname.setter
    # def hostname(self, value):
    #     if not isinstance(value, str):
    #         raise TypeError("hostname value must be a string!")
    #     self._hostname = value

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

    @property
    def file_dict(self):
        return self._file_dict

    def add_A_mrfile(self, aMrFile):
        self._file_dict[aMrFile._filename] = aMrFile


    def del_A_mrfile(self, filename):
        if filename in self._file_dict.keys():
            self._file_dict.pop(filename)

    def update_A_mrfile(self, aMrFile):
        if aMrFile.filename in self._file_dict.keys():
            sef._file_dict[aMrFile.filename] = aMrFile
        else:
            self.add_A_mrfile(aMrFile)
