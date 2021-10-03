# src 135.py
# lambda function
# The lambda function is a simple function consisting of one sentence.

# 1
add = lambda x, y: x+y
ret = add(1, 3)
print(ret)

# 2
funcs = [lambda x: x+'.pptx', lambda x: x+'.docx']
ret1 = funcs[0]('Intro')
ret2 = funcs[1]('Report')
print(ret1)
print(ret2)

#3