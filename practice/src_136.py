# src 136.py
# map function
# This maps arguments to a function.

# 1
f = lambda x: x*x
args = [1, 2, 3, 4, 5]
ret = map(f, args)
print(list(ret))

# 2
f2 = lambda x, y: x*x + y
X = [1, 2, 3, 4, 5]
Y = [10, 9, 8, 7, 6]
ret2 = map(f2, X, Y)
print(list(ret2))