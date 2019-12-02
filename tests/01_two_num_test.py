from problems.two_sum import Solution

def test_no1():
    sol = Solution()

    result = sol.twoSum([], 1)
    assert len(result) != 0