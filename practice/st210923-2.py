names = {'M': 1000, 'N': 2000, 'O': 3000}
k = input('Input the name you want.')
if k in names:
    print('The number of the person that has the name, %s are %d' %(k, names[k]))
else:
    print('There is no data')