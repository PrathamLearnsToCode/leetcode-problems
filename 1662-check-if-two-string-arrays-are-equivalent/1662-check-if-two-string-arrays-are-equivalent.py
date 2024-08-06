class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
      res1 = ""
      for i in word1:
        res1 = res1 + i
        
      res2 = ""
      for j in word2:
        res2 = res2 + j
        
      return res1==res2
        