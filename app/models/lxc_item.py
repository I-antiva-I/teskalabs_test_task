from datetime import datetime
from typing import Tuple, List

from models.network import Network


class LXCItem:

    @staticmethod
    def __datetime_to_timestamp(created_time: str) -> int:
        return -1 if created_time is None else int(round(datetime.fromisoformat(created_time).timestamp()))

    def __init__(self, name: str, cpu_usage: int, memory_usage: int, status: str, created_at: str):
        self.__name: str = "I have no name" if (name is None) else name
        self.__cpu_usage: int = -1 if (cpu_usage is None) else cpu_usage
        self.__memory_usage: int = -1 if (memory_usage is None) else memory_usage
        self.__created_timestamp: int = LXCItem.__datetime_to_timestamp(created_at)
        self.__status = "NONE" if (status is None) else status
        self.__networks = []

    def add_network(self, network: Network):
        self.__networks.append(network)

    def get_networks(self) -> List[Network]:
        return self.__networks

    def as_query_parameters(self) -> list:
        return [self.__name, self.__cpu_usage, self.__memory_usage, self.__created_timestamp, self.__status]

    def is_valid(self):
        return True

    def __str__(self):
        return f"LXCItem ({self.__name}): CPU usage {self.__cpu_usage}; MEM usage {self.__memory_usage}; CTS {self.__created_timestamp}"