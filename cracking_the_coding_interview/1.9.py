'''
다시보기
미쳤네에에에
'''

def checkRotated(s1, s2):
    if not len(s1) or len(s1) != len(s2): return False
    return isSubstring(s1+s1, s2)