# slots 

MAX_LINE = 5
MAX_BET = 100
MIN_BET = 1

REELS = 5 
VISIBLE_TABS = 3  

symbol_count ={
    "Blank": 60,
    "Cherries": 50,
    "Bars": 40,
    "Double Bars": 30,
    "Tripple Bars": 20,
    "Sevens": 10 
}

def get_slot_spin(reels, tabs, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)


class Gambler:
    def __init__(self, balance):
        self.balance = balance
    
    def updateBalance(self, increase, amount):
        if increase:
            self.balance += amount
        else:
            self.balance -= amount

    def deposit(self):
        
        while True:
            amount = input("How much would you like to deposit? \n $ ")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    break
                else:
                    print("You broker than broke. Enter a value greater than 0.")
            else:
                print("You stupid. Enter a positive number.")

        return amount


if __name__ == "__main__":
    
    def main():
        
        print("Let's Play slots!! Gambling is fun and totally really cool and any financial advisor would recommend!")
        print("Source: Trust me bro")
        
        homeless = Gambler(0)
        balance = homeless.deposit()
        homeless.updateBalance(True, balance)

        print(f"Homeless's Balance: $ {balance}")
    
    main()

