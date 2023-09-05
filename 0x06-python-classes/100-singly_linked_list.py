#!/usr/bin/python3
""" Create a singly list """


class Node:
    """ to define node of singly list """
    def __init__(self, data, next_node=None):
        """ to initialize instance """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ to retrieve data """
        return self.__data

    @data.setter
    def data(self, value):
        """ to set data to value """
        if type(value) is not integer:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ to retrieve node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ to set node to value """
        if not isinstance(value, Node) or value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ to define  singly linked list """
    def __init__(self):
        """ Inistialize a nez linkedList """
        self.__head = None

    def sorted_insert(self, value):
        """ inserts a new Node to the SinglyLinkedList

        the node inserted into the list at position
        ordered

        Args:
            value (Node): the new node to insert
        """

    new = Node(value)
    if self.__head is None:
        new.next_node = None
        self.__head = new
    elif self.__head.data > value:
        new.next_node = self.__head
        self.__head = new
    else:
        tmp = self.__head
        while (tmp.next_node is not None and tmp.next_node_data < value):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new

    def __str__(self):
        """ Define the print() representation of SinglyLinkedList """
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('/n'.join(values))
