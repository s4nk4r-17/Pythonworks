
class Shipping:

    def calculate_shipping_cost(self,weight):

        print(weight*5)

class ExpressShipping(Shipping):

    def calculate_shipping_cost(self, weight):
        
        print(weight*20)

class StandardShipping(Shipping):

    def calculate_shipping_cost(self, weight):
        
        print(weight*10)

std_instance=StandardShipping()

std_instance.calculate_shipping_cost(5)

exp_instance_2=ExpressShipping()

exp_instance_2.calculate_shipping_cost(5)

