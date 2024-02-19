#Sylvie Edelstein
#9/30/22
#This project plays around with "spam" and "ni!"

def spam():
    s1 = "spam"
    s2 = "ni!"
    print ("The Knights who say, " + s2)
    print (3 * s1 + 2 * s2)
    print (s1[1])
    print (s1[1:3])
    print (s1[2] + s2[:2])
    print (s1 + s2[-1])
    print (s1.upper())
    print (s2.upper().ljust(4) * 3)

    print (s2[0:2].upper())  
    print (s2+s1+s2)
    print (s1.capitalize() + " " + s2.capitalize() + " " + s1.capitalize() + " " + s2.capitalize() + " " + s1.capitalize() + " " + s2.capitalize())
    print (s1)
    print (s1.split("a"))
    list1 = s1.split("a")
    print ("".join(list1))

    for ch in "aardvark":
        print(ch)
    for w in "Now is the winter of our discontent...".split():
        print(w)
    for w in "Mississippi".split("i"):
        print(w, end=" ")
    msg = ""
    for s in "secret".split("e"):
        msg = msg + s
    print(msg)
    msg = ""
    for ch in "secret":
        msg = msg + chr(ord(ch)+1)
    print(msg)

spam()
