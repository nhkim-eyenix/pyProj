# eval()
# eval() runs the code by taking the character string that is possible to run as a parameter.
# src 134.py
# 2021-10-01


expr1 = '2 + 3'
expr2 = 'round(3.7)'
expr3 = 'print(\'This is a practice about eval().\')'
ret1 = eval(expr1)
ret2 = eval(expr2)
ret3 = eval(expr3)
print('<%s>를 eval()로 실행한 결과: ' % expr1, end=''); print(ret1)
print('<%s>를 eval()로 실행한 결과: ' % expr2, end=''); print(ret2)
print(ret3)