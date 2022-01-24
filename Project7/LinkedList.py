# Name: Frank Shang
# Date: 07/26/2021
# Project 7
# Description: This program contains a LinkedList class that has recursive implementations of
# add, remove, contains, insert, reverse, and to_plain_list methods

class Node:
    '''
    Represents a node in a linked list
    '''

    def __init__(self, data):
        '''
        initializes node with private data members
        '''
        self._data = data
        self._next = None

    def get_data(self):
        '''
        get method that returns the object's (Node) data
        '''
        return self._data

    def get_next(self):
        '''
        get method that returns the object's (Node) next
        '''
        return self._next

    def set_data(self, data):
        '''
        set method that sets the object's (Node) data
        '''
        self._data = data

    def set_next(self, next):
        '''
        set method that sets the object's (Node) next
        '''
        self._next = next


class LinkedList:
    '''
    Represents a linked list object
    '''

    def __init__(self):
        '''
        init method that sets the head to None
        '''
        self._head = None

    def get_head(self):
        '''
        returns the head of the linked list
        '''
        return self._head

    def set_head(self, head):
        '''
        sets the head of the linked list
        '''
        self._head = head

    def add(self, val):
        '''
        recursive helper method for the recursive add method
        '''
        self.rec_add(val, self.get_head())

    def rec_add(self, val, current):
        '''
        recursive method that adds the node to the end of the linked list
        stops calling itself when the current node's next value is None
        '''
        if self.get_head() is None:
            self._head = Node(val)
            return
        if current.get_next() is None:
            current.set_next(Node(val))
            return
        self.rec_add(val, current.get_next())

    def remove(self, val):
        '''
        helper method for the recursive remove method
        returns if the linked list is empty
        '''
        if self.get_head() is None:
            return
        else:
            self.rec_remove(val, self.get_head(), self.get_head())

    def rec_remove(self, val, current, previous):
        '''
        recursive method for removing a node from the linked list
        '''
        if current.get_next() is None:
            # tests for the last node
            if current.get_data() == val:
                previous.set_next(current.get_next())
                return
            else:
                return
        if current.get_next() is not None:
            # tests for the all preceding nodes before the last node
            if current.get_data() == val and current != self.get_head():
                # if the current node is not the head node
                previous.set_next(current.get_next())
                # removes the current node, sets the previous node's next value to the node that is after current
                return
            if current.get_data() == val and current == self.get_head():
                # tests whether the removed node is the head node
                self.set_head(current.get_next())
                # sets the head node to the next node
                return
        self.rec_remove(val, current.get_next(), current)

    def contains(self, key):
        '''
        helper method for the recursive contains method
        '''
        return self.rec_contains(key, self.get_head())

    def rec_contains(self, key, current):
        '''
        recursive method for the contains method
        determines whether the key value is in the linked list
        returns True if in linked list
        returns False if not in linked list
        '''
        if self.get_head() is None:
            # if the linked list is empty, return False
            return False
        if current.get_next() is None:
            if current.get_data() != key:
                # tests to see if the last node's data is equal to the key, if not, return false
                return False
            return True
        if current.get_data() == key:
            return True
        return self.rec_contains(key, current.get_next())

    def insert(self, val, pos):
        '''
        helper method for the recursive insert method
        '''
        self.rec_insert(val, pos, self.get_head())

    def rec_insert(self, val, pos, current, counter=1):
        '''
        recursive method for the insert method
        '''
        if self.get_head() is None:
            # if the linked list is empty, then add the value to the list
            self.add(val)
            return
        if current.get_next() is None:
            # if on the last node, make the last node point to the new node object
            current.set_next(Node(val))
            return
        if pos == 0:
            # if inserting at the beginning, make it the header node
            self.set_head(Node(val))
            self.get_head().set_next(current)
            return
        if pos == counter:
            # if position is equal to the counter, then insert node in between
            temp = current.get_next()
            current.set_next(Node(val))
            next = current.get_next()
            next.set_next(temp)
            return
        self.rec_insert(val, pos, current.get_next(), counter + 1)

    def reverse(self):
        '''
        helper method that calls rec_reverse
        '''

        following = self.get_head().get_next()
        self.rec_reverse(self.get_head(), following)

    def rec_reverse(self, current, following, previous=None):
        '''
        recursive method that reverses the linked list. stops calling itself when current is on the last node
        '''
        if current.get_next() is None:
            self.set_head(current)
            current.set_next(previous)
            return
        following = current.get_next()
        current.set_next(previous)
        previous = current
        current = following
        self.rec_reverse(current, following, previous)

    def to_plain_list(self):
        '''
        helper method that calls the rec_to_plain_list to print out the linked list in a regular list
        '''
        return self.rec_to_plain_list(self.get_head())

    def rec_to_plain_list(self, current, result = None):
        '''
        recursive method that prints out the linked list in a regular list
        '''
        if result is None:
            result = []
        if current is None:
            return result
        result.append(current.get_data())
        return self.rec_to_plain_list(current.get_next(), result)

#my_list = LinkedList()
#my_list.add(5)
#my_list.add(7)
#my_list.add(8)
#my_list.add(10)
#my_list.add(45)
#my_list.remove(8)
#my_list.insert(6, 2)
#print(my_list.to_plain_list())
#my_list.reverse()
#print(my_list.to_plain_list())
