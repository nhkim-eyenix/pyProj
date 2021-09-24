val = input('Input the char code')
val = int(val)

try:
    ch = chr(val)
    print('code value: %d[%s], char: %s' %(val, hex(val), ch))
except ValueError:
    print('Don\'t exist <%d>' %val)