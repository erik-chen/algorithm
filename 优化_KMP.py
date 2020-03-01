"""
    题目：给定长字符串和短字符串，判断后者是否为前者的子字符串，若是，返回第一个匹配成功的位置，
         若不是，返回-1
    作者：陈志豪
    日期：2019、07、15
"""
import copy
import random
import time

def kmp_advanced(s, t):
            def forward2(forward, special):
                forward2 = copy.deepcopy(forward)
                for i in range(1, len(special)):
                    j = i
                    while j + 1 - forward2[j] == special[j] and special[j]:
                        forward2[j] = copy.deepcopy(forward2[j] + forward2[special[j] - 1])
                        # while j + 1 - forward2[j] == special[j] and special[j]:
                        #     forward2[j] = copy.deepcopy(forward[j] + forward[special[j] - 1])
                        j = special[j]
                return forward2

            def forward(special):
                forward = [-10000 for x in range(len(special))]
                forward[0] = 1
                for i in range(len(special) - 1):
                    forward[i + 1] = i + 1 - special[i]
                return forward

            def special(t):
                tlen = len(t)
                special = [0 for x in range(tlen)]
                special[0] = 0
                for i in range(2, tlen + 1):
                    for j in range(i - 1, 0, -1):
                        if equal(t, i, j):
                            special[i - 1] = j
                            break
                return special

            def equal(t, i, j):
                for k in range(j):
                    if t[k] != t[i - j + k]:
                        return False
                return True


            i = 0
            j = 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                    j += 1
                    if j == len(t):
                        return i-j
                else:
                    special_kk = special(t)
                    forward_kk = forward(special_kk)
                    forward2_kk = forward2(forward_kk, special_kk)
                    i -= j
                    i += forward2_kk[j]
                    j = 0
            return -1





def rand_str(length):
    str_0 = ''
    for i in range(length):
        str_0 += (random.choice("abcabbbbbbbbbbbaaaaaaadefghiaaaaaaaaajklmnopqrstuvwxyz"))
    return str_0


def rand_str2(length):
    str_0 = ''
    for i in range(length):
        str_0 += (random.choice("aaabba"))
    return str_0


# s=rand_str(2000000)
# t =rand_str2(12)
time1 = time.time()
print("KMP优化算法：第%d位" % kmp_advanced("bcacbcbbbbbbbacbcaacbccaa",
"bbcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaaabcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaaabcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaaabcacbcbbbbbbbacbcaacbccaaabcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaabbcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaacbcacbcbbbbbbbacbcaacbccaaabcacbcbbbbbbbacbcaacbccaaa"))
time2 = time.time()
print(time2-time1)

