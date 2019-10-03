"""
8165012

8165  012

81 65 01 2

8 1 6 5 0 1 2

18 56 01 2

1568 012

0112568
"""

class MergeSort(object):
    
    def __init__(self, data):
        self.data = data

    def split(self, data):
        """
        [7, 1, 5, 4, 0]
        """
        print("Splitting %s" % data)
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
            if left_value < right_value:
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
