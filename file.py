class File:
    def __init__(self, file_name, remote_path, local_path):
        self._file_name = file_name
        self._remote_path = remote_path
        self._local_path = local_path

    def __repr__(self):
        return repr((self._file_name, self._remote_path, self._local_path))

    @property
    def file_name(self):
    	return self._file_name

    @file_name.setter
    def file_name(self, value):
    	self._file_name = value

    @property
    def remote_path(self):
    	return self._remote_path

    @remote_path.setter
    def remote_path(self, value):
    	self._remote_path = value

    @property
    def local_path(self):
    	return self._local_path

    @local_path.setter
    def local_path(self, value):
    	self._local_path = value
