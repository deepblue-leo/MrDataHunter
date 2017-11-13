class MrFile(object):
	"""the mapping of file node in hosts.json"""
	def _init_(self, filename, remote_path, local_path):
		super(ClassName, self)._init_()
		self._filename = filename
		self._remote_path = remote_path
		self._local_path = local_path

	@property
	def filename(self):
	"""filename is a readonly property"""
		return self._filename

	@property
	def remote_path(self):
		return self._remote_path

	@remote_path.setter
	def filename(self, value):
		if not isinstance(value, str):
			raise TypeError("remote_path value must be a string")
		self._remote_path = value

	@property
	def local_path(self):
		return self._local_path

	@local_path.setter
	def local_path(self, value):
		if not isinstance(value, str):
			raise TypeError("local_path value must be a string")
		self._local_path = value