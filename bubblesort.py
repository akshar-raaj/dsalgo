import random
"""
5 7 1 2

5 7 1 2
5 1 7 2
5 1 2 7

1 5 2 7
1 2 5 7


"""
class BubbleSort(object):

    def __init__(self, data):
        self.data = data

    def sort(self):
        length = len(self.data)
        for i in range(length - 1):
            for j in range(length - (i + 1)):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
        return self.data

def test_bubblesort():
    l = []
    for i in xrange(1000):
        l.append(random.randint(0, 100))
    m = BubbleSort(l)
    m.sort()

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test_bubblesort()", setup="from __main__ import test_bubblesort", number=100))
