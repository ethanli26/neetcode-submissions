class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = []
        tlist = []
        for char in s:
            slist.append(char)
        for char in t:
            tlist.append(char)

        sortedslist = sorted(slist)
        sortedtlist = sorted(tlist)

        if sortedslist == sortedtlist:
            return True

        return False