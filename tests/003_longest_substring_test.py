from problems.longest_substring import Solution

subject = Solution()

def test_scenario_1():
    string1 = "ababcde"
    result = subject.lengthOfLongestSubstring(string1)
    assert result == 5

def test_scenario_2():
    string1 = "ohaidfds"
    result = subject.lengthOfLongestSubstring(string1)
    assert result == 6

def test_scenario_3():
    string1 = "bbbbb"
    result = subject.lengthOfLongestSubstring(string1)
    assert result == 1


def test_scenario_4():
    string1 = "wke"
    result = subject.lengthOfLongestSubstring(string1)
    assert result == 3
