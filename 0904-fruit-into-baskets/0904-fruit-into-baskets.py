class Solution(object):
    def totalFruit(self, fruits):
        freq = {}
        left = 0
        max_length = 0
        for right in range(len(fruits)):
            freq[fruits[right]] = freq.get(fruits[right],0)+1
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]

                left+=1

            max_length = max(max_length,right-left+1)
        return max_length
        