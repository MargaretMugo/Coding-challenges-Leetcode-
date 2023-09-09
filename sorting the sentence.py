# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.
#
# For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
#
#
#
# Example 1:
#
# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
class Solution:
    def sortSentence(self, s: str) -> str:
        words=list(s.split(" "))
        index_list = [0]*len(words)
        for word in words:
            index_list[int(word[-1])-1]=word[:-1]
        return " ".join(index_list)
