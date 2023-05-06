class Node:
    """class constructor"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    """data getter"""

    @property
    def data(self):
        return self.__data

    """next_node getter"""

    @property
    def next_node(self):
        return self.__next_node

    """data setter"""

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    """next_node setter"""

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next node must be a node object")

    class SinglyLinkedList:
        """class constructor"""
