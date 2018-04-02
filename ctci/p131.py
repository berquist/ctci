def fib1(n):
    """Book solution from page 131."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    """Own solution using memoization."""
    cache = dict()
    cache[0] = 0
    cache[1] = 1
    def _fib(n):
        if n in cache:
            return cache[n]
        cache[n] = _fib(n - 1) + _fib(n - 2)
        return cache[n]
    return _fib(n)


def fib3(n):
    """Own solution using memoization, slighly modified to match book."""
    cache = dict()
    cache[0] = 0
    cache[1] = 1
    def _fib(n):
        if n not in cache:
            cache[n] = _fib(n - 1) + _fib(n - 2)
        return cache[n]
    return _fib(n)


def fib4(n):
    """Book solution from page 133."""
    return _fib4(n, dict())


def _fib4(n, memo):
    if n == 0 or n == 1:
        return n
    if n not in memo:
        memo[n] = _fib4(n - 1, memo) + _fib4(n - 2, memo)
    return memo[n]


def fib5(n):
    """Bottom-up approach. Book solution from page 134."""
    memo = dict()
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


def fib6(n):
    """Bottom-up approach that avoids caching entirely."""
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    return c


def fib7(n):
    """Bottom-up approach that avoids caching entirely. Book solution from
    page 134.
    """
    if n == 0:
        return n
    a, b = 0, 1
    for i in range(2, n):
        c = a + b
        a, b = b, c
    return a + b


impls = (fib1, fib2, fib3, fib4, fib5, fib6, fib7)
