import re

# Regular Expression Class

class RegularExpression:
    def __init__(self, pattern):        
        self.pattern = pattern
    
    def search(self, text):
        res = re.search(self.pattern, text)
        if res is not None:
            return res.start()
        else:
            return -1

def check(pattern, text):
    pos = -1
    k = 0
    i = 0
    while(i < len(text) and k < len(pattern)):
        # print("k : " + str(k))
        theRE = RegularExpression(pattern[k])
        searchRes = theRE.search(text[i])
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
