class Animal:
    def _init_(self, name):
        """Constructor: Initializes an Animal object with a name."""
        self.name = name
        print(f"{self.name}'s object has been created")

    def make_sound(self):
        """Prints a message indicating the animal is making a sound."""
        print(f"{self.name} is now making sound")

    def walk(self):
        """Prints a message indicating the animal is walking."""
        print(f"{self.name} is now walking")

    def _del_(self):
        """Destructor: Called when the object is about to be destroyed."""
        print(f"{self.name} object has been deleted")

# Creating instances and calling methods
if _name_ == "_main_":
    dog = Animal("Buddy")
    dog.make_sound()
    dog.walk()

    cat = Animal("Bills")
    cat.make_sound()
    cat.walk()

    # Deleting objects
    del dog
    del cat

    # Attempting to call a method on a deleted object will result in an error
    # cat.make_sound()  # Uncommenting this line will give an error
