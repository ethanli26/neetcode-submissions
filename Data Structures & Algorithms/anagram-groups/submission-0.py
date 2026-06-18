class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        char_dic = {}

        for i in range(len(strs)):
            str_sorted = sorted(strs[i])
            if ''.join(str_sorted) in char_dic:
                char_dic[''.join(str_sorted)].append(strs[i])
            else:
                char_dic[''.join(str_sorted)] = [strs[i]]
        
        for lst in char_dic.values():
            result.append(lst)

        return result