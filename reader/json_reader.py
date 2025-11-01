import json
from typing import List, Tuple

from models.lxc_item import LXCItem
from models.network import Network


class JSONReader:
    @staticmethod
    def get_inner_key(data, keys: List[str], default=None):
        for key in keys:
            if isinstance(data, dict) and key in data:
                data = data[key]
            else:
                return default
        return data

    @staticmethod
    def read_json_data(filepath: str = "sample-data.json") -> List[LXCItem]:
        lxc_items: List[LXCItem] = []

        with open(filepath, 'r') as file:
            json_data = json.load(file)
            for item in json_data:
                # LXC
                name = item.get("name", None)
                cpu_usage = JSONReader.get_inner_key(item, ["state", "cpu", "usage"])
                memory_usage = JSONReader.get_inner_key(item, ["state", "memory", "usage"])
                status = item.get("status", None)
                created = item.get("created_at", None)

                lxc_item = LXCItem(name, cpu_usage, memory_usage, status, created)

                # IPs
                nets = JSONReader.get_inner_key(item, ["state", "network"])
                if nets:
                    for net in nets:
                        ips = JSONReader.get_inner_key(nets[net], ["addresses"])
                        if ips:
                            for ip in ips:
                                network = Network(net, ip.get("address", None))
                                lxc_item.add_network(network)

                lxc_items.append(lxc_item)

        return lxc_items
