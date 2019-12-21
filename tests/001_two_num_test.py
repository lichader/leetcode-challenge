from problems.two_sum import Solution

def test_sample_1():
    sol = Solution()

    result = sol.twoSum([2, 7, 11, 15], 9)
    assert result == [0, 1]

def test_sample_2():
    sol = Solution()

    result = sol.twoSum([1, 4, 0, 9], 9)
    assert result == [2, 3]