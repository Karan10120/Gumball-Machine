“””
Checks if the input string is float number
@param str - string that contains the potential float
@return returns true if the input string is a float, return false otherwise
“””
def isfloat(str):
    try: 
        float(str)
    except ValueError: 
        return False
    return True

“””
Gumball Machine Class creates a Gumball Machine Objects that 
can take in coins and dispense gumballs
“””
class GumballMachine:
    deposit = 0

    “””
    Prints out the list of  accepted commands to console
    “””
    def print_commands(self):
        print('''Error: Invalid Command
Commands: insert <coin>, change, pull <lever color>, finish''')


    “””
    Prints out the list of valid coin commands to console
    “””
    def print_coin_options(self):
        print('''Error: Invalid Coin
Valid Coins: nickel, dime, quarter''')
      
    “””
    Prints out the accepted lever colors to console
    “””  
    def print_lever_colors(self):
        print('''Error: Invalid Lever Color 
Lever Valid Colors: red, yellow''')  
    
    “””
    Prints out the current deposit amount to console
    “””
    def print_amount_left(self) : 
          print("Current Amount: $%1.2f" % (self.deposit))      
    
    “””
    Takes in the type of coin inserted and adds the value of 
    the coin to the current deposit
    @param coin - str that identifies the inserted coin
    “””
    def insert_coin(self, coin):
        coin = str.upper(coin)
        if coin == "NICKEL":
            self.deposit = self.deposit + 0.05
        elif coin == "DIME":
            self.deposit = self.deposit + 0.10
        elif coin == "QUARTER":
            self.deposit = self.deposit + 0.25
        else:
            if isfloat(coin):
                print('''Error: Values not Accepted 
        Enter Coin Name
        Valid Coins: nickel, dime, quarter''')
            else:
                self.print_coin_options()
            return
        self.print_amount_left()
    
    “””
    Pulls the red lever verifying that the deposit is atleast 5 
    cents. If it is not at least five cents prints an error      
    message
    “””
    def red_lever(self):
        if self.deposit < 0.05:
            print("Error: Costs $0.05")
            return
        self.deposit = self.deposit - 0.05
        print("Red gumball dispensed")
        self.print_amount_left()
        return 1


    “””
    Pulls the yellow lever verifying that the deposit is at
    least 10 cents. If it is not at least five cents prints an  
    error message
    “””
    def yellow_lever(self):
        if self.deposit < 0.1:
            print("Insufficient Funds: Costs $0.10")
            return
        self.deposit = self.deposit - 0.1
        print("Yellow gumball dispensed")
        self.print_amount_left()
    
    “””
    Parse input string to determine which lever is supposed to 
    be pulled than calls the appropriate function associated
    with said lever color
    @param color - string that contains the pull lever color
    “””   
    def lever_pull(self, color):
        color = str.upper(color)
        if color == "YELLOW":
            self.yellow_lever()
        elif color == "RED":
            self.red_lever()
        else:
            self.print_lever_colors()
    
    “””
    Check the amount in the deposits. Prints out that amount 
    as change then sets deposit to 0.
    “””        
    def get_change(self) : 
        change = self.deposit
        self.deposit = 0
        print("Change: $%1.2f" % (change))

    “””
    Parses string to determine which command was imputed. Then 
    calls appropriate function associated with said command
    @param action -string that contains the user inputted action
    “”” 
    def determine_action(self, action):
        args = str.split(action)
        
        command = str.upper(args[0])
        if command == "INSERT":
            self.insert_coin(args[1])
        elif command == "CHANGE":
            self.get_change()
        elif command == "PULL":
            self.lever_pull(args[1])
        elif command == "FINISH":
            return False
        else:
            self.print_commands()
        return True
    
    “””
    Initializes the gumball machine object and handles command 
    inputs from user
    “””
    def __init__(self):
        self.print_amount_left()
        while(True):
            if not self.determine_action(input()):
                break
            
gumball = GumballMachine()


