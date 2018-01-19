class StackNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack(object):


    def __init__(self):
        self.top = None

    def pop(self):
        if not self.top:
            raise Exception
        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, item):
        node = StackNode(item)
        node.next = self.top
        self.top = node

    def peek(self):
        if not self.top:
            raise Exception
        return self.top.data

    def is_empty(self):
        return self.top is None


class QueueNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue(object):

    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        # to end
        node = QueueNode(item)
        if self.last:
            self.last.next = node
        self.last = node
        if not self.first:
            self.first = self.last

    def remove(self):
        # from front
        if not self.first:
            raise Exception
        data = self.first.data
        self.first = self.first.next
        if not self.first:
            self.last = None
        return data

    def peek(self):
        # from front
        if not self.first:
            raise Exception
        return self.first.data

    def is_empty(self):
        return self.first is None


class StackMin(Stack):

    def push(self, item):
        node = StackNode(item)
        if self.top:
            if item < self.top.min:
                # originally self.top.min, node.min = item, self.top.min
                node.min = item
            else:
                # originally node.min = item
                node.min = self.top.min
        else:
            node.min = item
        node.next = self.top
        self.top = node

    def min(self):
        if not self.top:
            raise Exception
        return self.top.min


class SetOfStacks(object):

    def __init__(self, thresh):
        if thresh < 1:
            raise Exception
        self.stacks = []
        self.counter = 0
        self.thresh = thresh

    def peek(self):
        if not self.stacks:
            raise Exception
        return self.stacks[-1].peek()

    def push(self, item):
        if not self.stacks:
            stack = Stack()
            self.stacks.append(stack)
        if self.counter == self.thresh:
            stack = Stack()
            stack.push(item)
            self.stacks.append(stack)
            self.counter = 1
        else:
            self.stacks[-1].push(item)
            self.counter += 1

    def pop(self):
        if not self.stacks:
            raise Exception
        item = self.stacks[-1].pop()
        if self.counter == 1:
            self.stacks.pop()
            if self.stacks:
                self.counter = self.thresh
            else:
                self.counter = 0
        else:
            self.counter -= 1
        return item

    def pop_at(self, index):
        try:
            return self.stacks[index].pop()
        except:
            raise


class MyQueue(object):
    """Implement a queue using a pair of stacks."""

    def __init__(self):
        self.spush = Stack()
        self.spop = Stack()

    def peek(self):
        if self.spop.is_empty():
            self._transfer()
        return self.spop.peek()

    def add(self, item):
        self.spush.push(item)

    def remove(self):
        if self.spop.is_empty():
            self.transfer()
        return self.spop.pop()

    def transfer(self):
        if self.spush.is_empty():
            raise Exception
        while not self.spush.is_empty():
            self.spop.push(self.spush.pop())

    def is_empty(self):
        # A transfer may not have been done, so need to inspect both
        # stacks.
        return self.spush.is_empty() or self.spop.is_empty()


def test_stackmin():
    stack = StackMin()
    # from bottom to top
    pairs = [
        (10, 10),
        (6, 6),
        (3, 3),
        (2, 2),
        (9, 2),
        (4, 2),
        (5, 2),
    ]
    for item, _ in pairs:
        stack.push(item)
    for expected_item, expected_min in reversed(pairs):
        assert stack.min() == expected_min
        assert stack.pop() == expected_item
    return True


def test_setofstacks():
    # from itertools import cycle
    thresh = 3
    threshl = list(range(1, 1 + thresh))
    # cycler = cycle(threshl)
    items = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    nstacks = (len(items) // thresh) + int((len(items) % thresh) > 0)
    pairs = [
        (10, 1),
        (9, 3),
        (8, 2),
        (7, 1),
        (6, 3),
        (5, 2),
        (4, 1),
        (3, 3),
        (2, 2),
        (1, 1),
    ]
    nstacks = 4
    setofstacks = SetOfStacks(thresh)
    for item in reversed(items):
        setofstacks.push(item)
    # for item, counter in zip(items, cycler):
    for item, counter in pairs:
        assert setofstacks.counter == counter
        assert setofstacks.pop() == item
        newcounter = counter - 1
        if not newcounter:
            newcounter = thresh
        if not setofstacks.stacks:
            newcounter = 0
        assert setofstacks.counter == newcounter
    return True


def test_myqueue():
    q = Queue()
    mq = MyQueue()
    l = [4, 3, 2, 1]
    for item in l:
        q.add(item)
        mq.add(item)
    assert q.peek() == l[0]
    assert mq.peek() == l[0]
    return True


if __name__ == '__main__':
    test_stackmin()
    test_setofstacks()
    test_myqueue()
