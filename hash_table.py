class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f'(key:{self.key}, value:{self.value}, next -> {self.next})'


class HashTable:
    def __init__(self):
        self.data = dict()

    def hash_f(self, key):
        return str(key)[0].upper()

    def add_update_key_value(self, key, value):
        hashed_key = self.hash_f(key)
        
        if hashed_key in self.data.keys():
            previous_cell = None
            current_cell = self.data[hashed_key]
            while current_cell is not None and current_cell.key != key:
                previous_cell = current_cell
                current_cell = current_cell.next
            if current_cell is not None:
                current_cell.value = value
                return
            else:
                previous_cell.next = Node(key, value)
        else:
            self.data[hashed_key] = Node(key, value)

    def get_value_by_key(self, key):
        hashed_key = self.hash_f(key)
        if hashed_key in self.data.keys():
            current_cell = self.data[hashed_key]
            while current_cell is not None and current_cell.key != key:
                current_cell = current_cell.next
            if current_cell is not None:
                return current_cell.value
        return None

    def remove_value_by_key(self, key):
        hashed_key = self.hash_f(key)
        if hashed_key in self.data.keys():
            previous_cell = None
            current_cell = self.data[hashed_key]
            while current_cell is not None and current_cell.key != key:
                previous_cell = current_cell
                current_cell = current_cell.next
            if current_cell is not None:
                if current_cell.next:
                    previous_cell.next = current_cell.next
                else:
                    previous_cell.next = None
        return None

    def __str__(self):
        for k, v in self.data.items():
            print(f'{k} -> {v}')
        return ''


if __name__ == '__main__':
    ht = HashTable()
    ht.add_update_key_value('John', 1)
    ht.add_update_key_value('Smith', 2)
    ht.add_update_key_value('Mask', 3)
    ht.add_update_key_value('Mila', 4)
    ht.add_update_key_value('jack', 5)
    ht.add_update_key_value('Nick', 6)
    ht.add_update_key_value('jastin', 7)
    ht.add_update_key_value('Name', 8)
    print(ht)
    ht.add_update_key_value('Jack', 555)
    print(ht)
    ht.remove_value_by_key('jack')
    print(ht)
