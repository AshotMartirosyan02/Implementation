from hash_node import Node
from typing import Any


class HashTable:
    def __init__(self, size = 20):
        self.size = size
        self.table = [None] * size

    def __str__(self) -> str:
        ls = []
        for i in range(self.size):
            curent = self.table[i]
            while curent:
                ls.append(f"{curent.key}: {curent.value}")
                curent = curent.next
        return "{" + ",   ".join(ls) + "}"

    def __hash_function(self, key:Any) -> int:
        return hash(key) % self.size

    def put(self, key: Any, value: Any)-> None:
        node = Node(key, value)
        hash_key = self.__hash_function(key)
        if self.table[hash_key] is None:
            self.table[hash_key] = node
        else:
            curent = self.table[hash_key]
            while curent.next:
                if curent.key == key:
                    curent.value = value
                    return
                curent = curent.next
            if curent.key == key:
                curent.value = value
            else:
                curent.next = node

    def get(self, key: Any):
        hash_key = self.__hash_function(key)
        curent = self.table[hash_key]
        while curent:
            if curent.key == key:
                return curent.value
            curent = curent.next
        return None

    def remove(self, key: Any) -> str:
        hash_key = self.__hash_function(key)
        curent = self.table[hash_key]
        ancac = None
        while curent:
            if curent.key == key:
                if ancac:
                    ancac.next = curent.next
                else:
                    self.table[hash_key] = curent.next
                return f"Delete elements"
            ancac = curent
            curent = curent.next
        return f"Not found"
