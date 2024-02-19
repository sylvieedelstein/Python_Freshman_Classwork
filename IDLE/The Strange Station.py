#Sylvie Edelstein
#Intro Programming
#Final Project
#This is a text-based adventure game set in a New York City subway station

inventory = []
event = []

def intro():
    event.append("idling rat")

    print("""I reccomend that you now expand the IDLE window to make sure all text is clear and legible.
""")
    print("""This is a text-based adventure game.
Input the letters that correlate to the choice you want to make.
Please keep your hands and feet in the subway car at all times and enjoy the ride.

""")
    print("""You pull your coat tighter as you escape the frigid air and flee down into the warm subway station.
It has been a long exhausting day of work, and as you drift on into an idle daydream, your feet seem to carry you down to the tracks.
You notice that though it is rush hour there seem to be very few people milling about.
You begin to think about how strange that is, but the bench in the center of the platform, normally teeming with people,
calls to you and you sit down, and take a moment to revel in your mysterious solitude.
A moment later, a train rolls into the station.
""")

    choice1 = input("""
a) Examine your surroundings
b) Leave the station
c) Board the train

""").lower()
        
    if choice1 == "a":
        print("""
You look around the quiet station.
To your left, you see a strange object on a bench.
Straight ahead, the train seems to be idling for a peculiarly long time.
To your right, a frighteningly large rat scurries beneath the map board.
""")
    subway()

def subway():

    onPlatform = True
    while onPlatform == True:

        choice2 = input("""
a) look at the strange object
b) investigate the train
c) examine the rat
d) inspect the map board
e) return to previous options
""").lower()

        if choice2 == "a":
            if "metro card" in inventory:
                print("""
You have already pocketed the metro card.
The bench is empty now, aside from you.
""")
                continue

        else:
            print("""
Upon closer inspection the strange object appears to be a peculiar metro card.
As a student your metro card was green, and beyond that it was always yellow.
This one however, appears to be lavendar and slightly metallic.
""")
            choice3 = input("""
a) Pick up the metro card
b) Leave the metro card
""").lower()

            if choice3 == "a":
                print("""You gingerly reach for the glimmering card.
It's cool to the touch.
How odd, you think.
This day really couldn't get any stranger.
You place the card in your deepest coat pocket, so it will never be lost.
""")

                inventory.append("metro card")
                continue

            elif choice3 == "b":
                print("""That metro card is definitely someone else's trash.
Better to leave it alone.
""")
                continue

            else:
                print("""
Your exhaustion must be getting the best of you since that is not an option. Please review your choices and try again.
""")
                continue

        elif choice2 == "b":
            print("""
You move closer to the stalled vehicle.
Upon closer inspection, this seems to be the @!*#$ train.
How strange, you think. You usually take the Q.
""")

            choice4 = input("""
a) Board the train.
b) Do not board the train """).lower()

            if choice4 == "a":
                print("""
Feeling curious, you board the @!*#$ train, even though it is most certainly not the Q.
It suddenly jolts to life and begins speeding downtown.
'Why, this might just be the fastest train I've ever been on,' you think.
Suddenly you come to the realization that you are the only person in this train car, and it occurs to you that you might be the only person on this train!
Oddly enough, you do not feel afraid, but you are still quite tired, and decide to make yourself comfortable as the train speeds along, hopefully in the general direction of home.
""")
                pass

            elif choice4 == "b":
                print("""
This is most certainly not the Q, and therefore not the train you take home.
You decide that the @!*#$ is simply too suspicious to ride and return to the middle of the platform.
""")
                continue

        elif choice2 == "c":
            if "idling rat" in event:
                print("""
'That,' you think, 'is the biggest and most peculiar rat I have ever seen in my entire life.
You realize that just as you have been looking at the rat, it too has been looking at you.
In fact, though you can't seem to understand why, you have this feeling that you and the rat have known eachother for a very long time.
All of a sudden the rat darts away and slips into a vent through a door at the far end of the station.""")

                event.remove("idling rat")
                event.append("followable rat")

                choice5 = input("""
a) Follow the rat
b) Stay on the platform
""").lower()

            elif "followable rat" in event:
                print("You remember that the rat went through a door at the other end of the station.")
                print("")
                print("")
                alternatechoice5 = input("""
                                         a) Follow the rat
                                         b) Stay on the platform
                                         """).lower()
                        
                        
            else:
                print("The abnormally large rat seems to have scurried away.")
                print("")
                print("")


        elif choice2 == "d":
            print("""
You idle up to the map board and begin inspecting it.
'Is it just me,' you think 'or is this thing more complicated than usual?'
As you ponder how all the train lines seems to be intersecting in new, dizzying ways, the large rat underneath scurries away.""")
            print("")
            print("")
            event.remove("idling rat")
            continue

        elif choice2 == "e":
            intro()

        else:
            print("test")

intro()
                
            


