# Higher Order Function: 
#A Function accept a fucntion as a parameter or return a fucntion

def great(func):
    func()

def greet2():
    def func():
        return 5
    return func