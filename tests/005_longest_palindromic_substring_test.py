from problems.longest_palindromic_substring import Solution

subject = Solution()

def test_1():
    s1 = "babad"
    result = subject.longestPalindrome(s1)
    assert (result == 'aba') or (result == "bab")


def test_2():
    input = "cbbd"
    result = subject.longestPalindrome(input)
    assert result == "bb"

def test_3():
    input = "a"
    result = subject.longestPalindrome(input)
    assert result == "a"


def test_4():
    input = "bb"
    result = subject.longestPalindrome(input)
    assert result == "bb"


def test_5():
    input = "ccd"
    result = subject.longestPalindrome(input)
    assert result == "cc"
