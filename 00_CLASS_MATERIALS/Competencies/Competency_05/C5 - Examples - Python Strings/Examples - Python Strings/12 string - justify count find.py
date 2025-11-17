var=’Python’
print (var.rjust(10))
# Python
print (var.ljust(10,’-‘))
# Python—-

var=’Python’
print (var.ljust(10))
# Python
print (var.ljust(10,’-‘))
# Python—-

var=”Tech Beamers”
str=”Beam”
print (var.find(str))
# 5
var=”Tech Beamers”
str=”Beam”
print (var.find(str,4))
# 5
var=”Tech Beamers”
str=”Beam”
print (var.find(str,7))
# -1

var=’This is a good example’
str=’is’
print (var.count(str))
# 2
print (var.count(str,4,10))
# 1
