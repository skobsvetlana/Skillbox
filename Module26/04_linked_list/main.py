from typing import Any, Optional

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0


    def __str__(self):
        string = "["
        node = self.head
        while node.next:
            string += str(node.value) + ', '
            node = node.next
        string += str(node.value) + ']'

        return string


    def __iter__(self):
        return self


    def __next__(self):
        if not self.head:
            raise StopIteration
        item = self.head.value
        self.head = self.head.next
        return item


    def find_tail(self, head: Node) -> Node:
        tail = head
        if tail.next:
            tail = self.find_tail(head=tail.next)

        return tail


    def append(self, node: Any) -> None:
        if not isinstance(node, Node):
            node = Node(node)

        if self.head:
            self.find_tail(head=self.head).next = node
        else:
            self.head = node

        self.length += 1


    def get(self, ind: int) -> Optional:
        curr = self.head
        try:
            for _ in range(ind):
                curr = curr.next
        except AttributeError:
            return f'Элемента с таким индексом {ind} не существует'

        return curr


    def remove(self, ind: int) -> None:
        curr = self.head
        try:
            for _ in range(ind - 1):
                curr = curr.next

            curr.next = curr.next.next
        except AttributeError:
            print(f'Элемента с таким индексом {ind} не существует')

        self.length -= 1


my_linked_list = LinkedList()
my_linked_list.append(10)
my_linked_list.append(20)
my_linked_list.append(30)

print('Текущий список:', my_linked_list)
print('Получение третьего элемента:', my_linked_list.get(2))
print('Удаление второго элемента.')
my_linked_list.remove(1)
print('Новый список:', my_linked_list)

my_linked_list.append(40)
my_linked_list.append(50)
print('Текущий список:', my_linked_list)

for i in my_linked_list:
    print(i)