from pets import Pet

polly = Pet("Polly", "Parrot")
print ("Polly is a %s" % polly.getSpecies())

print ("Polly is a %s" % Pet.getSpecies(polly))
print(polly.getName())

print(polly.getSpecies())

print (polly)

ginger = Pet("Ginger", "Cat")
print(ginger.getName())
print(ginger.getSpecies())
print (ginger)


clifford = Pet("Clifford", "Dog")
print(clifford.getName())
print(clifford.getSpecies())
print(clifford)

from pets import Pet, Dog
mister_pet = Pet("Mister", "Dog")
mister_dog = Dog("Mister", True)

print(isinstance(mister_pet, Pet))
print(isinstance(mister_pet, Dog))
print(isinstance(mister_dog, Pet))
print(isinstance(mister_dog, Dog))


print(mister_dog.chasesCats())
print(mister_pet.getName())
print(mister_dog.getName())

from pets import Cat, Dog
fido = Dog("Fido", True)
rover = Dog("Rover", False)
mittens = Cat("Mittens", True)
fluffy = Cat("Fluffy", False)
print (fido)

print (rover)

print (mittens)

print (fluffy)

print ("%s chases cats: %s" % (fido.getName(), fido.chasesCats()))

print ("%s chases cats: %s" % (rover.getName(), rover.chasesCats()))

print ("%s hates dogs: %s" % (mittens.getName(), mittens.hatesDogs()))

print ("%s hates dogs: %s" % (fluffy.getName(), fluffy.hatesDogs()))







