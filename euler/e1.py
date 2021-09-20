# Project Euler #1
# 2021-09-09

value = []

ThresholdVaule = 1000

# Get the multiples of first number below threshold number
for i in range(ThresholdVaule):
    number1 = 3 * (i+1)
    if number1 >= ThresholdVaule:
        break
    value.append(number1)

# Get the multiples of second number below threshold number
for i in range(ThresholdVaule):
    number2 = 5 * (i+1)
    if number2 >= ThresholdVaule:
        break
    value.append(number2)

# To sort values
value.sort()
print(value)

print("After removing duplicated values")
# To remove duplicated value
# https://careerkarma.com/blog/python-remove-duplicates-from-list/
newValue = list(dict.fromkeys(value))
print(newValue)

# To get summation of the values
sum = 0
for item in newValue:
    sum = sum + item
    # print(item, sum)
print("The answer is %d" % sum)



