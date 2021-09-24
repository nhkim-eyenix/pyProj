# 문장에 나타나는 문자 빈도수 구하기.
# Source 166.py

def getTextFreq(filename):
    with open(filename, 'r') as f:
        text = f.read()
        fa = {} # fa is dictionary.
        for c in text:
            if c in fa:     # If c exists in dictionary, f
                fa[c] += 1  # add 1 at index c's value
            else:
                fa[c] = 1
    return fa

ret = getTextFreq('mydata.txt')
ret = sorted(ret.items(), key=lambda x:x[1], reverse = True)
for c, freq in ret:
    if c == '\n':
        continue
    print('[%c] -> [%d] 회 나타남' %(c, freq))


