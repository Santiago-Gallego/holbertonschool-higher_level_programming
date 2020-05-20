#!/usr/bin/python3
"""
 Node Class
"""


class Node:
    """
     Variables and Methods of the Node Class
    """
    def __init__(self, data, next_node=None):
        """ instance variables """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data getter """
        return self.__data

    @data.setter
    def data(self, value):
        """ data setter """
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ next getter """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ next setter """
        if value is None:
            self.__next_node = value
            return
        if type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next must be a Node object")


"""
 SinglyLinkedList Class
"""


class SinglyLinkedList:
    """
     Variables and Methods of the SinglyLinkedListClass
    """
    def __init__(self):
        """ sets initializatoins """
        self.__head = None

    def sorted_insert(self, value):
        """ inserts new node into position"""
        temp = self.__head
        new_node = Node(value, self.__head)
        if temp is None:
            self.__head = new_node
            return
        if temp.data > value:
            new_node.next_node = temp
            self.__head = new_node
            return
        while temp.next_node is not None:
            if temp.next_node.data > value:
                break
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node
        return

    def __str__(self):
        """ creates a string representation """
        new_list = []
        temp = self.__head
        while temp is not None:
            new_list.append(temp.data)
            temp = temp.next_node
        string = '\n'.join(str(item) for item in new_list)
        return string
