
class BruteForce:
    def __init__(self, pattern):        
        self.pattern = pattern
    
    def search(self, text):
        n = len(text)
        m = len(self.pattern)
        for i in range(0, n-m+1):
            j = 0
            while((j < m) and (text[i+j] == self.pattern[j])):
                j += 1
            if(j == m):
                return i
        return -1

def check(pattern, text):
    pos = -1
    k = 0
    i = 0
    while(i < len(text) and k < len(pattern)):
        theBF = BruteForce(pattern[k])
        searchRes = theBF.search(text[i])
        if(searchRes != -1):
            if(k == 0):
                pos = searchRes
                k = k + 1
            else:
                if(pos == searchRes):
                    k = k + 1
                else:
                    k = 0
        else:
            k = 0
        i = i + 1
    return(k != 0)
