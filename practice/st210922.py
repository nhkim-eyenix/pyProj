strdata = input('Input the string you want to sort: ')
ret1 = sorted(strdata)
ret2 = sorted(strdata, reverse=True)
print(ret1)
print(ret2)
# join: concate as string
ret1 = ''.join(ret1)
ret2 = ''.join(ret2)
print(ret1)
print(ret2)