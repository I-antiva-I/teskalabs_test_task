import json
import os
import time
from datetime import datetime
from typing import List

from database_access.database_access_control import DatabaseAccessControl
from reader.json_reader import JSONReader

print("Script started!")



json_files, n_of_files = JSONReader.list_directory("../logs/")

if n_of_files == -1:
    exit(-1)
else:
    file_index = min(max(int(input()), 0), n_of_files)
    if file_index == 0:
        exit(0)
    else:
        selected_file = json_files[file_index-1]

start = time.perf_counter()
DatabaseAccessControl.connect_to_database()
lxc_items = JSONReader.read_json_data(selected_file)

for lxc_item in lxc_items:
    if lxc_item.is_valid():
        lxc_item_id = DatabaseAccessControl.insert_lxc_item(lxc_item)
        networks = lxc_item.get_networks()

        if networks:
            for network in networks:
                if network.is_valid():
                    DatabaseAccessControl.insert_network(network, lxc_item_id)

end = time.perf_counter()
print(f"Time passed: {end - start:.3f} s")