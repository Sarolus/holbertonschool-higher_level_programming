#!/usr/bin/python3

"""
Singly_linked_list

Manages a singly linked list and it's node.

"""


class Node():
    """
    Node class

    This class defines a node of a singly linked list

    Attributes:
        __data (int): Data of a node
        __next_node (int): Next node of a singly linked list
    """
    __data = 0
    __next_node = None

    def __init__(self, prmData, next_node=None):
        """
        constructor method

        Args:
            prmData (int): data of a node
            next_node (int): Next node of a singly linked list
        """
        self.data = prmData
        self.next_node = next_node

    @property
    def data(self):
        """
        size getter method

        Returns the data of a node
        """
        return self.__data

    @data.setter
    def data(self, prmValue):
        """
        size setter method

        Args:
            prmValue (int): Given value for a data node
        """
        self.__data = prmValue
        if not isinstance(prmValue, int):
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """
        next_node getter method

        Returns the next the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, prmValue):
        """
        next_node setter method

        Args:
            prmValue (int): Given value for a next node of
            a singly linked list
        """
        self.__next_node = prmValue
        if not isinstance(prmValue, Node) and prmValue is not None:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """
    SinglyLinkedList class

    This class defines a singly linked list

    Attributes:
        __head: Head of our singly linked list
    """
    head = None
    __next_node = None

    def __init__(self):
        """
        constructor method
        """
        self.head = None
        self.next_node = None

    def sorted_insert(self, prmValue):
        """
        Insert a new node into a singly linked lists

        Args:
            prmValue (int): Given value of a new node.
        """
        new = Node(prmValue)
        Head = self.head
        if Head is None or Head.data >= prmValue:
            if Head:
                new.next_node = Head
            self.head = new
        else:
            while Head.next_node is not None and \
                    Head.next_node.data < prmValue:
                Head = Head.next_node
            new.next_node = Head.next_node
            Head.next_node = new

    def __str__(self):
        """
        Convert to string in order to be print

        Returns a string containing all the singly linked list.
        """
        node = self.head
        while node and node.next_node is not None:
            print(node.data)
            node = node.next_node
        return str(node.data)
