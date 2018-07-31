def two_sum(nums, target):
    d = dict()
    for i in range(len(nums)):
        comp = target - nums[i]
        if comp in d:
            return [d[comp], i]
        d[nums[i]] = i


def test_two_sum():
    test_cases = [
        ([1, 2, 3], 4, [0, 2]),
        ([1234, 5678, 9012], 14690, [1, 2]),
        ([2, 2, 3], 4, [0, 1]),
    ]
    for numbers, target, outcome in test_cases:
        assert two_sum(numbers, target) == outcome
