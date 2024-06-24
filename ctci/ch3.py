class StackNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:


    def __init__(self):
        self.top = None
        self.length = 0

    def __len__(self):
        return self.length

    def pop(self):
        if not self.top:
            raise Exception
        item = self.top.data
        self.top = self.top.next
        self.length -= 1
        return item

    def push(self, item):
        node = StackNode(item)
        node.next = self.top
        self.top = node
        self.length += 1

    def peek(self):
        if not self.top:
            assert len(self) == 0
            raise Exception
        return self.top.data

    def is_empty(self):
        return self.top is None


class QueueNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

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

    # def __str__(self, acc=None):
    #     if self.is_empty():
    #         return acc
    #     if acc is None:
    #         acc = '['
    #     acc += str(self.peek()) + ', '
    #     return acc


class StackMin(Stack):
    """Implementation for 3.2"""

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


class SetOfStacks:
    """Implementation for 3.3"""

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


class MyQueue:
    """Implement a queue using a pair of stacks (3.4)."""

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
            self._transfer()
        return self.spop.pop()

    def _transfer(self):
        if self.spush.is_empty():
            raise Exception
        while not self.spush.is_empty():
            self.spop.push(self.spush.pop())

    def is_empty(self):
        # A transfer may not have been done, so need to inspect both
        # stacks.
        return self.spush.is_empty() or self.spop.is_empty()


def test_stackmin():
    """Test for 3.2"""
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


def test_setofstacks():
    """Test for 3.3"""
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


def test_myqueue():
    """Test for 3.4"""
    q = Queue()
    mq = MyQueue()
    lst = [4, 3, 2, 1]
    for item in lst:
        q.add(item)
        mq.add(item)
    assert not mq.spush.is_empty()
    assert mq.spop.is_empty()
    assert mq.spush.peek() == 1
    assert q.peek() == mq.peek() == 4
    assert q.remove() == mq.remove() == 4
    q.add(5)
    q.add(6)
    mq.add(5)
    mq.add(6)
    assert not mq.spush.is_empty()
    assert not mq.spop.is_empty()
    assert mq.spush.peek() == 6
    assert mq.spop.peek() == 3
    assert q.remove() == mq.remove() == 3
    assert q.remove() == mq.remove() == 2
    assert q.remove() == mq.remove() == 1
    assert not q.is_empty()
    assert mq.spop.is_empty()
    assert not mq.spush.is_empty()
    # assert not mq.is_empty()
    q.add(7)
    q.add(8)
    mq.add(7)
    mq.add(8)
    assert q.remove() == mq.remove() == 5
    assert q.remove() == mq.remove() == 6
    assert q.remove() == mq.remove() == 7
    assert q.remove() == mq.remove() == 8


def sort_stack(stack):
    """Implementation for 3.5"""
    if stack.is_empty():
        raise Exception
    if len(stack) == 1:
        return stack
    # initialize the secondary stack for comparison
    sorted_stack = Stack()
    sorted_stack.push(stack.pop())
    while not stack.is_empty():
        current_element = stack.pop()
        while (not sorted_stack.is_empty()) and (current_element > sorted_stack.peek()):
            stack.push(sorted_stack.pop())
        sorted_stack.push(current_element)
    return sorted_stack


def test_sort_stack():
    """Test for 3.5"""
    elements = [6, 2, 12, 3, 10]
    sorted_elements = sorted(elements)
    stack = Stack()
    reference_stack = Stack()
    for a, b in zip(reversed(elements), reversed(sorted_elements)):
        stack.push(a)
        reference_stack.push(b)
    sorted_stack = sort_stack(stack)
    for i in range(len(elements)):
        assert reference_stack.pop() == sorted_elements[i]
        assert sorted_stack.pop() == sorted_elements[i]
