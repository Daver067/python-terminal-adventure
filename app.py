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
    # Use variables here or go right into objects (dicts in python)? Or a
    # Class? You Pick, delete the rest ;)

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

        def demoColours():
            print(
                f"""
colour Demo
{colour.HEADER}Header{colour.ENDC}
{colour.BLUE}Blue{colour.ENDC}
{colour.GREEN}Green{colour.ENDC}
{colour.CYAN}Cyan{colour.ENDC}
{colour.YELLOW}Yellow{colour.ENDC}
{colour.RED}Red{colour.ENDC}
{colour.BOLD}Bold{colour.ENDC}
{colour.UNDERLINE}Underlined{colour.ENDC}
{colour.ENDC}End colour formatting
"""
            )

    class PlayerClass:
        def __init__(self):
            self.name = ""
            self.money = 0

        def changeName(self, newName):
            self.name = newName

        def addMoney(self, amount):
            if isinstance(amount, int):
                self.money += amount
                print(
                    f"{colour.YELLOW}{amount}${colour.ENDC} added to your wallet! \nCurrent Balance: {colour.YELLOW}{self.money}${colour.ENDC}"
                )
            else:
                print("This ain't money...")

    # Creates player instance
    player = PlayerClass()
    player.changeName(enterName())

    # Player is getting released from jail, and the guard releasing you is
    # trying to be encouraging, but not doing a great job.
    print(
        """
JAILER
The good news is, you're finally free. You've been locked up for so
many years, must feel good! The bad news is, this probably isn't the
world you remember. You don't have a penny to your name, and your
possessions are worth as much as your wallet.
    """
    )

    print(
        """
JAILER 
Your family felt bad for you though, and they've sent you some money. It should
be enough to buy yourself lunch.
          """
    )

    player.addMoney(40)

    colour.demoColours()

    return None


# A function which will provide the name for the main func.
def enterName():
    name = str(input("\nHello Adventurer! What shall I call you?\n"))
    print(f"\nWell it's a pleasure to meet you, {name}!")
    return name


# End the program with the main function call
main()
