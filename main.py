import json
from datetime import datetime
from typing import List

from mysql import connector

from database_access.database_access_control import DatabaseAccessControl
from reader.json_reader import JSONReader


DatabaseAccessControl.connect_to_database()

lxc_items, lxc_items_networks = JSONReader.read_json_data()

print(len(lxc_items), len(lxc_items_networks))
n = len(lxc_items)

for i in range(n):
    lxc_item_id = DatabaseAccessControl.insert_lxc_item(lxc_items[i])
    # print(lxc_items[i])
    networks_ids = []
    for network in lxc_items_networks[i]:
        # print("\t", network)
        networks_ids.append(DatabaseAccessControl.insert_network(network))

    for networks_id in networks_ids:
        DatabaseAccessControl.insert_lxc_item_network(lxc_item_id, networks_id)