# local
new_x = lambda x: x**2

#enclosing function locals
name = 'This is a global name!'

def greet():
    #name = "sammy" -> It looks for local and then global
    def hello():
        print("hello " + name)

    hello()

x = 50

# This function doesn't modify x -> once it goes out the function it would go back as 50
def func(x):
    x = 1000
    print(x)

# To modify x in a funcion to 1000 -> avoid using global as much as possible
def func2():
    global x
    x = 1000

if __name__ == '__main__':
    greet()
    print(new_x(5))
    print("Before runing func")
    print(x)
    print("During ejecution func")
    func(x)
    print("After ejecution func")
    print(x)
    print("Modified using func2")
    func2()
    print(x)
    # hello() -> only exists inside of greet