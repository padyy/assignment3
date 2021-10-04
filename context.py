'''
This is the module for context of the strategy Pattern. In it, there is the class for the product,
which in our case is the T-shirt. Context can use the desired strategy.
'''
from strategy import PaymentCredit,PaymentBank,PaymentCash

class T_Shirt_payment: #This is the context class for the strategy Pattern

    color = ['red','orange','yellow','green','blue','indigo','violet'] #In this line and above  are the lists with the accepted inputs for color,size,fabric and payment
    size = ['xs','s','m','l','xl','xxl','xxxl']
    fabric = ['wool','cotton','polyester','rayon','linen','cashmere','silk']
    payment = ['credit','bank','cash']

    #dictionaries with the price of each color,size and fabric
    color_prices={'red': 7 , 'orange': 5.70 , 'yellow': 5.60, 'green': 5.90 , 'blue': 6.20 , 'indigo': 7.30,'violet': 6.60 }
    size_prices={'xs': 5, 's': 5.5, 'm': 6.5, 'l': 7.2, 'xl': 7.8, 'xxl': 8, 'xxxl':8.5}
    fabric_prices={'wool' : 10, 'cotton': 13, 'polyester': 11.5, 'rayon':14, 'linen': 12, 'cashmere':16, 'silk':15.5}
    
    def __init__(self, t_color, t_size, t_fabric, t_payment, strategy ) : #init of T_shirt_payment
        
        self._t_color = t_color
        self._t_size = t_size
        self._t_fabric = t_fabric
        self._t_payment = t_payment
        self._strategy = strategy

    #Properties and setters for getting the protected attributes
    @property
    def t_color(self):
        return self._t_color

    @property
    def t_size(self):
        return self._t_size

    @property
    def t_fabric(self):
        return self._t_fabric

    @property
    def t_payment(self):
        return self._t_payment

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter #setter for strategy so it can be redefined outside the class
    def strategy(self,value):
        self._strategy = value

        
    def executeStrategy(self): #The function that executes the chosen strategy
        return self._strategy.dopayment(self)

    def totalCost(self): # Function that culculates the total cost of each t-shirt object
        total_cost = self.color_prices[self.t_color] + self.size_prices[self.t_size] + self.fabric_prices[self.t_fabric]
        return total_cost
