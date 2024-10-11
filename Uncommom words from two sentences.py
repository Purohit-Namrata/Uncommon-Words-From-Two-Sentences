from typing import List
from collections import defaultdict

class Solution:
    def uncommonFromSentence(self,s1:str,s2:str)->List[str]:
        count=defaultdict(int)

        for i in s1.split(" ")+ s2.split(" "):
            count[i]+=1
        print(count)
        
        res=[]
        for i,c in count.items():
            if c==1:
                res.append(i)
        return res
    

s1="the apple is sweet"
s2="the apple is sour"
s=Solution()
print(s.uncommonFromSentence(s1,s2))