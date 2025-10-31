class Network:
    def __init__(self, name: str, ip_address: str):
        self.__name: str = name
        self.__ip_address: str = ip_address

    def as_list(self) -> list:
        return [self.__name, self.__ip_address]

    def is_valid(self):
        return True

    def __str__(self):
        return f"Network ({self.__name}): IP {self.__ip_address}"
