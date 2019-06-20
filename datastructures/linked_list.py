class Node:
    def __init__(self, init_data):
        self.__data = init_data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def __str__(self):
        max_len = 3

        current = self.head
        s = '['
        while current is not None and max_len > 0:
            s += f'{current.data},'
            current = current.next
            max_len -= 1

        if current is not None:
            s += '...'

        s += ']'
        return s

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        previous = None
        current = self.head
        while current is not None:
            if current.data == item:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                del current
                return
            previous = current
            current = current.next


ul = UnorderedList()
ul.add(1)
ul.add(3)
ul.add(2)
ul.remove(2)
print(ul)

