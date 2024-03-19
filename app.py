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
                    print("see_the_fam")
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
        

        return {
            'start_game': start_game,
            'go_for_lunch': go_for_lunch,
            'go_in_restaurant': go_in_restaurant,
            }   
    ############################################################################
    #############################  END PATHS  ##################################
    ############################################################################

    # Initiate the paths to be used below... mostly i think they will just link to eachother above though. But now no hoisting issue
    paths = game_paths()
    paths['start_game']()

    return None #! This is the end of main()



class Item:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.quantity = 0


class Dice(Item):
    def __init__(self, sides) -> None:
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
        for item in self.items:
            char_length = 1 + len(item.name) + len(str(item.quantity)) + 2
            modifier = length - char_length
            print(f"| {Colour.GREEN}{item.name}{Colour.ENDC}: {" "*(modifier-3)}{item.quantity} |")
        print("|==========================================|")

    def add_item(self, item: Item, quantity=1):
        if item in self.items:
            instance = [item for item in self.items if item.name == item.name][0]
            instance.quantity = instance.quantity + quantity
        else:
            item.quantity = quantity
            self.items.append(item)

    def query_item(self, item):
        if item in self.items:
            instance = [item for item in self.items if item.name == item.name][0]
            return instance
        else: 
            # You don't have this item!
            return False


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


# Weird, I don't remember having to specifically place funcs above their
# invocation in python.... but putting it below the match case didn't work

# Chartley:
# So, I moved the lunch function out of here. From what I can gather, there is no
# hoisting in python, like there is in Javascript. The main() function being at
# the bottom is a convention because this is the python workaround for the lack
# of hoisting. So, I propose that we keep any reusable functions and classes down
# below, and any narrative one-time-use functions within main(). So while we work
#     within main(), we first declare a function, then call it.
#
# I also did some other general refactoring so that my linter stopped yelling at
# me haha. You'll figure it out.

#! Dave:
#! my issue with declaring a func and then using it makes the script basically read backwards,
#! when a game like this will need to run unilaterally. Think goosebumps - turn to page 72. now turn to page 13. now 73.
#! think how it is now, first choice results in choices ABC, which all have to be declared above the initial choice
#! Then each ABC will have a1 b1 c1 a2 b2 c2...etc which will in turn have to be above... but if c3 links back to b1's
#! function/storyline you will get an error because c3 function declaration is before b1. 
#! We need either:
    #! 1: scope all story routes in global
    #! 2: scope all story routes in an inner function
    #! 3: break a rule and use a separate helper module
#! just thinking about this has already put me into my 30 minute limit haha, I'm going to pull off #2 before i commit



# End the program with the main function call
main()
