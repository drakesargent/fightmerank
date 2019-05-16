import random

NUM_WEEKS = 26


class player:

    def __init__(self, name, rank):
        self.name = 'a'+str(name)
        self.rank = rank
        self.wins = 0
        self.matches = 0
        self.countdown = 0
        self.willFight = True

    def fightElegible(self):
        return self.countdown <= 0

    def setRank(self, newRank):
        self.rank = newRank

    def acceptChallenge(self, challenger):
        return (challenger.rank-self.rank) <= 5

    def setCountdown(self):
        self.countdown = 4

    def incrWin(self):
        self.wins += 1

    def incrMatches(self):
        self.matches += 1

    def fightChance(self):
        if self.rank > 51:
            chance = 75
        if self.rank > 26:
            chance = 50
        if self.rank > 11:
            chance = 25
        chance = 20
        rand = random.randint(1, 101)
        self.willFight = rand <= chance

    def win(self, newRank):
        self.incrWin()
        self.incrMatches()
        self.setCountdown()
        self.rank = newRank

    def lose(self, newRank):
        self.incrMatches()
        self.setCountdown()
        self.rank = newRank


def fight(challenger, defender):
    if challenger.fightElegible() and defender.fightElegible():
        if defender.acceptChallenge(challenger):
            winningRank = defender.rank
            losingRank = challenger.rank
            challengeWin = random.randint(1, 100)
            if challengeWin < 60:
                defender.win(winningRank)
                challenger.lose(losingRank)
            else:
                defender.lose(losingRank)
                challenger.win(winningRank)
            return True
    return False


def runHeat(contenders):
    fights = 0
    passes = 0
    fightAttempts = 0
    for challenger in contenders:
        challenger.fightChance()
    for challenger in contenders:
        if challenger.willFight:
            fightAttempts += 1
            willChallenge = random.randint(1, 6)
            challengeRank = challenger.rank - willChallenge
            if challengeRank < 1:
                challengeRank = 1
            if fight(challenger, contenders[challengeRank-1]):
                fights += 1
            else:
                passes += 1
    print("In this heat {} fights attempted {} fights, and {} passes".format(fightAttempts, fights, passes))

fighters = []

for fighter in range(100):
    fighters.append(player(fighter+100, fighter+1))

print("{} fighters created".format(len(fighters)))

for heats in range(NUM_WEEKS):
    for fighter in fighters:
        fighter.countdown -= 1
    runHeat(fighters)
    fighters = sorted()
