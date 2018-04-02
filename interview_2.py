"""
You are working on a project and you noticed that there has been a performance decrease between two releases. You have a function:

`boolean worseCommit(int commit1, int commit2)`

that runs performance tests and returns true if `commit2` is worse than `commit1` and false otherwise.

Find all of the bad commits that have decreased the performance between releases. Assume no improvement in performance.
"""


def worse_commit(commit1, commit2):
    """This is a stub to replace the given function, mimicing the
    performance graph.
    """
    assert commit1 > 0
    log = [None, 0, 0, 1, 1, 1, 2]
    return log[commit2] > log[commit1]


def test_worse_commit():
    assert worse_commit(1, 2) == False
    assert worse_commit(2, 3) == True
    return True


def find_worst_commits(first, last):
    log = list(range(first + 1, last + 1))
    worst_commits = []
    for i in log:
        commit1 = i - 1
        commit2 = i
        is_decrease = worse_commit(commit1, commit2)
        if is_decrease:
            worst_commits.append(commit2)
    return worst_commits


def test_find_worst_commits():
    ref = [3, 6]
    assert find_worst_commits(1, 6) == ref
    return True


"""
The above runs in O(N) time, where N is the length of the commit log. However, because `worse_commit` is quite expensive to run, can we do better than O(N)?

> Yes; since the log is sorted in chronological order, we can do binary search and reduce the time to O(log(N)).
"""


def find_worst_commits_log(first, last):
    return _find_worst_commits_log(first, last, [])


def _find_worst_commits_log(first, last, worst_commits):
    if first == last:
        return worst_commits
    mid = (first + last) // 2
    is_decrease_left = worse_commit(first, mid)
    if is_decrease_left:
        if (mid - first) == 1:
            worst_commits.append(mid)
        return _find_worst_commits_log(first, mid - 1)
    is_decrease_right = worse_commit(mid, last)
    if is_decrease_right:
        if (last - mid) == 1:
            worst_commits.append(last)
        return _find_worse_commits_log(mid + 1, last)
    return worst_commits


def test_find_worst_commits_log():
    ref = [3, 6]
    assert find_worst_commits_log(1, 6) == ref
    return True
