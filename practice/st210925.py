# 2021-09-25 Sat
# Source 132.py

# ord(): To get char code value of the character

ch = input('Input one character ')
if len(ch) != 0:
    ch = ch[0]
    chv = ord(ch)
    print('char: %s \t code value: %d [%s]' %(ch, chv, hex(chv)))