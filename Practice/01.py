print ("Hello World!")
#Python supports two types of numbers - integers and floating point numbers.

number = 7
print(number)
flotnumber = 7.0
print(flotnumber)
myflot = float(8)
print(myflot)
#Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner.
mylist = []
mylist.append(1)
mylist.append(2.0)
for x in mylist:
    print(x)

squired = 7 ** 2
qube = 2 ** 3
print(squired)
print(qube)
oddnumber = [2,4,6]
evennumber = [1,3,5]
allnumbers = oddnumber + evennumber
print(allnumbers)
name = "jijeesh"
age = 20
print("my name is %s and the age is %d" % (name,age))
print("my list is %s" %mylist)
x = 3
if x == 2:
    print("x = 2")
elif x == 3:
    print("x=3")
else:
    print("not ")
def My_function():
    print("this is my function")

def My_args(name,age):
    print("my name is %s and age %d" %(name,age))

def addvalues(x,y):
    return x+y

My_function()
My_args("jijeesh",20)
print(addvalues(5,6))
print(addvalues(5,6))

class MyClass:
    myvariable = "jijeesh"
    phonebook = {
        "jijeesh" : 1234,
        "mon" : 456
    }
    def myclassFunction(self):
        print("This is class function")

myobj = MyClass()

print(myobj.myvariable)
myobj.myclassFunction()
for name,num in myobj.phonebook.items():
    print("%s's phone number is %d" %(name,num))

