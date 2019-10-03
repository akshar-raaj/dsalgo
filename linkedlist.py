import unittest


class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class List(object):

    def __init__(self):
        self.initial = None
        self.length = 0

    def insert(self, data, position=0):
        assert position <= self.length
        if self.initial is None:
            self.initial = Node(data)
            self.length += 1
            return
        if position == 0:
            node = Node(data, self.initial)
            self.initial = node
            self.length += 1
            return
        index = 0
        node = self.initial
        while index < (position-1):
            node = node.next
            index += 1
        temp = node.next
        new = Node(data, temp)
        node.next = new
        self.length += 1

    def append(self, data):
        if self.initial is None:
            self.initial = Node(data)
            self.length += 1
            return
        node = self.initial
        while node.next is not None:
            node = node.next
        node.next = Node(data)
        self.length += 1

    def __str__(self):
        if self.initial is None:
            return ''
        node = self.initial
        while node is not None:
            print(node.data)
            node = node.next
        return ''

    def values(self):
        l = []
        node = self.initial
        while node is not None:
            l.append(node.data)
            node = node.next
        return l


class TestStringMethods(unittest.TestCase):

    def test_append(self):
        l = List()
        l.append(5)
        self.assertEqual(l.values()[0], 5)
        l.append("abc")
        self.assertEqual(l.values()[1], "abc")

    def test_insert(self):
        l = List()
        l.insert(5)
        self.assertEqual(l.values()[0], 5)
        l.insert("abc")
        self.assertEqual(l.values()[0], "abc")
        self.assertEqual(l.values()[1], 5)


if __name__ == '__main__':
    unittest.main()
