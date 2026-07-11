class Solution(object):
    def countConsistentStrings(self, allowed, words):
        
        count = 0

        for word in words:

            ok = True

            for ch in word:

                if ch not in allowed:
                    ok = False
                    break

            if ok:
                count += 1

        return count
    
# Time Complexity: O(n × m × k)

# where:
# n = number of words
# m = average length of each word
# k = length of allowed string

# Reason:
# - We iterate through each word.
# - Then we iterate through each character of the word.
# - For every character, we check `ch not in allowed`.
# - Since `allowed` is a string, membership checking takes O(k) time.
# - Therefore, the overall time complexity is O(n × m × k).