day 32 DSA Daily Practice 02.11.2026

problems solved:
- to lower case: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(n)
    approach: for each char, if ord is 65 to 90 add 32, else keep it. join list at end.
    initial error: shifted every character
    mitigation: only shift when code is in 65 to 90.

- capitalize the title: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(n)
    approach: split into words. words of length 1 or 2 are all lowercase, longer words get uppercase first letter and lowercase rest, using ord shifts by 32.
    initial error: capitalizing short words
    mitigation: check len(w) > 2 before uppercasing 1st letter.

- defanging an ip address: {solved on leetcode}
    time complexity: O(n)
    space complexity: O(n)
    approach: copy each char into list, writing "[.]" for ".", then join.
    initial error: edited the string in place
    mitigation: build new list and join.