import time
import sys
# I know we said no packages, but I added a virtual environment anyways.
# To create a venv
# python -m venv (source name... i always just use venv)
# To activate the virtual env run:
# source/{the name you picked (venv)}/bin/activate
# You'll see a (venv) in front of your terminal, youre in!
# pip install -r requirements.txt will install all requirements (do this in
# your venv or they will go global) pip freeze > requirements.txt  (will write
# all imports you've added to the requirements)
# Will save the current config to the requirements
###############################################################################


def main():
    class colour: 
        HEADER = "\033[95m"
        BLUE = "\033[94m"
        CYAN = "\033[96m"
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        RED = "\033[91m"
        ENDC = "\033[0m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"

        def money(amount):
            return (f"{colour.YELLOW}${amount}{colour.ENDC}")

        def demoColours():
            print(
                f"""
colour Demo
{colour.HEADER}Header
{colour.BLUE}Blue
{colour.GREEN}Green
{colour.CYAN}Cyan
{colour.YELLOW}Yellow
{colour.RED}Red{colour.ENDC}
{colour.BOLD}Bold{colour.ENDC}
{colour.UNDERLINE}Underlined
{colour.ENDC}End colour formatting
"""
            )

    class PlayerClass:
        def __init__(self):
            self.name = ""
            self.money = 0

        def setName(self, newName):
            self.name = newName

        def addMoney(self, amount):
            if isinstance(amount, int):
                self.money += amount
                delay_print(
                    f"{colour.money(40)} added to your wallet! \nCurrent Balance: {colour.money(self.money)}"
                )
            else:
                delay_print("This ain't money...")

    # Creates player instance
    player = PlayerClass()
    player.setName(enterName())
    # Player is getting released from jail, and the guard releasing you is
    # trying to be encouraging, but not doing a great job.
    delay_print(
        f"""

{colour.GREEN}JAILER{colour.ENDC}
        The good news is, you're finally free. You've been locked up for so
        many years, must feel good! The bad news is, this probably isn't the
        world you remember. You don't have a penny to your name, and your
        possessions are worth as much as your wallet.

{colour.BLUE}{player.name}{colour.ENDC}
        I have a wallet?!

{colour.GREEN}JAILER{colour.ENDC}
        Your family felt bad for you though, and they've sent you some money. It should
        be enough to buy yourself lunch.
          """
    )
    player.addMoney(40)
    return None


# A function which will provide the name for the main func.
def enterName():
    name = str(input("\nHello Adventurer! What shall I call you?\n")) #TODO can we make this delay_print? We will probably have to make a delay_input... I couldn't make it work
    delay_print(f"\nWell it's a pleasure to meet you, {name}!")
    return name

# Prints things slowly, the LOWER the speed the faster the typing
def delay_print(str, speed = 4):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed/100)


# End the program with the main function call
main()
