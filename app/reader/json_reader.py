import json
import os
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
    def list_directory(dirpath="/logs") -> (list[str], int):
        try:
            json_files = [file for file in os.listdir(dirpath) if file.endswith(".json")]
            n_of_files = len(json_files)

            leading_zeros = 0
            temp_n = n_of_files
            while temp_n >= 10:
                temp_n = temp_n // 10
                leading_zeros += 1

            print("Select JSON file:", leading_zeros)
            print('0'.rjust(leading_zeros+1, '0'), "| None")
            for i in range(n_of_files):
                print(str(i+1).rjust(leading_zeros+1, '0'), f"| {json_files[i]}")

            return json_files, n_of_files

        except FileNotFoundError:
            print(f"Error: Directory {dirpath} not found")
            return [], -1

        except Exception as e:
            print(f"Error listing files: {e}")
            return [], -1

    @staticmethod
    def read_json_data(filepath: str, dirpath="/logs") -> List[LXCItem]:
        lxc_items: List[LXCItem] = []

        with open(dirpath+"/"+filepath, 'r') as file:
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
