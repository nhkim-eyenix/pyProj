# a = "Hello "
# print(a * 3)
# print(a[0])
# print(a[3])
# # b = int(input("Input your age: "))
# # print("Ah! Your age is %d" %b)
#
# print(type(a))
# a = 3
# print(type(a))
#
# # write down next line
# b = 100 + 200 + \
#     300 + 400 + \
#     500
#
# print(b, type(b))

# # Using a function
# def add(x, y):
#     return x+y
#
# print(add(3, 5))
#
# # f-string formatting
# def ggd(m):
#     for n in range(1, 10):
#         d = f'{m} * {n} = {m * n}'
#         print(d)
# ggd(5)

# # power of number
# print("5^3 is %d" %5**3)

# tuple
print("## tuple ##")
tp1 = ()
tp2 = (1, )
tp3 = (1, 2, 3, 4, 5)
tp4 = (1, 2, (3, 4, 5))
tp5 = 1, 2, 3
print(tp1, tp2, tp3, tp4, tp5)
print(tp3[1])
print(tp4[2])
print(len(tp4))
tp6 = tp4 + tp5
print(tp6)
print(len(tp6))

# # Dictionary 2021-08-05 목 18:01
# # https://blog.myungseokang.dev/posts/python-basic-grammar1/
# dic1 = dict()
# dic2 = {'k1': 'v1', 'k2':'v2', 'k3':'v3'}
# dic3 = dict([('name', 'Kyle'), ('phone', '010-3280-9111')])
# dic4 = dict(firstName = 'Kyle', lastName = 'Kim')
# dic5 = {'ls': ['a', 'b', 'c']}
# print("## dictionay ##")
# print(dic1)
# print(dic2['k2'])
# print(dic3['phone'])
# print(dic4['firstName'])
# print(dic5['ls'][1])
# print(dic5)