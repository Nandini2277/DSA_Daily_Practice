day 34 DSA Daily Practice 04.11.2026

problems solved:
- ransom note: {solved on leetcode}
    time complexity: O(m + n)
    space complexity: O(1)
    approach: count letters of magazine in dict. for each letter in ransomNote, return false if count is 0, else decrement it.
    initial error: swapped which string is counted
    mitigation: count magazine, spend letters for ransomNote.

- find common characters: {solved on leetcode}
    time complexity: O(total characters)
    space complexity: O(1)
    approach: start with counts of first word. for each next word, build its dict and keep minimum count per letter. at end, repeat each letter count times.
    initial error: kept only letters, lost duplicates
    mitigation: stored counts and took minimum per letter.

- jewels and stones: {solved on leetcode}
    time complexity: O(j + s)
    space complexity: O(j)
    approach: put jewel letters in set. walk stones and add 1 whenever letter is in set.
    initial error: nested loops, which is O(j * s)
    mitigation: used dict for O(1) lookup.