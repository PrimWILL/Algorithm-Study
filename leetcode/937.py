class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = list()
        letter = list()
        
        for x in logs:
            if x.split(' ')[1].isdigit():
                digit.append(x)
            else:
                letter.append(x)
        
        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter + digit