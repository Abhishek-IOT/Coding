"""
a word or phrase that is made by arranging the letters of another word or phrase in a different order.But has same frequency

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        d={}
        if len(s)<len(t):
            s,t=t,s
        for i in s:
            if i in d:
                d[i]+=1
            else :
                d[i]=1
        
        for j in t:
            if j in d:
                d[j]-=1
        
        if max(d.values())>0:
            return False
        return True