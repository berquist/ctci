def bubble_sort(l):
    """Runtime: O(N^2) average and worst case. Memory: O(1).

    We start at the beginning of the array and swap the first two
    elements if the first is greater than the second. Them, we go to
    the next pair, and so on, continuously making sweeps of the array
    until it is sorted. In doing so, the smaller items slowly "bubble"
    up to the beginning of the list.
    """
    ln = len(l)
    if ln == 1:
        return
    is_sorted = False
    while not is_sorted:
        # bubble pass
        for i in range(1, ln):
            if l[i - 1] > l[i]:
                l[i - 1], l[i] = l[i], l[i - 1]
        # check pass
        pass_is_sorted = True
        for i in range(1, ln):
            if l[i - 1] > l[i]:
                pass_is_sorted = False
                break
        if pass_is_sorted:
            is_sorted = True
    return


def test_bubble_sort():
    l1 = [9, 8, 7, 6, 5, -1, -2]
    l1_ref = [-2, -1, 5, 6, 7, 8, 9]
    bubble_sort(l1)
    assert l1 == l1_ref
    l2 = [2, 3, 4, 10, 20, 90]
    l2_ref = l2.copy()
    bubble_sort(l2)
    assert l2 == l2_ref
    l3 = [1, 4, 5, 2, 8, 9]
    l3_ref = [1, 2, 4, 5, 8, 9]
    bubble_sort(l3)
    assert l3 == l3_ref
    return True


def selection_sort(l):
    """Runtime: O(N^2) average and worst case. Memory: O(1).

    Selection sort is the child's algorithm: simple, but
    inefficient. Find the smallest element using a linear scan and
    move it to the fron (swapping it with the front element). Then,
    find the second smallest and move it, again doing a linear
    scan. Continue doing this until all the elements are in place.
    """
    ln = len(l)
    if ln == 1:
        return
    for i in range(ln):
        # find the smallest element
        _min = l[i]
        k = i
        for j in range(k, ln):
            if l[j] < _min:
                k = j
        # swap
        if k > i:
            l[i], l[k] = l[k], l[i]
    return


def test_selection_sort():
    l1 = [9, 8, 7, 6, 5, -1, -2]
    l1_ref = [-2, -1, 5, 6, 7, 8, 9]
    selection_sort(l1)
    assert l1 == l1_ref
    l2 = [2, 3, 4, 10, 20, 90]
    l2_ref = l2.copy()
    selection_sort(l2)
    assert l2 == l2_ref
    l3 = [1, 4, 5, 2, 8, 9]
    l3_ref = [1, 2, 4, 5, 8, 9]
    selection_sort(l3)
    assert l3 == l3_ref
    return True


def insertion_new_sort(l):
    if len(l) == 1:
        return ln
    nl = []
    while len(l) > 0:
        element = l.pop()
        lnl = len(nl)
        for i, sorted_element in enumerate(nl):
            if element < sorted_element:
                nl.insert(i, element)
                break
        if lnl == len(nl):
            nl.append(element)
    return nl


def test_insertion_new_sort():
    l1 = [9, 8, 7, 6, 5, -1, -2]
    l1_ref = [-2, -1, 5, 6, 7, 8, 9]
    nl1 = insertion_new_sort(l1)
    assert nl1 == l1_ref
    l2 = [2, 3, 4, 10, 20, 90]
    l2_ref = l2.copy()
    nl2 = insertion_new_sort(l2)
    assert nl2 == l2_ref
    return True


def insertion_sort(l):
    ln = len(l)
    if ln == 1:
        return
    for i in range(1, ln):
        element = l[i]
        for j in range(i):
            sorted_element = l[j]
            if element < sorted_element:
                l.insert(j, l.pop(i))
                break
    return


def test_insertion_sort():
    l1 = [9, 8, 7, 6, 5, -1, -2]
    l1_ref = [-2, -1, 5, 6, 7, 8, 9]
    insertion_sort(l1)
    assert l1 == l1_ref
    l2 = [2, 3, 4, 10, 20, 90]
    l2_ref = l2.copy()
    insertion_sort(l2)
    assert l2 == l2_ref
    l3 = [1, 4, 5, 2, 8, 9]
    l3_ref = [1, 2, 4, 5, 8, 9]
    insertion_sort(l3)
    assert l3 == l3_ref
    return True


def insert(l, element, index):
    _len = len(l)
    assert index <= _len
    if index == _len:
        l.append(element)
    else:
        # strategy: grow the list by appending its own last element,
        # shuffle everything up from index to the end (by iterating
        # backwards), then assign at the index
        l.append(l[-1])
        for i in range(_len, index, -1):
            l[i] = l[i - 1]
        l[index] = element
    return


def test_insert():
    l1 = []
    l1r = [4]
    insert(l1, 4, 0)
    assert l1 == l1r
    l2 = [4]
    l2r = [4, 5]
    insert(l2, 5, 1)
    assert l2 == l2r
    l3 = [4]
    l3r = [5, 4]
    insert(l3, 5, 0)
    assert l3 == l3r
    l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l4r = [1, 2, 3, 4, 5, 6, 7, 20, 8, 9]
    insert(l4, 20, 7)
    assert l4 == l4r
    return


def insertion2_sort(l):
    ln = len(l)
    if ln == 1:
        return
    for i in range(1, ln):
        for j in range(i):
            if l[i] < l[j]:
                insert(l, l.pop(i), j)
                break
    return


def test_insertion2_sort():
    l1 = [9, 8, 7, 6, 5, -1, -2]
    l1_ref = [-2, -1, 5, 6, 7, 8, 9]
    insertion2_sort(l1)
    assert l1 == l1_ref
    l2 = [2, 3, 4, 10, 20, 90]
    l2_ref = l2.copy()
    insertion2_sort(l2)
    assert l2 == l2_ref
    l3 = [1, 4, 5, 2, 8, 9]
    l3_ref = [1, 2, 4, 5, 8, 9]
    insertion2_sort(l3)
    assert l3 == l3_ref
    return True


def insertion3_sort(l):
    """The first piece of pseudocode from Wikipedia"""
    if len(l) == 1:
        return
    i = 1
    while i < len(l):
        j = i
        while j > 0 and l[j - 1] > l[j]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j = j - 1
        i = i + 1
    return


def test_insertion3_sort():
    l1 = [9, 8, 7, 6, 5, -1, -2]
    l1_ref = [-2, -1, 5, 6, 7, 8, 9]
    insertion3_sort(l1)
    assert l1 == l1_ref
    l2 = [2, 3, 4, 10, 20, 90]
    l2_ref = l2.copy()
    insertion3_sort(l2)
    assert l2 == l2_ref
    l3 = [1, 4, 5, 2, 8, 9]
    l3_ref = [1, 2, 4, 5, 8, 9]
    insertion3_sort(l3)
    assert l3 == l3_ref
    return True


def insertion4_sort(l):
    """The second piece of pseudocode from Wikipedia"""
    if len(l) == 1:
        return
    i = 1
    while i < len(l):
        x = l[i]
        j = i - 1
        while j >= 0 and l[j] > x:
            l[j + 1] = l[j]
            j = j - 1
        l[j + 1] = x
        i = i + 1
    return


def test_insertion4_sort():
    l1 = [9, 8, 7, 6, 5, -1, -2]
    l1_ref = [-2, -1, 5, 6, 7, 8, 9]
    insertion4_sort(l1)
    assert l1 == l1_ref
    l2 = [2, 3, 4, 10, 20, 90]
    l2_ref = l2.copy()
    insertion4_sort(l2)
    assert l2 == l2_ref
    l3 = [1, 4, 5, 2, 8, 9]
    l3_ref = [1, 2, 4, 5, 8, 9]
    insertion4_sort(l3)
    assert l3 == l3_ref
    return True


def sorted_matrix_search(mat, element):
    """return the matrix tuple (i, j) of the element's location in the
    matrix; if not found, return None (10.9)
    """
    # scan along the shortest dimension which presumably has the
    # longest stride -> future optimization
    assert len(mat) > 0
    assert len(mat[0]) > 0
    m, n = len(mat), len(mat[0])
    if mat[0][0] > element:
        return None
    if mat[m - 1][n - 1] < element:
        return None
    # this is really searching for the midpoint
    for i in range(m):
        if mat[i][0] == element:
            return (i, 0)
        elif mat[i][0] > element:
            i = i - 1
            break
    # this should be binary search
    for j in range(n):
        if mat[i][j] == element:
            return (i, j)
        elif mat[i][j] > element:
            break
    return None


def sorted_matrix_proper_search(mat, element):
    """return the matrix tuple (i, j) of the element's location in the
    matrix; if not found, return None (10.9)
    """
    # scan along the shortest dimension which presumably has the
    # longest stride -> future optimization
    assert len(mat) > 0
    assert len(mat[0]) > 0
    m, n = len(mat), len(mat[0])
    if mat[0][0] > element:
        return None
    if mat[m - 1][n - 1] < element:
        return None
    # this is really searching for the midpoint
    for i in range(m):
        if mat[i][0] == element:
            return (i, 0)
        elif mat[i][0] > element:
            i = i - 1
            break
    j = binary_search(mat[i], element)
    if j is None:
        return None
    return (i, j)


def test_sorted_matrix_search():
    """Test for 10.9"""
    mat1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    # mat1t = [[1, 4, 7],
    #          [2, 5, 8],
    #          [3, 6, 9]]
    assert sorted_matrix_search(mat1, 0) == None
    assert sorted_matrix_search(mat1, 1) == (0, 0)
    assert sorted_matrix_search(mat1, 2) == (0, 1)
    assert sorted_matrix_search(mat1, 3) == (0, 2)
    assert sorted_matrix_search(mat1, 4) == (1, 0)
    assert sorted_matrix_search(mat1, 5) == (1, 1)
    assert sorted_matrix_search(mat1, 6) == (1, 2)
    assert sorted_matrix_search(mat1, 7) == (2, 0)
    assert sorted_matrix_search(mat1, 8) == (2, 1)
    assert sorted_matrix_search(mat1, 9) == (2, 2)
    assert sorted_matrix_search(mat1, 10) == None
    return True


def test_sorted_matrix_proper_search():
    """Test for 10.9"""
    mat1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    # mat1t = [[1, 4, 7],
    #          [2, 5, 8],
    #          [3, 6, 9]]
    assert sorted_matrix_proper_search(mat1, 0) == None
    assert sorted_matrix_proper_search(mat1, 1) == (0, 0)
    assert sorted_matrix_proper_search(mat1, 2) == (0, 1)
    assert sorted_matrix_proper_search(mat1, 3) == (0, 2)
    assert sorted_matrix_proper_search(mat1, 4) == (1, 0)
    assert sorted_matrix_proper_search(mat1, 5) == (1, 1)
    assert sorted_matrix_proper_search(mat1, 6) == (1, 2)
    assert sorted_matrix_proper_search(mat1, 7) == (2, 0)
    assert sorted_matrix_proper_search(mat1, 8) == (2, 1)
    assert sorted_matrix_proper_search(mat1, 9) == (2, 2)
    assert sorted_matrix_proper_search(mat1, 10) == None
    return True

def quick_sort(l, left, right):
    """Runtime: O(N*log(N)) average, O(N^2) worst case. Memory: O(log(N)).

    In quick sort, we pick a random element and partition the array,
    such that all numbers that are less than the partitioning element
    come before all elements that are greater than it. The
    partitioning can be performed efficiently through a series of
    swaps.

    If we repeatedly partition the array (and its sub-arrays) around
    an element, the array will eventually become sorted. However, as
    the partitioned element is not guaranteed to be the median (or
    anywhere near the median), our sorting could be very slow. This is
    the reason for the O(N^2) worst case runtime.
    """
    index = partition(l, left, right)
    # sort left half
    if left < (index - 1):
        quick_sort(l, left, index - 1)
    # sort right half
    if index < right:
        quick_sort(l, index, right)
    return


def partition(l, left, right):
    pivot = l[(left + right) // 2]
    while left <= right:
        # find element on the left that should be on the right
        while l[left] < pivot:
            left += 1
        # find element on the right that should be on the left
        while l[right] > pivot:
            right -= 1
        # swap elements and move left/right indices
        if left <= right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
    return left


def test_quick_sort():
    l1 = [9, 8, 7, 6, 5, -1, -2]
    l1_ref = [-2, -1, 5, 6, 7, 8, 9]
    quick_sort(l1, 0, len(l1) - 1)
    assert l1 == l1_ref
    l2 = [2, 3, 4, 10, 20, 90]
    l2_ref = l2.copy()
    quick_sort(l2, 0, len(l2) - 1)
    assert l2 == l2_ref
    l3 = [1, 4, 5, 2, 8, 9]
    l3_ref = [1, 2, 4, 5, 8, 9]
    quick_sort(l3, 0, len(l3) - 1)
    assert l3 == l3_ref
    return True


def merge_sort(l):
    """Runtime: O(N*log(N)) average and worst case. Memory: Depends.

    Merge sort divides the array in half, sorts each of those halves,
    and then merges them back together. Each of those halves has the
    same sorting algorithm applied to it. Eventually, you are merging
    just two single-element array. It is the "merge" part that does
    all the heavy lifting.

    The merge method operates by copying all the elements from the
    target array segment into a helper array, keeping track of where
    the start of the left and right halves should be (`helper_left`
    and `helper_right`). We then iterate through `helper`, copying the
    smaller element from each half into the array. At the end, we copy
    any remaining elements into the target array.
    """
    helper = ['' for _ in range(len(l))]
    _merge_sort(l, helper, 0, len(l) - 1)
    return


def _merge_sort(l, helper, low, high):
    if low < high:
        middle = (low + high) // 2
        _merge_sort(l, helper, low, middle)
        _merge_sort(l, helper, middle + 1, high)
        merge(l, helper, low, middle, high)
    return


def merge(l, helper, low, middle, high):
    # copy both halves into a helper array
    for i in range(low, high + 1):
        helper[i] = l[i]

    helper_left = low
    helper_right = middle + 1
    current = low

    # Interate through helper array. Compare the left and right half,
    # copying back the smaller element from the two halves into the
    # original array.
    while (helper_left <= middle) and (helper_right <= high):
        if helper[helper_left] <= helper[helper_right]:
            l[current] = helper[helper_left]
            helper_left += 1
        else:
            l[current] = helper[helper_right]
            helper_right += 1
        current += 1

    # Copy the rest of the left side of the array into the target
    # array
    remaining = middle - helper_left
    for i in range(remaining + 1):
        l[current + i] = helper[helper_left + i]
    return


def test_merge_sort():
    l1 = [9, 8, 7, 6, 5, -1, -2]
    l1_ref = [-2, -1, 5, 6, 7, 8, 9]
    merge_sort(l1)
    assert l1 == l1_ref
    l2 = [2, 3, 4, 10, 20, 90]
    l2_ref = l2.copy()
    merge_sort(l2)
    assert l2 == l2_ref
    l3 = [1, 4, 5, 2, 8, 9]
    l3_ref = [1, 2, 4, 5, 8, 9]
    merge_sort(l3)
    assert l3 == l3_ref
    return True


def binary_search(l, x, low=None, high=None):
    """Perform binary search on a sorted list iteratively."""
    ln = len(l)
    if ln == 0:
        return None
    if low is None:
        low = 0
    if high is None:
        high = ln - 1
    if low > high:
        return None

    while low <= high:
        mid = (low + high) // 2
        if l[mid] < x:
            low = mid + 1
        elif l[mid] > x:
            high = mid - 1
        else:
            return mid
    return None


def binary_search_recursive(l, x, low=None, high=None):
    """Perform binary search on a sorted list recursively."""
    ln = len(l)
    if ln == 0:
        return None
    if low is None:
        low = 0
    if high is None:
        high = ln - 1
    if low > high:
        return None

    mid = (low + high) // 2

    if l[mid] < x:
        return binary_search_recursive(l, x, mid + 1, high)
    if l[mid] > x:
        return binary_search_recursive(l, x, low, mid - 1)
    # Both failed comparisons: must be equal.
    return mid


def binary_search_closest(l, x, low=None, high=None):
    """Use iterative binary search to find the (value, index) that is
    closest to the desired value.

    If the desired value exists, this is normal binary search.
    """
    ln = len(l)
    if ln == 0:
        return (None, None)
    if low is None:
        low = 0
    if high is None:
        high = ln - 1
    if low > high:
        return (None, None)

    while low <= high:
        mid = (low + high) // 2
        if l[mid] < x:
            low = mid + 1
        elif l[mid] > x:
            high = mid - 1
        else:
            return (l[mid], mid)

    return (l[mid], mid)


def test_binary_search():
    le = []
    l0 = [0]
    l1_ref = [-2, -1, 5, 6, 7, 8, 9]
    tests = [
        (le, 5, None),
        (l0, 0, 0),
        (l1_ref, -2, 0),
        (l1_ref, 9, 6),
        (l1_ref, 6, 3),
        (l1_ref, 2, None),
    ]
    for (l, x, outcome) in tests:
        assert binary_search(l, x) == outcome
    return True

def test_binary_search_recursive():
    le = []
    l0 = [0]
    l1_ref = [-2, -1, 5, 6, 7, 8, 9]
    tests = [
        (le, 5, None),
        (l0, 0, 0),
        (l1_ref, -2, 0),
        (l1_ref, 9, 6),
        (l1_ref, 6, 3),
        (l1_ref, 2, None),
    ]
    for (l, x, outcome) in tests:
        assert binary_search_recursive(l, x) == outcome
    return True


def test_binary_search_recursive():
    le = []
    l0 = [0]
    l1_ref = [-2, -1, 5, 6, 7, 8, 9]
    tests = [
        (le, 5, (None, None)),
        (l0, 0, (0, 0)),
        (l1_ref, -2, (-2, 0)),
        (l1_ref, 9, (9, 6)),
        (l1_ref, 6, (6, 3)),
        (l1_ref, 2, (None, None)),
    ]
    for (l, x, outcome) in tests:
        assert binary_search_closest(l, x) == outcome
    return True


if __name__ == '__main__':
    test_bubble_sort()
    test_selection_sort()
    test_insertion_new_sort()
    test_insertion_sort()
    test_insert()
    test_insertion2_sort()
    test_insertion3_sort()
    test_insertion4_sort()
    test_sorted_matrix_search()
    test_quick_sort()
    test_merge_sort()
    test_binary_search()
    test_binary_search_recursive()
    test_binary_search_closest()
