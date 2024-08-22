class Solution(object):
    def mergeAlternately(self, word1, word2):
        i=0
        j=0
        output = []
        while i < len(word1) and j < len(word2):
            output.append(word1[i])
            output.append(word2[j])
            i+=1
            j+=1
        output.append(word1[i:])
        output.append(word2[j:])
        return "".join(output)
        