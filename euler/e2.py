# Project Euler
# 2021-09-14

thresholdValue = 4000000
number = [1, 2]                         # n1, n2
i = 0

while True:
    lastNumber = number[i] + number[i + 1]
    if lastNumber >= thresholdValue:
        break
    number.append(lastNumber)
    i += 1

print(number)

# evenNumber = []
sum = 0
for e in number:
    if e % 2 == 0:
        # print(e)
        # evenNumber.append(e)
        sum += e
print(sum)