class Dog:
    def run(self):
        print('dog run')
    def eat(self):
        print('dog eat')
class Cat:
    def run(self):
        print('cat run')
    def eat(self):
        print('cat eat')
class Tiger:
    def run(self):
        print('tiger run')
    def eat(self):
        print('tiger eat')
def test(animal):
    animal.run()
    animal.eat()
def main1():
    dog = Dog()
    dog.run()
    dog.eat()
    cat = Cat()
    cat.run()
    cat.eat()
    tiger = Tiger()
    tiger.run()
    tiger.eat()
main1()


def main1():
    dog = Dog()
    cat = Cat()
    tiger = Tiger()
    test(cat)
    test(dog)
    test(tiger)
main1()