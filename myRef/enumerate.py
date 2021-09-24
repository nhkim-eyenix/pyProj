# enumerate: it makes the list that consists of (index, element) from the list of elements
# 2021-09-23
# source 120.py
solaysys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
ret = list(enumerate(solaysys))
print(ret)
print(type(ret))

for i, body in enumerate(solaysys):
    print('%d, %s' %(i, body))
    print(type(i))
    print(type(body))
