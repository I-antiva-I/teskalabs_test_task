import os
from typing import List

from mysql import connector
from mysql.connector import MySQLConnection
from mysql.connector.abstracts import MySQLCursorAbstract, MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from models.lxc_item import LXCItem
from models.network import Network


class DatabaseAccessControl:
    cursor: MySQLCursorAbstract = None
    connection: MySQLConnection = None

    @staticmethod
    def connect_to_database():
        DatabaseAccessControl.connection = connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE"),
            port=3306,
        )
        DatabaseAccessControl.cursor = DatabaseAccessControl.connection.cursor()

    @staticmethod
    def insert_lxc_item(lxc_item: LXCItem) -> int:
        sql_query = ("INSERT INTO LXCItems (name, cpu_usage, memory_usage, created_timestamp, status) "
                     "VALUES (%s, %s, %s, %s, %s)")

        DatabaseAccessControl.cursor.execute(sql_query, lxc_item.as_query_parameters())
        DatabaseAccessControl.connection.commit()

        return DatabaseAccessControl.cursor.lastrowid

    @staticmethod
    def insert_network(network: Network, lxc_item_id: int) -> int:
        sql_query = ("INSERT INTO Networks (name, ip_address, lxc_item_id) "
                     "VALUES (%s, %s, %s)")

        DatabaseAccessControl.cursor.execute(sql_query, network.as_query_parameters(lxc_item_id))
        DatabaseAccessControl.connection.commit()

        return DatabaseAccessControl.cursor.lastrowid


