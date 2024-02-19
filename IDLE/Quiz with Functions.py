#Sylvie Edelstein
#10/21/22
#quiz.py
#This program is a quiz that calculates the number of correct answers the user has

def askQuestion(question, answer):
    ans = input(question).lower()
    if ans == answer:
        print("Correct!")
        return True
    else:
        print("Sorry. That is not correct.")
        return False

def FinalScore(totalscore):
    if totalscore > 4:
        print("Congratulations you are a certified G-E-N-I-U-S!")
    elif totalscore == 3:
        print("You did pretty well. You aren't perfect, but not everyone can be me!")
    elif totalscore == 4:
        print("You did pretty well. You aren't perfect, but not everyone can be me!")
    elif totalscore < 3:
        print("I mean that was just tragic. I didn't know that was even possible.")

def main():
    print ("This is a fun quiz!")
    score = 0
    question_list=["How many politicians are in the senate? ","What color is featured in the center of the Japanese flag? ","Who composed 32 Sonatas in their lifetime? ","How many inches are in a foot? ","What theory explains why jumping off a building would cause you to hit the ground? "]
    answer_list= ["100", "red", "beethoven", "12", "gravity"]

    for i in range (len(question_list)):
        if askQuestion(question_list[i], answer_list[i]) == True:
            score = score + 1

    (FinalScore(score))
            

main()





















    
