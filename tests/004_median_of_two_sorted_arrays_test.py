from problems.median_of_two_sorted_arrays import Solution

subject = Solution()

def test_scenario_1():
    a1 = [1, 2]
    a2 = [3, 4]

    result = subject.findMedianSortedArrays(a1, a2)
    assert result == 2.5

def test_scenario_2():
    a1 = [1, 3]
    a2 = [2, 3, 6, 8]

    result = subject.findMedianSortedArrays(a1, a2)
    assert result == 3

def test_scenario_3():
    a1 = [2, 6, 9]
    a2 = [5, 7, 8]
    
    result = subject.findMedianSortedArrays(a1, a2)
    assert result == 6.5

def test_scenario_4():
    a1 = [12, 28]
    a2 = [10, 14, 27]

    result = subject.findMedianSortedArrays(a1, a2)
    assert result == 14


def test_scenario_5():
    a1 = [1, 3]
    a2 = [2]

    result = subject.findMedianSortedArrays(a1, a2)
    assert result == 2.0


def test_scenario_6():
    a1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4]
    a2 = [1, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]

    result = subject.findMedianSortedArrays(a1, a2)
    assert result == 3.0


def test_scenario_7():
    a1 = [1, 2]
    a2 = [-1, 3]

    result = subject.findMedianSortedArrays(a1, a2)
    assert result == 1.5


def test_scenario_8():
    a1 = [1, 1]
    a2 = [1, 2]

    result = subject.findMedianSortedArrays(a1, a2)
    assert result == 1
