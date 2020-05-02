import numpy
# Boyer Moore Algorithm Class

class BoyerMoore:
    def __init__(self, pattern):
        self.pattern = pattern
        self.last = [-1]*256
        self.lastOccurenceComputation()

    def lastOccurenceComputation(self):
        for i in range(0, self.patternSize(), 1):
            self.last[self.pattern[i]] = i

    def patternSize(self):
        return len(self.pattern)

    def getLastIdx(self, index):
        return self.last[index]

    def search(self, text):
        n = len(text)
        m = self.patternSize()
        j = m - 1
        i = j
        if( i > n - 1):
            return -1
        else:
            while(True):
                if(self.pattern[j] == text[i]):
                    if(j == 0):
                        return i
                    else:
                        i = i - 1
                        j = j - 1
                else:
                    lastOccurence = self.getLastIdx(text[i])
                    i = i + m - min(j, 1 + lastOccurence)
                    j = m - 1

                if(i > n-1):
                    return -1
            

def check(pattern, text):
    pos = -1
    k = 0
    i = 0
    while(i < len(text) and k < len(pattern)):
        # print("k : " + str(k))
        theBM = BoyerMoore(pattern[k])
        searchRes = theBM.search(text[i])
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
