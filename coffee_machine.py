class Drink:
    cups_req = 1
    def __init__(self, cost, water_req, milk_req, beans_req):
        self.cost = cost
        self.water_req = water_req
        self.milk_req = milk_req
        self.beans_req = beans_req
        
class CoffeeMachine:
    def __init__(self, money, water, milk, beans, cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
                
    def buy(self):  
        def make(drink):          
            def not_enough(ingredient):
                print("Sorry, not enough {}!\n".format(ingredient))
                
            if self.water < drink.water_req:
                not_enough("water")
            elif self.milk < drink.milk_req:
                not_enough("milk")
            elif self.beans < drink.beans_req:
                not_enough("coffee beans")
            elif self.cups < drink.cups_req:
                not_enough("disposable cups")
            else:
                print("I have enough resources, making you a coffee!\n")
                self.money += drink.cost
                self.water -= drink.water_req
                self.milk -= drink.milk_req
                self.beans -= drink.beans_req
                self.cups -= drink.cups_req
        
        order = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")
        if order == "1":
            make(espresso)
        elif order == "2":
            make(latte)
        elif order == "3":
            make(cappuccino)
        elif order == "back":
            self.menu()
             
    def fill(self):
        def how_many(unit, ingredient):
            return int(input('Write how many {} of {} do you want to add:\n'.format(unit, ingredient)))
        
        print('\n')
        self.water += how_many("ml", "water")
        self.milk += how_many("ml", "milk")        
        self.beans += how_many("grams", "coffee beans")
        self.cups += how_many("disposable cups", "coffee")
        print('\n')
        
    def take(self):
        print(f'I gave you ${self.money}\n')
        self.money = 0
        
    def remaining(self):
        print(f'\nThe coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money\n')
    
    def menu(self):
        import sys
        while True:
            action = input("Write action (buy, fill, take, remaining, exit): \n")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                sys.exit()
                  
espresso = Drink(4, 250, 0, 16)
latte = Drink(7, 350, 75, 20)
cappuccino = Drink(6, 200, 100, 12)

customer = CoffeeMachine(550, 400, 540, 120, 9)
customer.menu()