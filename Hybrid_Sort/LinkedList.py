from random import randint, shuffle, seed, choice
class Node:
    __slots__ = 'value', 'next_node'

    def __init__(self, value, next_node=None):
        """
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node

    def __eq__(self, other):
        """
        Determine if two nodes are equal (same value)
        :param other: node to compare to
        :return: True if nodes are equal, False otherwise
        """
        if other is None:
            return False
        if self.value == other.value:
            return True
        return False

    def __repr__(self):
        """
        String representation of a node
        :return: string of value
        """
        return str(self.value)


def _insertion_wrapper(insertion_sort):
    """
    :return:
    """

    def insertion_counter(self, *args, **kwargs):
        if self.size > 1:
            LinkedList._c += 1
        insertion_sort(self)
    return insertion_counter


class LinkedList:
    _c = 0

    def __init__(self, data=None):
        """
        Create/initialize an empty linked list
        """
        self.head = None  # Node
        self.tail = None  # Node
        self.size = 0  # Integer

        if data:
            [self.push_back(i) for i in data]

    def __len__(self):
        return self.length()

    def __eq__(self, other):
        """
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """
        if self.size != other.size:
            return False
        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next_node
                temp_other = temp_other.next_node
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True
        return False

    def __repr__(self):
        """
        String representation of a linked list
        :return: string of list of values
        """
        temp_node = self.head
        values = []
        if temp_node is None:
            return str([])
        while temp_node is not None:
            values.append(temp_node.value)
            temp_node = temp_node.next_node
        return str(values)

    # ------------------------Accessor Functions---------------------------

    def length(self):
        """
        Gets the number of nodes of the linked list
        :return: size of list
        """
        return self.size

    def is_empty(self):
        """
        Determines if the linked list is empty
        :return: True if list is empty and False if not empty
        """
        return self.size == 0

    def front_value(self):
        """
        Gets the first value of the list
        :return: value of the list head
        """
        if self.is_empty():
            return None
        return self.head.value

    def push_front(self, val):
        """
        Adds a node to the front of the list with value 'val'
        :param val: value to add to list
        :return: no return
        """
        new_node = Node(val, self.head)
        if self.is_empty():
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def push_back(self, val):
        """
        Adds a node to the back of the list with value 'val'
        :param val: value to add to list
        :return: no return
        """
        new_node = Node(val)
        # Update current head and tail, if necessary
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next_node = new_node
        # new_node is now the tail
        self.tail = new_node
        self.size += 1

    def pop_front(self):
        """
        Removes a node from the front of the list
        :return: the value of the removed node
        """
        if self.is_empty():
            return None
        val = self.head.value
        # Update head and size
        self.head = self.head.next_node
        self.size -= 1
        # If the only node was removed, also need to update tail
        if self.is_empty():
            self.tail = None
        return val

    @_insertion_wrapper
    def insertion_sort(self):
        """
        Sorts the singly linked list using a placeholder list.
        :return: nothing
        """
        leng = self.length()
        if self.is_empty():
            return None
        new = LinkedList()
        new.push_back(self.front_value())
        real_head = self.head.next_node
        count = 0
        while count < leng - 1:
            if real_head.value >= new.tail.value:
                new.push_back(real_head.value)

            elif real_head.value <= new.head.value:
                new.push_front(real_head.value)

            else:
                new_head = new.head
                while new_head.next_node is not None:
                    if real_head.value <= new_head.next_node.value and real_head.value > new_head.value:
                        temp = Node(real_head.value, new_head.next_node)
                        new_head.next_node = temp
                        new.size += 1
                        new_head = new_head.next_node
                        break
                    else:
                        new_head = new_head.next_node
                        continue
            real_head = real_head.next_node
            count += 1
        self.head = new.head
        self.tail = new.tail
        self.size = new.size
