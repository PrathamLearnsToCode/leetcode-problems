class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for char in operations:
            if char not in {"C", "D", "+"}:
                record.append(int(char))
            elif char=="C":
                record.pop()
            elif char=="D":
                record.append(2*record[-1])
            elif char=="+":
                record.append(record[-1]+record[-2])
                
        return sum(record)
    
        