# practice 1
# class Calculator:
#     def __init__(self):
#         self.result = 0
#
#     def add(self, num):
#         self.result += num
#         return self.result
#
# cal1= Calculator()
# cal2 = Calculator()
#
# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))
# print(type(cal1))

# =======================================
# practice 2
# class Engineer:
#     def __init__(self):
#         self.tList = []
#
#     def addTool(self, tool):
#         self.tList.append(tool)
#         return
#
# kyle = Engineer()
# kyle.addTool("PADS")
# kyle.addTool("EXCEL")
# kyle.addTool("Python")
#
# print(kyle.tList)

# 3 =======================================
class Person:
    def __init__(self):
        self.name = None
        self.age = None

    def setName(self, newName):
        self.name = newName
        print("The name was set %s." %(newName))

    def setAge(self, newAge):
        self.age = newAge
        print("The age was set %d" %newAge)

k = Person()

k.setName("Kyle")
k.setAge(30)

print("k's name is %s, and his age is %d" % (k.name, k.age))




