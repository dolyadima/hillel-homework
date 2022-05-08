from random import randint


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f'<k:{self.key}|v:{",".join(self.value) if isinstance(self.value, list) else self.value}|next:{self.next is not None}>'


class HashTable:
    def __init__(self, init_capacity=15):
        self.capacity = init_capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash_func(self, key):
        hash = 0
        for index, char in enumerate(key):
            hash += (index + len(key)) ** ord(char)
            hash = hash % self.capacity
        return hash

    def add_key_value(self, key, value):
        self.size += 1
        index = self.hash_func(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def find_value_by_key(self, key):
        index = self.hash_func(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def __getitem__(self, item):
        return self.find_value_by_key(item)

    def remove_value_by_key(self, key):
        index = self.hash_func(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next
            return result

    def __str__(self):
        result = ''
        for i, bucket in enumerate(self.buckets):
            if bucket is not None:
                result += f'bucket-{str(i).zfill(2)}: {bucket}'
                count = 1
                prev = bucket
                while prev.next is not None:
                    curr = prev.next
                    result += f', {curr}'
                    count += 1
                    prev = curr
                result += f' ({count})\n'
            else:
                result += f'bucket-{str(i).zfill(2)}: <>\n'
        return result


def generate_test_data(hashtable_obj, count=20):
    for num in range(count):
        rand_int = randint(10, 99)
        key = f'key{str(rand_int)}'
        hashtable_obj.add_key_value(f'{key}', [f'value{num}',
                                               f'value{num}',
                                               f'value{num}'])


if __name__ == '__main__':
    ht = HashTable()
    generate_test_data(ht)

    """Block Tests HashTable()"""
    # KEY_TEST = 'KEY322'
    # ht.add_key_value(KEY_TEST, 'TESTING_DATA_VALUE')
    # print(ht)
    # print()
    # print(f'FINDED_VALUE : "{ht.find_value_by_key(KEY_TEST)}"')
    # print(f'FINDED_VALUE : "{ht.find_value_by_key("zxc")}"')
    # print(f'FINDED_VALUE : "{ht["asdasd"]}"')
    # print(f'FINDED_VALUE : "{ht[KEY_TEST]}"')
    # print(f'REMOVED_VALUE: "{ht.remove_value_by_key(KEY_TEST)}"')
    # print(f'REMOVED_VALUE: "{ht.remove_value_by_key("qwerty")}"')
