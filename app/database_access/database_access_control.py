import os
from typing import List

import aiomysql
from aiomysql import Connection, Cursor, Pool

from models.lxc_item import LXCItem
from models.network import Network


class DatabaseAccessControl:
    # cursor: Cursor = None
    # connection: Connection = None

    pool: Pool = None

    @staticmethod
    async def close_connection():
        if DatabaseAccessControl.pool:
            DatabaseAccessControl.pool.close()
            await DatabaseAccessControl.pool.wait_closed()

    @staticmethod
    async def connect_to_database():
        DatabaseAccessControl.pool = await aiomysql.create_pool(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            db=os.getenv("DB_DATABASE"),
            port=3306,
            minsize=4,
            maxsize=32
        )

    @staticmethod
    async def insert_lxc_item(lxc_item: LXCItem) -> int:
        async with DatabaseAccessControl.pool.acquire() as connection:
            async with connection.cursor() as cursor:
                sql_query = ("INSERT INTO LXCItems (name, cpu_usage, memory_usage, created_timestamp, status) "
                             "VALUES (%s, %s, %s, %s, %s)")

                await cursor.execute(sql_query, lxc_item.as_query_parameters())
                await connection.commit()

                return cursor.lastrowid

    @staticmethod
    async def insert_network(network: Network, lxc_item_id: int) -> int:
        async with DatabaseAccessControl.pool.acquire() as connection:
            async with connection.cursor() as cursor:
                sql_query = ("INSERT INTO Networks (name, ip_address, lxc_item_id) "
                             "VALUES (%s, %s, %s)")

                await cursor.execute(sql_query, network.as_query_parameters(lxc_item_id))
                await connection.commit()
        
                return cursor.lastrowid


