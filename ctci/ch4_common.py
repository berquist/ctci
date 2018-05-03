"""ch4_common.py: common daa structures needed for binary (search)
trees, heaps, and graphs.

"""

import math


class Container(object):

    def __init__(self, data=None):

        if data is not None:
            self._repr = data.copy()
        else:
            self._repr = []

    def __str__(self):
        return str(self._repr)

    def __len__(self):
        # if hasattr(self, '_len'):
        #     return self._len
        # else:
        #     # return len(self._repr) - self._repr.count(None)
        #     return len(self._repr)
        return len(self._repr)

    def count(self):
        return len(self) - self._repr.count(None)

    def __eq__(self, other):
        return self._repr == other._repr

    def __getitem__(self, index):
        return self._repr[index]

    def _index_parent(self, i):
        return math.floor((i - 1) / 2)
