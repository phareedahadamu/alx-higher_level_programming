#!/usr/bin/python3
class Node:

    """Defines a new node"""

    def __init__(self, data, next_node=None):
        """Instantiation"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (value is not None and isinstance(value, Node) is False):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:

    """Defines a singly linked list"""

    def __init__(self):
        """Instantiation"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts values in the linked list and sorts lowest to highest"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """configures for print()"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
