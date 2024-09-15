class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Init name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting response to a command"""
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        """Simulate a rollover command"""
        print(f'{self.name} rolled over!')

my_dog = Dog('Steve', 48)
your_dog = Dog('Caity', 40)
print(my_dog.name)
print(my_dog.age)

my_dog.sit()
my_dog.roll_over()
your_dog.roll_over()
