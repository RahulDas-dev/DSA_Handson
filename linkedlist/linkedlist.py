class Node:
    def __init__(self, data):
        self.data = data
        self.fnext = None

    def __str__(self):
        return f"{self.data}->NULL" if self.fnext is None else f"{self.data}->"


# Linked List Implementation.
# Stack Implementation using Linked List.


class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def push(self, data_):
        node = Node(data_)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.fnext is not None:
            temp = temp.fnext
        temp.fnext = node

    def pop(self):
        if self.head is None:
            return
        temp = self.head
        if self.head.fnext is None:
            self.head = None
            return temp
        temp = temp.fnext
        prev_node = self.head
        while temp.fnext is not None:
            prev_node = temp
            temp = temp.fnext
        prev_node.fnext = None
        return temp

    def __str__(self):
        temp = self.head
        pstr = ""
        while temp is not None:
            pstr = f"{pstr}{temp.data}->"
            temp = temp.fnext
        return f"{pstr}NULL"


if __name__ == "__main__":
    ll = LinkedList()
    ll.push(5)
    ll.push(15)
    ll.push(25)
    ll.push(35)
    ll.push(55)
    print(ll)
    i = ll.pop()
    print(ll, i)
