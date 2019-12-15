from problems.list_node import ListNode
from problems.add_two_numbers import Solution


'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
output: 7 -> 0 -> 8
'''
def test_1():
    solution = Solution()
    l1 = buildNodes([2, 4, 3])
    l2 = buildNodes([5, 6, 4])
    expectation = buildNodes([7, 0, 8])
    result = solution.addTwoNumbers(l1, l2)
    assertNodes(result, expectation)

def buildNodes(digits):
    firstNode = ListNode(digits[0])
    node = firstNode
    for index in range(1, len(digits)):
        temp = ListNode(digits[index])
        node.next = temp
        node = temp

    return firstNode

def assertNodes(result, expected):
    n1 = result
    n2 = expected
    while n2.next:
        assert n1.val == n2.val
        n1 = n1.next
        n2 = n2.next

'''
Input: (1 -> 2) + (3 -> 5 -> 7)
output: (4 -> 7 -> 7)
'''
def test_2():
    l1 = buildNodes([1, 2])
    l2 = buildNodes([3, 5, 7])
    expectation = buildNodes([4, 7, 7])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    assertNodes(result, expectation)

'''
Input: (9 -> 2 -> 3) + (2 -> 8)
output: (1 -> 1 -> 4)
'''
def test_3():
    l1 = buildNodes([9, 2, 3])
    l2 = buildNodes([2, 8])
    expectation = buildNodes([1, 1, 4])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    assertNodes(result, expectation)
