class StackNode(object):

    self.data = None
    self.next = None

    def __init__(self, data):
        self.data = data


class Stack(object):

    self.top = None

    def __init__(self):
        pass

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

    self.data = None
    self.next = None

    def __init__(self, data):
        self.data = data


class Queue(object):

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
                self.top.min, node.min = item, self.top.min
            else:
                node.min = item
        else:
            node.min = item
        node.next = self.top
        self.top = node

    def min(self):
        if not self.top:
            raise Exception
        return self.top.min


class SetOfStacks(object):

    self.stacks = []
    self.counter = 0

    def __init__(self, thresh):
        if thresh < 1:
            raise Exception
        self.thresh = thresh

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
