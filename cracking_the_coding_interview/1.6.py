def compress(s):
    ret = []
    current = s[0]
    current_count = 0
    for c in s[1:]:
        if c == current:
            current_count += 1
        else:
            if current_count:
                ret.append(current)
                ret.append("{}".format(current_count))
            current_count = 1
            current = c

    ret.append(current)
    ret.append("{}".format(current_count))
    return ''.join(ret) if len(ret) <= len(s) else s

def countCompress(s):
    l = 0
    current = ""
    current_count = 0
    for c in s:
        if c == current:
            current_count += 1
        else:
            if current_count:
                l+=1
                l += len(str(current_count))
            current_count = 1
            current = c
    l += 1
    l += len(str(current_count))
    return l



s = "aaaaaaaabccdeeaa"
print(compress(s))
print(countCompress(s))