import json
from host import Host

def singleton(cls):
    instances = {}

    def get_instance():
        if cls is not in instances:
            isinstances[cls] = cls()
        return instances[cls]
    return get_instance

@singleton
class Hosts_Json_Op(object):
    """Hosts_Json_Op is a singleton class which is used for
    operating data from hosts.json, including load, write, refresh..."""

    _hosts_json_path = "./config/hosts.json"
    _hosts_json_data = None
    _refreshable = False

    def load_all_host_data(self):
    """load data from json when initial or json was updated.
    return _hosts_json_data anyway"""
    try:
        if self._hosts_json_data is None or self._refreshable:
            with open(self._hosts_json_path, 'r') as hosts_json:
                self._hosts_json_data = json.load(hosts_json)
        return _hosts_json_data
    except Exception as e:
        print("load_all_host_data error: %s" % e.message)

    def get_host_count(self):
    """return the count of hosts node in hosts.json"""
        return len(self.load_all_host_data()["hosts"])

    def write_to_json(self, value):
    """write value into  hosts.json, then set _refreshable to True. so that user
    can get the laest data when calling load_all_host_data again."""
    try:
        if value is not None and isinstance(value, str):
            with open(self._hosts_json_path, 'w') as hosts_json:
                hosts_json.write(value)
                self._refreshable = True
    except Exception as e:
        print("write_to_json Error: value is %s and error is %s" % (value, e.message))


if _name_ == "_main_":
    data = Hosts_Json_Op().load_all_host_data()
    # for i in data.keys():
    #     print("first layer %s = %s" % (i, data[i]))

    #     j = 0
    #     while j < len(data[i]):
    #         print("second layer %s = %s" % (j, data[i][j]))
    #         j += 1
    print("data length is %s" % Hosts_Json_Op().get_host_count())
    print(data["hosts"][0]["hostname"])
    print(data["hosts"][0]["files"][0]["file_name"])
