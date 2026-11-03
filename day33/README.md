day 33 DSA Daily Practice 03.11.2026

problems solved:
- valid anagram: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: check lengths first. count chars of s up in dict, then count chars of t down. if count is missing or hits 0 before decrementing, return false.
    initial error: skipped length check
    mitigation: return false early when lengths differ.

- group anagrams: {solved on leetcode}
    time complexity: O(n * k)
    space complexity: O(n * k)
    approach: for each word build 26-slot count list, convert to tuple and use as dict key. append word to that key's list, then collect all lists.
    initial error: using list as dict key
    mitigation: converted count list to tuple.

- first unique character in a string: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(1)
    approach: first pass counts every char in dict. second pass walks string in order and returns 1st index with count 1, else -1.
    initial error: looped over dict, loses the original order
    mitigation: looped over string indices in second pass.