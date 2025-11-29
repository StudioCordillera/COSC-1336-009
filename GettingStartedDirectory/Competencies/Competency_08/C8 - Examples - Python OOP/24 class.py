from pets import Cat, Dog

fido = Dog("Fido", True)
print ("%s chases cats: %s" % (fido.getName(), fido.chasesCats()))

rover = Dog("Rover", False)
print ("%s chases cats: %s" % (rover.getName(), rover.chasesCats()))

mittens = Cat("Mittens", True)
print ("%s hates dogs: %s" % (mittens.getName(), mittens.hatesDogs()))

fluffy = Cat("Fluffy", False)
print ("%s hates dogs: %s" % (fluffy.getName(), fluffy.hatesDogs()))

