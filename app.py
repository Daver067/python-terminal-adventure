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

    class PlayerClass:
        def __init__(self):
            self.name = ""
            self.money = 0
            self.hp = 100

        def set_name(self, newName):
            self.name = newName

        def add_money(self, amount):
            if isinstance(amount, int):
                self.money += amount
                delay_print(
                    f"""
        {colour.money(amount)} added to your wallet!
        Current Balance: {colour.money(self.money)}
    """
                )
            else:
                delay_print("This ain't money...")

        def take_damage(self, amount):
            self.hp -= amount



    # Creates player instance
    player = PlayerClass()
    player.set_name(enterName())
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
        Your family felt bad for you though, and they've sent you some money.
        It should be enough to buy yourself lunch.
        """
         )
    player.add_money(50)

    delay_print(
        f"""
        {colour.CYAN}NARRATOR{colour.ENDC}
        And so, {player.name} leaves the prison that has been home for so long. 
        Where should {player.name} go now?
        """
    )

    match showChoices(
        [
            "Lunch sounds like a good idea",
            "Might be a good idea to see the family!",
            "I'm feeling lucky, I'm gonna hit the casino",
        ]
    ):
        case "0":
            go_for_lunch()
        case "1":
            print('see the fam')
        case "2":
            print('go for lunch')





    return None



# A function which will provide the name for the main func.
def enterName():
    name = str(
        delay_input("\nHello Adventurer! What shall I call you?\n")
    )  # TODO can we make this delay_print? We will probably have to make a delay_input... I couldn't make it work
    delay_print(f"\nWell it's a pleasure to meet you, {name}!")
    return name

def delay_input(str, delay=1):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay / 1000)
    input('')

# Prints things slowly, the LOWER the speed the faster the typing
def delay_print(str, delay=1):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay / 1000)


# Shows a list of options, and gives them a number for each. Player must type in a number to make a selection.
def showChoices(options):
    # Check if inputs are the right type
    if not isinstance(options, list):
        showError("Developer! Make sure your options are a list of strings!")
        return

    print("\n")  # Controls format of options so they reset their indent
    for index, item in enumerate(options):
        # Check to make sure option is a string
        if not (isinstance(item, str)):
            showError("Developer! the option must be a string.")
            return
        print(f"{colour.BLUE}[{index}]{colour.ENDC} - {item}")
    answer = None
    while (
        not isinstance(answer, int) or not (answer >= 0) or not (answer < len(options))
    ):
        answer = input()
        if not (answer.isdigit()):
            showError("Not a valid answer, please enter a digit for your selection")
        if answer.isdigit():
            answer = int(answer)
            if not (answer >= 0):
                showError("Please enter a number greater than 0!")
            if not (answer < len(options)):
                showError("Please select a number within the range of options!")
    return str(answer)


# Helper function for displaying errors
def showError(error):
    print(f"\n{colour.RED}{error}{colour.ENDC}")


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
        return f"{colour.YELLOW}${amount}{colour.ENDC}"
    def damage(amount, str=""):
        return f"{colour.RED}{amount} {str}{colour.ENDC}"

    def demoColours(self):
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

# Weird, I don't remember having to specifically place funcs above their invocation in python.... but putting it below the match case didn't work
def go_for_lunch():
    delay_print(f'''
                You see the allure of the Golden Arches ahead and know you can\'t resist. You are reaching
                for the door handle when it comes flying into your face. Blood streams down from your nose. 
                You take {colour.damage(1, 'point of damage')}. The man walks right by you and gets into a black BMW. ''')
    
    showChoices(
        [
            "Jot down his license plate",
            "Keep your head down and head in"
        ]
        )
    return None

# End the program with the main function call
main()




