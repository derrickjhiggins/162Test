
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self._head = None

    def get_head(self):
        return self._head

    def rec_contains(self, nod, val):
        if nod is None:
            return False
        if nod.data == value:
            return True
        return self.rec_contains(node.next, val)

    def contains(self, val):
        return self.rec_contains(self._head, val)

    def rec_reverse(self, previous_node, current_node):

        if current_node is None:
            self._head = previous_node
            return
        next_node = current_node.next
        curr_node.next = previous_node
        self.rec_reverse(current_node, next_node)

    def reverse(self):

        self.rec_reverse(None, self._head)

    def rec_to_plain_list(self, nod):
        if plain_list is None:
            plain_list = []

        if nod is None:
            return plain_list
        plain_list.append(nod.data)
        return self.rec_to_plain_list(nod.next, plain_list)


    def to_plain_list(self):
        return self.rec_to_plain_list(self._head)


    def rec_add(self, nod, val):
        if nod is None:
            return Node(val)
        nod.next = self.rec_add(nod.next, val)
        return nod


    def add(self, val):
        self._head = self.rec_add(self._head, val)


    def rec_remove(self, previous_node, current_node, val):
        if current_node is None:
            return None
        if current_node.data == value:
            if previous_node is None:
             return current_node.next
        previous_node.next = current_node.next
        return self._head
        return self.rec_remove(current_node, current_node.next, val)


    def remove(self, val):
        self._head = self.rec_remove(None, self._head, val)


    def rec_insert(self, previouus_node, current_node, val, index):
        if index == 0:
            new_node = Node(val)
            if previous_node:
                previous_node.next = new_node
            else:
                self._head = new_node
            new_node.next = current_node
            return
        if current_node is None:
            raise IndexError
        self.rec_insert(current_node, current_node.next, value, index - 1)


    def insert(self, value, index):
        self.rec_insert(None, self._head, value, index)
