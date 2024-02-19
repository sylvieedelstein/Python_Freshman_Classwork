#Sylvie Edelstein
#Intro Programming
#December 6, 2022
#Dice Game

import random
class DiceGame:

    def __init__(self, num_dice):
        self.num_dice = num_dice
        self.score = 0

    def rollDice(self):
        score = 0
        for i in range(self.num_dice):
            roll = random.randint(1,6)
            print("You rolled a", roll, "on roll", i+1)
            score = score + roll
        return score
    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

def main():
    player1 = DiceGame(2)
    player2 = DiceGame(2)

    #Start the game
    
    # call the rollDice() for player 1. Print out the returned score.
    print("Player 1 rolls first:")
    score1 = player1.rollDice()
    player1.set_score(score1)
    print("Player 1 rolled a:",player1.get_score())

    #Repeat the same for Player 2
    print("Player 2 rolls next:")
    score2 = player2.rollDice()
    player2.set_score(score2)
    print("Player 2 rolled a:",player2.get_score())

    #Check for winner:
    #if player 1's score is greater than player 2's score:
    if player1.get_score() > player2.get_score():
        print("Player 1 wins this round")

    #else if player 2's score is greater than player 1's score:
    elif player2.get_score() > player1.get_score():
        print("Player 2 wins this round")

    #else a tie occurred
    else:
        print("This round was a tie.")

main()



