def hello():
    print("Hello World")
hello()

def hello(name):
    print("Hello " +name)
hello("Mike")
print("--------------")
def hello(name, age):
    print(name +" is of age: " + age)
hello("John", "28")
#OR
def hello(name, age):
    print(name +" is of age: " + str(age))
hello("John", 28)
