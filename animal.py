class Animal(object):
    def __init__(self,name,health):
        self.name= name
        self.health=health

    def walk(self):
        self.health -= 1
        print "steps walked:",self.health
        return self

    def run(self):
        self.health -= 5
        print "no of steps ran:",self.health
        return self

    def display_health(self):
        print  "Name:" ,self.name 
        print "Health:" ,self.health
        return self

animal1=Animal("elephant",100)
animal1.walk().walk().walk().run().run().display_health()
print ''
#Animal, have it walk() three times, run() twice, and finally displayHealth() to confirm that the health attribute has changed.

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name,health=150)
        #self.name =name
        #self.health=150
        

    def pet(self):
        self.health += 5
        #print "Pet:" ,self.pet
        return self

dog=Dog("dog")
dog.walk().walk().walk().run().run().pet().display_health()
print''

# Dog walk() three times, run() twice, pet() once, and have it displayHealth().


class Dragon(Animal):
    def __init__(self,name):
        self.name =name
        self.health=170

    def fly(self):
        self.health -= 10
        return self    

    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"
#Dragon Class inherits everything from Animal

dragon=Dragon("fire")
dragon.display_health()
print''




animal2=Animal("elephant",100)
animal2.walk().run().display_health()


