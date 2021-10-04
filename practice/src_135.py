# src 135.py
# lambda function
# The lambda function is a simple function consisting of one sentence.

# 1
add = lambda x, y: x+y
ret = add(1, 3)
print(ret)

sub = lambda x, y: x - y
print(sub(5, 3))

# 2
funcs = [lambda x: x+'.pptx', lambda x: x+'.docx']
ret1 = funcs[0]('Intro')
ret2 = funcs[1]('Report')
print(ret1)
print(ret2)

# 3
names = {'Mary': 10999, 'Sams': 2111, 'Aimy': 9778, 'Tom': 20245, 'Michale': 27115, 'Bob': 5887, 'Kelly': 7855}
print(names)
print('after sorting...')
ret3 = sorted(names.items(), key = lambda x: x[1])
print(ret3)