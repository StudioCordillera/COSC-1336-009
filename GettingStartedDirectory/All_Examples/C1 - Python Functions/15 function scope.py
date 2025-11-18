# scope

def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('inner_function >> a =',a)

    inner_function()
    print('outer_function >> a =',a)
     
a = 10
outer_function()
print('original >> a =',a)
