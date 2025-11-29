a = 40      # Create object <40>
b = a       
c = [b]     
print(c)
print(b)

del a       
b = 100     
c[0] = -1   
print(c)
