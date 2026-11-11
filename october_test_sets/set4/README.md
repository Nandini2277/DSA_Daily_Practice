set 04 DSA Practice Set

- Q1. peak traffic window: {solved on custom set}
    time complexity: O(n)
    space complexity: O(1)
    approach: sum first k values, then slide window by adding a[i] and removing a[i - k]. track best.
    initial error: starting best at 0, wrong for negative totals
    mitigation: started best at first window sum.

- Q2. repeated login alert: {solved on custom set}
    time complexity: O(n)
    space complexity: O(n)
    approach: dict stores last index of each ID. if ID seen and i - last <= k, print YES.
    initial error: not updating last index
    mitigation: update dict on every step.

- Q3. strong average days: {solved on custom set}
    time complexity: O(n)
    space complexity: O(1)
    approach: avoid fractions by comparing window sum with k * T. slide window and count qualifying windows.
    initial error: skipping first window
    mitigation: checked first window before loop.

- Q4. plagiarism pattern scanner: {solved on custom set}
    time complexity: O(26 * n)
    space complexity: O(1)
    approach: two 26-slot count lists for p and window. slide window, add new char, remove old char, compare lists, save start index on match.
    initial error: not handling len(p) > len(s)
    mitigation: only run when m <= n, print None if no match.

- Q5. longest unique scan run: {solved on custom set}
    time complexity: O(n)
    space complexity: O(n)
    approach: dict stores last index of each code. if code seen at index >= left, move left to last + 1. track longest window.
    initial error: moving left backwards
    mitigation: checked last[x] >= left first.