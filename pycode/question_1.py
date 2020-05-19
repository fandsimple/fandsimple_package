# 验证变位词
# 输入为两个字符串，分别为s, t 判断两个字符串是否属于变位字符串
# 举例1
# Input: s = "anagram", t = "nagaram"
# Output: true
# 举例2 
# Input: s = "rat", t = "car"
# Output: false


# 思路一
class SolutionOne:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = list(s)
        n = list(t)
        m.sort()
        n.sort()
        if m == n:
            return True
        else:
            return False


# 思路二
class SolutionTwo:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_table = {}
        for i in s:
            if i not in hash_table:
                hash_table[i] = 1
            else:
                hash_table[i] += 1
        for i in t:
            if i not in hash_table:
                return False
            else:
                hash_table[i] -= 1
                if hash_table[i] == 0:
                    hash_table.pop(i)
        return hash_table == {}


if __name__ == '__main__':
    s1 = SolutionOne()
    s2 = SolutionTwo()
    print(s1.isAnagram('123', '321'))
    print(s2.isAnagram('123', '321'))
