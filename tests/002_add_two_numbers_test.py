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
    result_array = to_array(result)
    expected_array = to_array(expected)

    assert result_array == expected_array

def to_array(nodes):
    ret = []
    node = nodes
    while node:
        ret.append(node.val)
        node = node.next
    
    return ret

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


'''
Input: [2,4,3] + [5,6,4]
output: [7,0,8]
'''
def test_4():
    l1 = buildNodes([2, 4, 3])
    l2 = buildNodes([5, 6, 4])
    expectation = buildNodes([7, 0, 8])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    assertNodes(result, expectation)


'''
Input: [5] + [5]
output: [0,1]
'''
def test_5():
    l1 = buildNodes([5])
    l2 = buildNodes([5])
    expectation = buildNodes([0, 1])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    assertNodes(result, expectation)

'''
Input: [9,1,6] + [0]
Output: [9, 1, 6]
'''
def test_6():
    l1 = buildNodes([9, 1, 6])
    l2 = buildNodes([0])
    expectation = buildNodes([9, 1, 6])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    assertNodes(result, expectation)
