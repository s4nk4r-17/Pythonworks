

class SuperHero:

    name:str
    suit:str

    def __init__(self,name,suit):
        self.name=name
        self.suit=suit

    def __str__(self):
        return self.name

class SpiderMan(SuperHero):

    def __init__(self, name, suit):

        super().__init__(name,suit)

    def superpowers(self):

        print("spider sence","web shooting")

spiderman_instance=SpiderMan("spiderman","spidersuit")

print(spiderman_instance)

spiderman_instance.superpowers()

class MinnalMurali(SuperHero):

    def __init__(self, name, suit):

        super().__init__(name, suit)

    def superpowers(self):

        print("running","jumping","reflex")


minnalmurali_instance=MinnalMurali("Minnalmurali","M-M suit")

print(minnalmurali_instance)

minnalmurali_instance.superpowers()