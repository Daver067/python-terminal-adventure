# I know we said no packages, but I added a virtual environment anyways. 
# To create a venv
# python -m venv (source name... i always just use venv)
# To activate the virtual env run:
# source/{the name you picked (venv)}/bin/activate
# You'll see a (venv) in front of your terminal, youre in!
# pip install -r requirements.txt will install all requirements (do this in your venv or they will go global) 
# pip freeze > requirements.txt  (will write all imports you've added to the requirements)
# Will save the current config to the requirements
#####################################################################################


def main():
    # Use variabless here or go right into objects (dicts in python)? Or a Class? You Pick, delete the rest ;)

    # Variable Option
    name = getName()
    print(name)

    # Dict option
    player_dict = {
        'name': name
    }
    print(player_dict["name"]) # Note python doesn't do dot notation... PlayerDict.name is a no bueno
    # print(PlayerDict.name) #This will be a syntax error

    # Class option (I haven't got much into python classes myself)
    class PlayerClass:
        def __init__(self, name):
            self.name = name
        def changeName(self, newName):
            self.name = newName
    player_class = PlayerClass(name)
    print(player_class.name)
    player_class.changeName('Chizzartley')
    print(player_class.name)

    return None

# A function which will provide the name for the main func.
def getName():
    name = str(input('\nHello Adventurer! What shall I call you?\n'))   
    print(f'\nWell it\'s a pleasure to meet you, {name}!\n')
    return name

# End the program with the main function call
main()