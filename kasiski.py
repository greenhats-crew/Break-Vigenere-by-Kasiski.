import re
import math
def kasiski(s, min_num = 4):
    dictionary = {}
    s = s.strip().upper()
    s = re.sub(r'[^A-Z]+', '', s)
    matches = []
    found = {}
    for k in range(min_num, len(s) // 2):
        found[k] = {}
        shouldbreak = True
        for i in range(0, len(s) - k):
            v = s[i:i+k]
            if v not in found[k]:
                found[k][v] = 1
            else:
                found[k][v] += 1
                shouldbreak = False
        if shouldbreak:
            break
        for v in found[k]:
            if found[k][v] > 1:
                matches.append(v)
    keylens = {}
    for v in matches:
        k = len(v)
        p = []
        for i in range(len(s)):
            if s[i:i+k] == v:
                p.append(i)
        factor = p[1] - p[0]
        for i in range(2, len(p)):
            factor = math.gcd(factor, p[i] - p[i - 1])
        locations = ""
        for i in range(len(p)):
            locations += "%d " % p[i]
            if i > 0:
                locations += "(%d) " % (p[i] - p[i-1])
        dictionary.update({v: [k,found[k][v],locations,factor]})
    return dictionary
