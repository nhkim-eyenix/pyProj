# study 210923
# Design STACK

mystack = []

def putdata(data):
    global mystack
    mystack.append(data)

def popdata():
    global mystack
    if len(mystack) == 0:
        return None
    return mystack.pop()
# ===============================================
putdata('data1')
putdata([3, 4, 5, 6])
putdata(12345)

print('<stack status>:', end=''); print(mystack)

ret = popdata()
while ret != None:
    print('Pop out data:', end=''); print(ret)
    print('<stack status>:', end=''); print(mystack)
    ret = popdata()
