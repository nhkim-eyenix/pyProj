# If it is input an integer value, it returns a character that is related the value.
# chr() is the opposite of src().
# src 133.py
# 2021-09-27

val = input('Input char\'s code value:' )
val = int(val)
try:
    ch = chr(val)
    print('code value: %d[%s], char: %s' %(val, hex(val), ch))
except ValueError:
    print("It doesn\'t exist the character you input!" % val)

