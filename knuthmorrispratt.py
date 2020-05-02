# Knuth Morris Prrat Algorithm Class

class KnuthMorrisPrrat:
    def __init__(self, pattern):
        
        self.pattern = pattern
        self.bordertable = [0]*self.patternSize()

        self.bordertable[0] = -1
        self.bordertable[1] = 0
        i = 2
        same = 0

        while(i < self.patternSize()):
            if(self.pattern[i-1] == self.pattern[same]):
                same = same + 1
                self.bordertable[i] = same
                i = i + 1
            else:
                if(same > 0):
                    same = self.bordertable[same]
                else:
                    self.bordertable[i] = 0
                    i = i + 1                    

    def createBorder(self, idx):
        self.bordertable = [0]*self.patternSize()

        self.bordertable[0] = -1
        self.bordertable[1] = 0
        i = 2
        same = 0

        while(i < self.patternSize()):
            if(self.pattern[i-1] == self.pattern[same]):
                same = same + 1
                self.bordertable[i] = same
                i = i + 1
            else:
                if(same > 0):
                    same = self.bordertable[same]
                else:
                    self.bordertable[i] = 0
                    i = i + 1      

    def patternSize(self):
        return len(self.pattern)

    def getBorderIdx(self, index):
        return self.bordertable[index]
    
    def search(self, text):
        i = 0; j = 0
        n = len(text); m = self.patternSize()
        while(i < n):
            if(self.pattern[j] == text[i]):
                if(j == m-1):
                    return i - m + 1
                i = i + 1
                j = j + 1
            elif(j > 0):
                j = self.getBorderIdx(j)
            else:
                i = i + 1

        return -1

def check(pattern, text):
    pos = -1
    k = 0
    i = 0
    while(i < len(text) and k < len(pattern)):
        # print("k : " + str(k))
        theKMP = KnuthMorrisPrrat(pattern[k])
        searchRes = theKMP.search(text[i])
        if(searchRes != -1):
            # print("masukk")
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
