from hosts_json_op import Hosts_Json_Op
from host import Host
from MrFile import MrFile

class Host_Manager(object):
	"""docstring for Host_Manager"""
	_hosts = {}

	def __init__(self, arg):
		super(Host_Manager, self).__init__()
		self.arg = arg

	def init_hosts(self):
	"""Init all host node"""
		pass