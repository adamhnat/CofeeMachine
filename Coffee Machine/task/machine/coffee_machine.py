class MyCoffeeMachine:
    CMD_WAIT =1
    CMD_EXIT =0
    ESPRESSO = {
        "water": 250,
        "milk": 0,
        "beans": 16,
        "cost": 4
    }

    LATTE = {
        "water": 350,
        "milk": 75,
        "beans": 20,
        "cost": 7
    }

    CAPPUCINO = {
        "water": 200,
        "milk": 100,
        "beans": 12,
        "cost": 6
    }

    coffee_map = {
        1:ESPRESSO,
        2:LATTE,
        3:CAPPUCINO
    }

    def __init__(self):
        self.money_lvl = 550
        self.water_lvl = 400
        self.milk_lvl = 540
        self.beans_lvl = 120
        self.cups_lvl = 9
        self.state='main'
        self.cmd()

    def buy(self,_type=None):
        c_cofee = self.coffee_map.get(int(_type))
        if self.validate(c_cofee) != 0:
            self.make_cofee(c_cofee)

    def validate(self, _type):
        if self.milk_lvl - _type['milk'] < 0:
            print("Sorry, not enough milk!")
            return 0
        if self.beans_lvl - _type['beans'] < 0:
            print("Sorry, not enough beans!")
            return 0
        if self.water_lvl - _type['water'] < 0:
            print("Sorry, not enough water!")
            return 0
        print("I have enough resources, making you a coffee!")

    def make_cofee(self, c_cofee):
        self.money_lvl += c_cofee['cost']
        self.milk_lvl -= c_cofee['milk']
        self.beans_lvl -= c_cofee['beans']
        self.water_lvl -= c_cofee['water']
        self.cups_lvl -= 1

    def fill(self,waterq,milkq,beansq,cupsq):
        self.water_lvl += int(waterq)
        self.milk_lvl += int(milkq)
        self.beans_lvl += int(beansq)
        self.cups_lvl += int(cupsq)

    def take(self):
        print("I gave you $", self.money_lvl)
        self.money_lvl = 0

    def status(self):
        print("The coffee machine has:\n",
            self.water_lvl , " of water\n",
            self.milk_lvl , " of milk\n",
            self.beans_lvl , " of cofee beans\n",
            self.cups_lvl , " of disposable cups\n",
            "$", self.money_lvl , " of money" )

    def cmd(self,command=None):
        prompts= {
            'main': "Write action (buy, fill, take, remaining, exit):",
            'buy': "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:",
            'fill1': "Write how many ml of water do you want to add:",
            'fill2': "Write how many ml of milk do you want to add:",
            'fill3': "Write how many grams of coffee beans do you want to add:",
            'fill4': "Write how many disposable cups of coffee do you want to add:"
        }

        if (command is None and self.state in prompts.keys()):
            print(prompts[self.state])
            return self.CMD_WAIT

        if (self.state == 'main' and command is not None):
            if command == 'buy':
                self.state='buy'
            elif command == 'fill':
                self.state = 'fill1'
            elif command == 'take':
                self.state = 'take'
            elif command == 'remaining':
                self.state = 'remaining'
            elif command == 'exit':
                return self.CMD_EXIT
            command=None

        if self.state == 'buy' and command is not None:
            if command == 'back':
                pass
            else:
                self.buy(int(command))
            self.state='main'
            command=None

        if self.state == 'fill1' and command is not None:
            self.fill(command,0,0,0)
            self.state='fill2'
            command=None
        if self.state == 'fill2' and command is not None:
            self.fill(0,command,0,0)
            self.state='fill3'
            command=None
        if self.state == 'fill3' and command is not None:
            self.fill(0,0,command,0)
            self.state='fill4'
            command=None
        if self.state == 'fill4' and command is not None:
            self.fill(0,0,0,command)
            self.state='main'
            command=None

        if self.state == 'take':
            self.take()
            self.state='main'
            command=None

        if self.state == 'remaining':
            self.status()
            self.state='main'
            command=None

        self.cmd()
        return self.CMD_WAIT

cm = MyCoffeeMachine()
ret = -1
while ret != 0:
    ret = cm.cmd(input())


