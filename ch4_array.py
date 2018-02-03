import math
import operator


class Container(object):

    def __init__(self, data=None):

        if data is not None:
            self._repr = data.copy()
        else:
            self._repr = []

    def __len__(self):
        return len(self._repr)

    def __eq__(self, other):
        return self._repr == other._repr

    def __getitem__(self, index):
        return self._repr[index]


class MinHeap(Container):

    def __init__(self, data=None):
        super().__init__(data)

    def extract(self):
        if not self._repr:
            raise Exception
        val = self._repr[0]
        if len(self) >= 2:
            self._repr[0], self._repr[-1] = self._repr[-1], self._repr[0]
            self._repr.pop()
            self._bubble_down(0)
        else:
            self._repr.pop()
        return val

    def insert(self, element):
        self._repr.append(element)
        self._bubble_up()
        return

    def _bubble_down(self, i=None):
        if i is None:
            i = 0
        if i >= len(self):
            raise IndexError
        left = 2*i + 1
        right = 2*i + 2
        smallest = i
        if left < len(self) and self._repr[left] < self._repr[smallest]:
            smallest = left
        if right < len(self) and self._repr[right] < self._repr[smallest]:
            smallest = right
        if smallest != i:
            self._repr[i], self._repr[smallest] = self._repr[smallest], self._repr[i]
            self._bubble_down(smallest)
        return

    def _bubble_up(self, i=None):
        if i is None:
            i = len(self) - 1
        if i >= len(self):
            raise IndexError
        parent = math.floor((i - 1) / 2)
        if parent >= 0:
            if self._repr[i] < self._repr[parent]:
                self._repr[i], self._repr[parent] = self._repr[parent], self._repr[i]
                self._bubble_up(parent)
        return


def test_minheap_extract():
    data_start = [2, 50, 23, 88, 90, 32, 74, 80]
    data_ref = [23, 50, 32, 88, 90, 80, 74]
    heap = MinHeap(data_start)
    val = heap.extract()
    assert val == 2
    assert heap._repr == data_ref
    heap_ref = MinHeap(data_ref)
    assert heap == heap_ref
    return True


def test_minheap_insert():
    data_start = [4, 50, 7, 55, 90, 87]
    data_ref = [2, 50, 4, 55, 90, 87, 7]
    heap = MinHeap(data_start)
    heap.insert(2)
    assert heap._repr == data_ref
    heap_ref = MinHeap(data_ref)
    assert heap == heap_ref
    return True


if __name__ == '__main__':
    test_minheap_extract()
    test_minheap_insert()
