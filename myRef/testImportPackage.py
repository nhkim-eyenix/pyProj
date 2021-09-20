# 1 To import the library using the package's name
import myPack1.myLib
ret1 = myPack1.myLib.add_txt("the 1st way.", "That is")
ret2 = myPack1.myLib.reverse(1, 2, 3)
print(ret1)
print(ret2)
myPack1.myLib.separtor()

# 2 To import my library using 'from'
from myPack1 import myLib
print(myLib.add_txt('the 2nd way.'))
myLib.separtor()

# 3 To import specific function from my library
from myPack1.myLib import add_txt
print(add_txt("the 3rd way."))
from myPack1.myLib import separtor
separtor()

# 4 To import my library using alias
import myPack1.myLib as l
print(l.add_txt("the 4th way."))
l.separtor()
