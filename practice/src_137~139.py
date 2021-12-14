# src 137.py

f = open('stockcode.txt', 'r')
data = f.read()
print(data)
f.close()

# src 138.py
f2 = open('stockcode.txt', 'r')
line_num = 1
line = f2.readline()
while line:
    print('%d %s' %(line_num, line), end='')
    line = f2.readline()
    line_num += 1
f2.close()
print('n')
print('# 3 ===================================')
# src 139.py
f3 = open('stockcode.txt')
lines = f3.readlines()
for line_num, line in enumerate(lines):
    print('%d, %s' %(line_num + 1, line), end='')
f3.close()