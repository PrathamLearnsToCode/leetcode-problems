class Solution:
    def reverseWords(self, s: str) -> str:
        split_words = s.split(' ')
        reversed_words = []
        for word in split_words:
            reversed_word = word[::-1]
            reversed_words.append(reversed_word)
            
        res = ' '.join(reversed_words)
        
        return res