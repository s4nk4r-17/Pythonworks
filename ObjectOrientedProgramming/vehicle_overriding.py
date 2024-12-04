
class Parent:

    def vehicles(self):

        self.bikes=["passionpro","activa"]

        return self.bikes

class Child(Parent):

    def vehicles(self):
        
        self.bikes=super().vehicles()    #["passionpro","activa"]

        self.bikes.append("Hunter")

        return self.bikes

child_instance=Child()

print(child_instance.vehicles())