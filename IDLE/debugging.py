#Sylvie Edelstein
#11/4/22
#debugging.py
#This program debus several coding examples

def example1(): 

#There are at least 3 errors in the code below: 2 can probably be found
#by simply "eyeing" the code, the last one you may need to run the code to find it.

    greeting = input("Hello, possible pirate! What's the password?")
    #add end quotation after password
    if greeting in ("Arrr!"):
        #make bracket parentheses
        print("Go away, pirate.")
    else:
        print("Greetings, hater of pirates!")
    #made elif else, added colon, and indented


def example2(): 

#At least 8 errors,
#First line of code (after comments) has 3 errors alone
#Some errors are repeated more than once.


# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

    year = int(input("Greetings! What is your year of origin?"))
    #remove extra equals, changed int.input to int(input, changed end quotation to "

    if year < 1900:
        print ("Woah, that's the past!")
        #changed ' to ", removed equals, added colon, change <= to <
    elif year >= 1900 and year <= 2020:
        #change && to and
        #changed to <= and =>
        print("That's totally the present!")
    else:
        print("Far out, that's the future!!")
        #changed to else, removed extra space

def example3(): 
	
# Calculating Grades:

#At least 9 errors. Most are typos, but a few may take running the code and stopping at various spots to examine values.

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 34
# Grade: F
# Student iis failing.

    exam_one = int(input("Input exam grade one: "))

    exam_two = int(input("Input exam grade two: "))

    #add int

    exam_three = int(input("Input exam grade three: "))

    #change str to int, 3 to three

    grades = [exam_one, exam_two, exam_three]
    #change spaces to ,
    sum = 0
    for grade in grades:
    #add s
      sum = sum + grade

    avg = sum / len(grades)
    #spelled grades wrong

    if avg >= 90:
        letter_grade = "A"
    elif avg >= 80 and avg < 90:
    #add colon after 90
        letter_grade = "B"
    elif avg > 69 and avg < 80:
        letter_grade = "C"
        #change ' to " after C
    elif avg <= 69 and avg >= 60:
    #change 60 to 65
        letter_grade = "D"
    else:
        letter_grade = "F"
    #change elif to else
    print("Exam: " + str(grades))
    #make grade grades

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

    if letter_grade == "F":
    #should _ not -, == not is
        print("Student is failing.")
    else:
        print("Student is passing.")
        #missing parentheses around print

example1()
example2()
example3()
