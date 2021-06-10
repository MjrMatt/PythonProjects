import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        #brains = 0
        while diceRollResults is not None:
            #brains += diceRollResults['brains']
            if random.choice([True, False]):
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class secondBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains<2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
class thirdBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if shotgun<2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class forthBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        times = random.randint(0,3)
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if shotgun<2 and times>0:
                diceRollResults = zombiedice.roll()
                times-=1
            else:
                break

class fifthBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        brains = 0
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if brains > shotgun:
                diceRollResults = zombiedice.roll()
            else:
                print(f"Stoped with {brains} brains and {shotgun} shotguns!")
                break

class sixthBot:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        choice = random.randint(1,200)
        diceRollResults = zombiedice.roll()
        shotgun = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if shotgun<2:
                diceRollResults = zombiedice.roll()
            elif choice==1:
                diceRollResults = zombiedice.roll()
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    #MyZombie(name='MB - randomly decide after 1st'),
    #secondBot(name='MB - Stop on 2 brains'),
    #thirdBot(name='MB - Stop on 2 shotguns'),
    #forthBot(name='MB - inicialy decides roll quantity, but stop on 2 shotguns'),
    #fifthBot(name='MB - stops when more shotguns than brains'),
    sixthBot(name='1/200 times continue playing after 2 shotguns'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
