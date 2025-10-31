from datetime import datetime
from typing import Tuple


class LXCItem:

    @staticmethod
    def __datetime_to_timestamp(created_time: str) -> int:
        return int(round(datetime.fromisoformat(created_time).timestamp()))

    def __init__(self, name: str, cpu_usage: int, memory_usage: int, status: str, created_at: str):
        self.__name: str = name
        self.__cpu_usage: int = -1 if (cpu_usage is None) else cpu_usage
        self.__memory_usage: int = -1 if (memory_usage is None) else memory_usage
        self.__created_timestamp: int = LXCItem.__datetime_to_timestamp(created_at)
        self.__status = status

    def as_list(self) -> list:
        return [self.__name, self.__cpu_usage, self.__memory_usage, self.__created_timestamp, self.__status]

    def is_valid(self):
        return True

    def __str__(self):
        return f"LXCItem ({self.__name}): CPU usage {self.__cpu_usage}; MEM usage {self.__memory_usage}; CTS {self.__created_timestamp}"