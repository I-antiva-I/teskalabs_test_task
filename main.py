import json
from datetime import datetime
from typing import List

from mysql import connector

from database_access.database_access_control import DatabaseAccessControl
from reader.json_reader import JSONReader


DatabaseAccessControl.connect_to_database()

lxc_items = JSONReader.read_json_data()

for lxc_item in lxc_items:
    lxc_item_id = DatabaseAccessControl.insert_lxc_item(lxc_item)
    networks = lxc_item.get_networks()

    if networks:
        for network in networks:
            DatabaseAccessControl.insert_network(network, lxc_item_id)