class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length = 0
        for i in words:
            available_chars = list(chars)
            can_form = True
            for char in i:
                if char in available_chars:
                    available_chars.remove(char)
                else:
                    can_form = False
                    break
            if can_form:
                length += len(i)
                
        return length
            
                
                