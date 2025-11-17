var=' This is a good example '
print (var.lstrip())

# This is a good example
var='*****This is a good example'
print (var.lstrip('*'))
# This is a good example

var=' This is a good example '
print (var.rstrip())
# This is a good example

var='This is a good example*****'
print (var.rstrip('*'))
# This is a good example

var='This is a good example'
print (len(var))
# 22
