
class Snake:
    def getname(self):
        return self._name

    def setname(self, value):
        # When property is set, capitalize it.
        self._name = value.capitalize()

    name = property(getname, setname)

# Create a snake instance.
s = Snake()

# Set name property.
s.name = "rattle"

# Get name property.
print(s.name)
