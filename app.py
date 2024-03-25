import random
import sys
import time

# I know we said no packages, but I added a virtual environment anyways.
# To create a venv
# python -m venv (source name... i always just use venv)
# To activate the virtual env run:
# source/{the name you picked (venv)}/bin/activate
# You'll see a (venv) in front of your terminal, you're in!
# pip install -r requirements.txt will install all requirements (do this in
# your venv or they will go global) pip freeze > requirements.txt  (will write
# all imports you've added to the requirements)
# Will save the current config to the requirements
###############################################################################


def main(): 
    # Creates player instance (must happen before paths are defined)
    player = Player()
    player.set_name(str(delay_input("\nHello Adventurer! What shall I call you?\n")))




    ########################################################################
    ###############################  PATHS  ################################
    ########################################################################
    def game_paths():
        def start_game():
            # Player is getting released from jail, and the guard releasing you is
            # trying to be encouraging, but not doing a great job.
            delay_print(
                f"""

                {Colour.GREEN}JAILER{Colour.ENDC}
                The good news is, you're finally free. You've been locked up for so
                many years, must feel good! The bad news is, this probably isn't the
                world you remember. You don't have a penny to your name, and your
                possessions are worth as much as your wallet.

                {Colour.BLUE}{player.name}{Colour.ENDC}
                I have a wallet?!

                {Colour.GREEN}JAILER{Colour.ENDC}
                Your family felt bad for you though, and they've sent you some money.
                It should be enough to buy yourself lunch.
                """
            )
            player.add_money(50)

            delay_print(
                f"""
                {Colour.CYAN}NARRATOR{Colour.ENDC}
                And so, {player.name} leaves the prison that has been home for so long.
                Where should {player.name} go now?
                """
            )
            match show_choices(
                [
                    "Lunch sounds like a good idea",
                    "Might be a good idea to see the family!",
                    "I'm feeling lucky, I'm gonna hit the casino",
                ]
            ):
                case "0":
                    return paths['go_for_lunch']()
                case "1":  # TODO: make game routes
                    return paths['see_the_fam']()
                case "2":     # TODO: make game routes
                    print("go_to_the_rippers")


        def go_for_lunch():
            delay_print(
                f"""
            You see the allure of the Golden Arches ahead and know you
            can\'t resist. You are reaching for the door handle when it
            comes flying into your face. Blood streams down from your nose. 
            You take {player.print_damage(1, 'point of damage')}. The man walks right by
            you and gets into a black BMW.

            {player.name} is pissed. As he cleans the blood the best he can, a
            homeless man sitting against the wall near by coughs, and then
            speaks.

            {Colour.CYAN}HOMELESS MAN{Colour.ENDC}
            Nasty, dude! And I thought I had bad luck. But you know, luck is a
            powerful thing, and in times like this it helps to think of karma.
            Let me give you a gift.

            The homeless man gives you two dice, one has four sides, the other
            six.
                """
            )
            player.add_item(Dice(4))
            player.add_item(Dice(6))
            player.add_item(OxygenTank(), 42)
            player.print_items()
            dice = player.query_item(Dice(6))
            if dice:
                result = dice.roll_dice()
            match show_choices([
                "Jot down his license plate", 
                "Keep your head down and head in", # TODO: make game routes
                ]):
                case "0":
                    delay_print('You write down his license plate in your notebook') # TODO: need a notebook in inventory
                    return paths['go_in_restaurant']()
                case "1":
                    delay_print('So, you\'re a bit of a coward huh? Go on in then, wuss.\n')
                    return paths['go_in_restaurant']()


        def go_in_restaurant():
            delay_print('you go in the food house')
            return None # TODO: make game routes


        def see_the_fam():
            delay_print(f'''
            {Colour.CYAN}NARRATOR{Colour.ENDC}
            {player.name} heads home. It's been many years, but the county roads
            leading home still feel familiar. The feeling wasn't meant to last
            though. As {player.name} approached the house, it was all too apparent
            that the home was deserted.
            
            {Colour.GREEN}{player.name}{Colour.ENDC}
            Hey!
            Anyone around here or what?

            Ma?

            Pa??
            
            Tick? Where are ya?


            {Colour.CYAN}NARRATOR{Colour.ENDC}
            {player.name} hears the sound of a car engine coming up the road.
            Turning around to face the noise, he sees a black BMW. The driver
            pulls up close to the house and circles to park facing the way they
            came. A man wearing a suit emerges from the car. He pulls on each
            side of his mustache, sequentially. He regards {player.name}.
            
            {Colour.GREEN}Mysterious Man{Colour.ENDC}
            Well, I guess it's bout time you showed up, ain't it?
            

            ''')
            match show_choices([
                "Ignore the man", 
                "\"I was in prison. Where's my family? Where's my dog?\"", 
                ]):
                case "0":
                    player.print_items()
                    if (player.query_item(Dice(6)) or player.query_item(Dice(4))): #! Issue - always returns false
                        delay_print('so its a dice fight then')
                    else:
                        delay_print('The mysterious man walks up to you, and tosses you a collection of die ')
                        player.add_item(Dice(6))
                        player.print_items()
                case "1":
                    delay_print(f'''
            {Colour.CYAN}MYSTERIOUS MAN{Colour.ENDC}
            So you were. The apple never falls...

            Nevermind.
            Your family is gone. Well 'gone' is a bit vague isn't it?
            That is to say, I have no idea, but they are not here.
            I imagine you're glad to be home! But I'm afraid 'home' is
            a bit of a vague word as well! Strictly speaking, this cannot be a home to you, as it no longer belongs to either you, or
            any member of your family. It belongs to the Bank of
            Generosity.
            
            Now, at the BoG, we believe in living up to our name. I
            want to see this house back in your hands, so you and your
            family can get back to 'it', whatever that is.

            I'm going to give you a dice. A standard one, with six
            sides! If you can roll a six 3 times in a row, you can have
            the house back. That sounds fair doesn't it?

            If you can't, your only other recourse is to purchase it
            from the BoG for $3,200,000. You look a little surprised at
            that valuation. You see, 6 years ago your farm flooded
            after the river diverted in its direction. As such, the
            house is considered water-front now. Highly sought after!
            
            As discussed, here's your dice. Please kindly roll the dice
            3 times!
                    ''')
                    player.add_item(Dice(6))
                    player.print_items()
                    dice = player.query_item(Dice(6))
                    if(dice):
                        results = []
                        for i in range(3):
                            roll = dice.roll_dice()
                            results.append(roll)
                        print(results)
        

        return {
            'start_game': start_game,
            'go_for_lunch': go_for_lunch,
            'go_in_restaurant': go_in_restaurant,
            'see_the_fam': see_the_fam,
            }   
    ############################################################################
    #############################  END PATHS  ##################################
    ############################################################################

    # Initiate the paths to be used below... mostly i think they will just link to eachother above though. But now no hoisting issue
    paths = game_paths()


    ########################################################################
    ###############################  TEST VALUES  ##########################
    ########################################################################
    # To use the testing values, you will need to supply 2 additional command line args:
    # python3 app.py see_the_fam test  
    # this will run the game starting at see_the_fam and add anything in this test values area to the player inventory
    if len(sys.argv) >= 3 and sys.argv[2] =='test':
        player.add_item(Dice(6))
        print(player.query_item(Dice(4)))
        print(player.boolcheck_items(Dice))

        print(player.items)
        player.print_items()
        print(player.query_item(Dice(6)))

    ########################################################################
    ###############################  END TEST VALUES  ######################
    ########################################################################

    # Checks to see if any other starting point is supplied, and if its valid
    if len(sys.argv) >= 2:
        if sys.argv[1] in paths:
            paths[str(sys.argv[1])]()
        else:
            print_error('Developer - Command line args should be: python3 app.py [starting_path]? [test]? \n             Please check spelling of path.')
    else:
        paths['start_game']()

    return None #! This is the end of main()



class Item:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.quantity = 0


class Dice(Item):
    def __init__(self, sides:int) -> None:
        self.sides = sides
        self.name = f"{sides} - sided dice"
        self.description = "Are you feeling lucky, punk?"
        self.quantity = 0

    def roll_dice(self) -> int:
        result = random.randint(0, self.sides)
        print(f'''
            You rolled a {Colour.GREEN}{ result }{Colour.ENDC}!
              ''')
        return result


class OxygenTank(Item):
    def __init__(self ) -> None:
        self.name = "Oxygen Tank"
        self.description = "Take a breath, it'll be okay."
        self.quantity = 0


class Player:
    def __init__(self):
        self.name = ""
        self.money = 0
        self.hp = 100
        self.items = []

    def print_money(self, amount) -> str:
        return f"{Colour.YELLOW}${amount}{Colour.ENDC}"

    def print_damage(self, amount, str=""):
        return f"{Colour.RED}{amount} {str}{Colour.ENDC}"

    def set_name(self, newName):
        self.name = newName

    def add_money(self, qty):
        if isinstance(qty, int):
            self.money += qty
            delay_print(
                f"""
    {self.print_money(amount=qty)} added to your wallet!
    Current Balance: {self.print_money(amount=self.money)}
"""
            )
        else:
            delay_print("This ain't money...")

    def take_damage(self, amount):
        self.hp -= amount

    def print_items(self):
        print("\n|==========================================|")
        print(f"| {Colour.YELLOW}INVENTORY{Colour.ENDC}                                |")
        length = len("|------------------------------------------|")
        print("|==========================================|")
        self.items.sort(key=lambda item: item.name)
        for item in self.items:
            char_length = 1 + len(item.name) + len(str(item.quantity)) + 2
            modifier = length - char_length
            print(f"| {Colour.GREEN}{item.name}{Colour.ENDC}: {" "*(modifier-3)}{item.quantity} |")
        print("|==========================================|")

    def add_item(self, item:Item, quantity=1):
        item_names = []
        for i in self.items:
            item_names.append(i.name)
        if item.name in item_names:
            instance = [inventory_item for inventory_item in self.items if inventory_item.name == item.name][0]
            instance.quantity = instance.quantity + quantity
        else:
            item.quantity = quantity
            self.items.append(item)

    def query_item(self, item: Item): #! ISSUE: - see line 157. always returns false.
        item_names = []
        for item_loop in self.items: # This had to be changed from item to item_loop, or it caused a name collision below
            item_names.append(item_loop.name)
        print(f"item_names: {item_names}")
        print(item.name) # This would ping the item in the for loop above, python scopes weird...
                         # If you add only a 6 sided dice to inventory, and look for a 4 sided dice, item is the 6 sided dice at this point unless the above variable name is changed. Weird eh?
        if item.name in item_names: # With the name collision, this would only add dice to the last iterated over dice in the inventory
            instance = [inventory_item for inventory_item in self.items if inventory_item.name == item.name][0]
            return instance
        else: 
            # You don't have this item!
            return False
        
        # This one will return True if any instance of the class is in inventory
        # EXAMPLE: if player owns Dice(6) doing a bool_check(Dice) will still be True
        #          as there is a Dice Object in inventory. 
    def boolcheck_items(self, item_class:Item):
        for inventory_item in self.items:
            if isinstance(inventory_item, item_class):
                return True
        else: return False


class Colour:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    def demo_colours(self):
        print(
            f"""
Colour Demo
{Colour.HEADER}Header
{Colour.BLUE}Blue
{Colour.GREEN}Green
{Colour.CYAN}Cyan
{Colour.YELLOW}Yellow
{Colour.RED}Red{Colour.ENDC}
{Colour.BOLD}Bold{Colour.ENDC}
{Colour.UNDERLINE}Underlined
{Colour.ENDC}End Colour formatting
"""
        )


# Prints things slowly, the LOWER the speed the faster the typing
def delay_input(str, delay=1):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay / 1000)
    return input("")


# prints things with a dalay in micro seconds
def delay_print(str, delay=1):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay / 1000)


# Shows a list of options, and gives them a number for each. Player must type
# in a number to make a selection.
def show_choices(options):
    # Check if inputs are the right type
    if not isinstance(options, list):
        print_error("Developer! Make sure your options are a list of strings!")
        return

    print("\n")  # Controls format of options so they reset their indent
    for index, item in enumerate(options):
        # Check to make sure option is a string
        if not (isinstance(item, str)):
            print_error("Developer! the option must be a string.")
            return
        print(f"{Colour.BLUE}[{index}]{Colour.ENDC} - {item}")
    answer = None
    while (
        not isinstance(answer, int) or not (answer >= 0) or not (answer < len(options))
    ):
        answer = input()
        if not (answer.isdigit()):
            print_error("Not a valid answer, please enter a digit for your selection")
        if answer.isdigit():
            answer = int(answer)
            if not (answer >= 0):
                print_error("Please enter a number greater than 0!")
            if not (answer < len(options)):
                print_error("Please select a number within the range of options!")
    return str(answer)


# Helper function for displaying errors
def print_error(error):
    print(f"\n{Colour.RED}{error}{Colour.ENDC}")

# End the program with the main function call
main()
