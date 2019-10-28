"""
8165012

8165  012

81 65 01 2

8 1 6 5 0 1 2

18 56 01 2

1568 012

0112568
"""
import random

class MergeSort(object):
    
    def __init__(self, data):
        self.data = data

    def sort(self):
        return self.split(self.data)

    def split(self, data):
        """
        [7, 1, 5, 4, 0]
        """
        length = len(data)
        if length <= 1:
            return data
        half = length/2
        left = data[0:half]
        right = data[half:]
        left_split = self.split(left)
        right_split = self.split(right)
        merged = self.merge(left_split, right_split)
        return merged

    @classmethod
    def merge(self, left, right):
        """
        [2] [1]

        [1, 4] [2, 3]

        [1, 3, 4] [2, 5]
        """
        left_index = 0
        right_index = 0
        left_length = len(left)
        right_length = len(right)
        merged = []
        while (left_index < left_length) and (right_index < right_length):
            left_value = left[left_index]
            right_value = right[right_index]
            if left_value <= right_value:
                merged.append(left_value)
                left_index += 1
            elif left_value > right_value:
                merged.append(right_value)
                right_index += 1
        if left_index < left_length:
            merged.extend(left[left_index:])
        if right_index < right_length:
            merged.extend(right[right_index:])
        return merged

def test_mergesort():
    l = []
    for i in xrange(1000):
        l.append(random.randint(0, 100))
    m = MergeSort(l)
    m.sort()

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test_mergesort()", setup="from __main__ import test_mergesort", number=100))
