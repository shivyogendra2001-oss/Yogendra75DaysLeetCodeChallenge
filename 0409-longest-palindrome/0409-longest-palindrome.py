class Solution(object):
    def longestPalindrome(self, s):
        freq = {}

        # Count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        length = 0
        odd_found = False

        # Calculate palindrome length
        for count in freq.values():
            length += (count // 2) * 2

            if count % 2 == 1:
                odd_found = True

        if odd_found:
            length += 1

        return length