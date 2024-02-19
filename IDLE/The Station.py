#Sylvie Edelstein
#Intro Programming
#Final Project
#This is a text-based adventure game set in a New York City subway station

inventory = []
event = []
event.append("idling rat") 
def intro(inventory, event):
#This is here so that my returned inventory and event functions are defined.

    print("""----------------------------------------
I recommend that you now expand the IDLE window to make sure all text is clear and legible.
""")
    print("""This is a text-based adventure game.
Input the letters that correlate to the choice you want to make.
Please keep your hands and feet in the subway car at all times and enjoy the ride.

""")
    print("""You pull your coat tighter as you escape the frigid air and flee down into the warm subway station.
It has been a long exhausting day of work, and as you drift on into an idle daydream, your feet seem to carry you down to the tracks.
You notice that though it is rush hour, there seem to be very few people milling about.
You begin to think about how strange that is, but the bench in the center of the platform, normally teeming with people,
calls to you and you sit down, and take a moment to revel in your mysterious solitude.
A moment later, a train rolls into the station.
""")

    choice1 = input("""
a) Examine your surroundings
b) Board the train
-------------------------------------------------

""").lower()
    #First choice of the game
    
    if choice1 == "a":
        subway(inventory, event)
        #calls subway function

    elif choice1 == "b":
        print("""You board train which suddenly jolts to life and begins speeding downtown.
'Why, this might just be the fastest train I've ever been on,' you think.
Suddenly you come to the realization that you are the only person in this train car, and it occurs to you that you might be the only person on this train!
A sudden sense of discomfort sets in but you are still quite tired,
and decide to make yourself comfortable as the train speeds along, hopefully in the general direction of home.
""")
        train(inventory, event)
        #calls the train function

    else:
        print("""Your exhaustion must be getting the best of you because that is not an option.
Please review your choices and try again.
""")
        intro(inventory, event)
        #player entered incorrect value so it returns them to the previous choice

def train(inventory, event):
    onTrain = True
    while onTrain == True:
    #Continue loops back to here

        choice6 = input("""
a) Close your eyes
b) Gaze out the window
----------------------------------

""").lower()

        newStation = True
        while newStation == True:
        #continue loops back here
            
            if choice6 == "a":
                print("""You close your eyes and let yourself be carried away by sweet slumber.
The train rattles along on this mysterious night...
...
.....
.......
.........
...........
You jolt awake! Where are you, and how long have you been out?
You soon realize that the doors to the train are open and it appears to have reached its last stop.
'But I don't recognize this station at all' you think!
You depart the train and the doors shut quickly behind you.
Oh dear. What a predicament.
""")
                if "directional knowledge" in event:
                    print ("""
To your left a set of stairs head down into darkness.
To your right an ominous elevator stalls with open doors.
Neither of these options seem particularly enticing.
Out of the corner of your eye you see a single train car labeled '!!!' and suddenly seem to recall seeing something about that train on the map board.
'Yes! I'm quite sure that train will take me home,' you think.'
""")
                    #if the player falls asleep but studied the map on the platform, they will get the option to choose the right train home

                    
                    choice8 = input("""
a) Descend the staircase
b) Enter the elevator
c) Board the !!! train
---------------------------------------

""").lower()
                    if choice8 == 'a':
                        print("You decide to descend the staircase. Feeling uneasy, you head into the darkness.")
                        badending(inventory, event)
                    elif choice8 == 'b':
                        print("""You decide to board the elevator.
Stepping inside, you see a small display of buttons.
You select one at random and begin to ascend.
You spend what feels like hours attempting to escape the station.
It feels as though the world is expanding and contracting around you.
Staircases lead to elevators leading to staircases leading to hallways leading to more elevators.
Shrouded in darkness you carry on, but to no avail.
Eventually, thoroughly exhausted, you sit down on the floor of some non-descript hallway, and close your eyes.
...
.....
.......
.........
...........
""")
                        badending(inventory, event)
                        #takes them to bad ending

                    elif choice8 == 'c':
                        print("""You board the !!! train.
The doors quickly close behind you and off you go!
A soft mechanical voice chirps over the intercom.
It simply says 'Home' and just like that the vehicle comes to a halt and the doors open.
You exit the train and find yourself in the lobby of your apartment.
Surprised, you spin back around, but all you see are the doors to the lobby.
The train is nowhere to be found.
Exhaustion hits you again and you head upstairs.
""")
                        goodending(inventory, event)
                        #takes them to good ending

                
                    else:
                        print("""Your exhaustion must be getting the best of you because that is not an option.
Please review your choices and try again.
""")
                        continue

                else:
                    print("""To your left a set of stairs head down into darkness.
To your right an ominous elevator stalls with open doors.
Neither of these options seem particularly enticing.
""")
                    choice8alternate = input("""
a) Descend the staircase
b) Enter the elevator
---------------------------------------

""").lower()
                    #alternate choice8 for if player did not read the map
                    if choice8alternate == 'a':
                        print("""You decide to descend the staircase. Feeling uneasy, you head into the darkness.
You spend what feels like hours attempting to escape the station.
It feels as though the world is expanding and contracting around you.
Staircases lead to elevators leading to staircases leading to hallways leading to more elevators.
Shrouded in darkness you carry on, but to no avail.
Eventually, thoroughly exhausted, you sit down on the floor of some non-descript hallway, and close your eyes.
...
.....
.......
.........
...........
""")
                        badending(inventory, event)
                    elif choice8alternate == 'b':
                        print("""You decide to board the elevator.
Stepping inside, you see a small display of buttons.
You select one at random and begin to ascend.
You spend what feels like hours attempting to escape the station.
It feels as though the world is expanding and contracting around you.
Staircases lead to elevators leading to staircases leading to hallways leading to more elevators.
Shrouded in darkness you carry on, but to no avail.
Eventually, thoroughly exhausted, you sit down on the floor of some non-descript hallway, and close your eyes.
...
.....
.......
.........
...........
""")
                        badending(inventory, event)
                    else:
                        print("""Your exhaustion must be getting the best of you because that is not an option.
Please review your choices and try again.
""")
                        continue


            elif choice6 == "b":
                print("""You gaze out the window as the train races along the track.
Outside, the most miraculous things are happening.
The lights of the city seem to twirl and rattle. You didn't know lights could do that.
A flock of pigeons travels alongside you for a ways performing circus tricks. 
The brooklyn bridge appears to dip and bend into the water and the sky appears to be filled with bicycles.
You wonder if the world is ending.
If it was, would it be this enchanting?
...
.....
.......
.........
...........
The train grinds to a stop and the doors open.
A robotic voice jolts you out of your seat.
'Last Stop: mn0e9wfur9825u7985 station. Please board the !!! train to take you home.'
Disembarking from the train, you assess your surroundings.
To your left a set of stairs head down into darkness.
To your right an ominous elevator stalls with open doors.
Neither of these options seem particularly enticing.
Out of the corner of your eye you see a single train car labeled '!!!' and recall what the robot voice said.
'Yes! I'm quite sure that train will take me home,' you think.'
""")

                    
                choice8alt = input("""
a) Descend the staircase
b) Enter the elevator
c) Board the !!! train
---------------------------------------

""").lower()
                #third choice8 for if the player stayed awake. If they stay awake AND read the map it doesn't matter. They need to have one of the two.
                if choice8alt == 'a':
                    print("""You decide to descend the staircase. Feeling uneasy, you head into the darkness.
You spend what feels like hours attempting to escape the station.
It feels as though the world is expanding and contracting around you.
Staircases lead to elevators leading to staircases leading to hallways leading to more elevators.
Shrouded in darkness you carry on, but to no avail.
Eventually, thoroughly exhausted, you sit down on the floor of some non-descript hallway, and close your eyes.
...
.....
.......
.........
...........
""")
                    badending(inventory, event)

                elif choice8alt == 'b':
                    print("""You decide to board the elevator.
Stepping inside, you see a small display of buttons.
You select one at random and begin to ascend.
You spend what feels like hours attempting to escape the station.
It feels as though the world is expanding and contracting around you.
Staircases lead to elevators leading to staircases leading to hallways leading to more elevators.
Shrouded in darkness you carry on, but to no avail.
Eventually, thoroughly exhausted, you sit down on the floor of some non-descript hallway, and close your eyes.
...
.....
.......
.........
...........
""")
                    badending(inventory, event)

                elif choice8alt == 'c':
                    print("""You board the !!! train.
The doors quickly close behind you and off you go!
The same soft mechanical voice chirps over the intercom.
It simply says 'Home' and just like that the vehicle comes to a halt and the doors open.
You exit the train and find yourself in the lobby of your apartment.
Surprised, you spin back around, but all you see are the doors to the lobby.
The train is nowhere to be found.
Exhaustion hits you again and you head upstairs.
""")
                    goodending(inventory, event)
                  

                else:
                    print("""Your exhaustion must be getting the best of you because that is not an option.
Please review your choices and try again.
    """)
                    continue
            else:
                print("""Your exhaustion must be getting the best of you because that is not an option.
Please review your choices and try again.
    """)
                break

def badending(inventory, event):
    print("""You awake in your bedroom. It is 6 am. Your window is open and the air is cool and crisp.
You remember leaving work yesterday, but trying to remember anything after that gives you a fierce headache.
There is a part of you that feels different.
As though something was within your grasp that you couldn't quite reach.
You wonder why that is.
The world feels a little darker.
You get ready for work.
-----------------------------------
""")
    again = input("""Would you like to play again?
a) Yes
b) No
-----------------------------------
""").lower()
    if again == "a":
        playagain()
        #calls the function before intro. This is so the inventory resets back to nothing and the event goes back to the idling rat. 

    elif again == "b":
        print("Thank you for playing!")
        #ends game

    else:
        print("""I cannot believe you actually gave me an incorrect input at the end of the game.
Your lack of care proves to me that you do not want to play again.
Goodbye.
""")


def goodending(inventory, event):
    print("""You step into your apartment and head straight for the bedroom.
Collapsing onto your mattress, you are out before your head hits the pillows.
""")
    if "metro card" and "companion rat" in inventory:
        print("""You awake to a bird gently chirping outside your open window.
The air is slightly warm and as you wipe the sleep out of your eyes, a sense of calm washes over you.
You can't help but notice the metallic metro card on your bedside table.
Hearing a skittering noise you leap out of bed and find a friendly looking rat scurrying on your hamster's old wheel.
The events of the previous night come rushing back.
They are hazy and mysterious but you are sure they were real.
Getting ready for work you are filled with a new found sense of wonderment.
As you approach the train station it occurs to you that you have many options.
Why, you could go left or right, or even up!
Yes, up! High into the sky.
Or down! Tunneling into the ground.
Or you could go backwards, into your apartment where your new companion happily awaits.
Yes, you think. I will do all of these things. Simultaenously.
The station will wait.
-----------------------------------
""")
#best ending!
        againalt = input("""Would you like to play again?
a) Yes
b) No
-----------------------------------
""").lower()
        if againalt == "a":
            playagain()

        elif againalt == "b":
            print("Thank you for playing!")

        else:
            print("""I cannot believe you actually gave me an incorrect input at the end of the game.
Your lack of care proves to me that you do not want to play again.
Goodbye.""")


    elif "metro card" in inventory:
        print("""You awake to a bird gently chirping outside your open window.
The air is slightly warm and as you wipe the sleep out of your eyes, a sense of calm washes over you.
You can't help but notice the metallic metro card on your bedside table. 
The events of the previous night come rushing back.
They are hazy and mysterious but the card calls to you, telling you to believe they were real.
Arriving on the platform for your commute, you are filled with a new found sense of wonderment.
As you step onto your morning train, you feel a sense of excitement, as though it could take you anywhere.
-----------------------------------------
""")
        again = input("""Would you like to play again?
a) Yes
b) No
-----------------------------------
""").lower()
        if again == "a":
            playagain()

        elif again == "b":
            print("Thank you for playing!")

        else:
            print("""I cannot believe you actually gave me an incorrect input at the end of the game.
Your lack of care proves to me that you do not want to play again.
Goodbye.""")


    else:
        print("""You awake to a bird gently chirping outside your open window.
The air is slightly warm and as you wipe the sleep out of your eyes, a sense of calm washes over you.
The events of the previous night come rushing back, but they are so hazy and mysterious that you can't help but believe they are a pleasant, memorable dream.
Arriving on the platform for your commute, you are filled with a new found sense of wonderment.
As you step onto your morning train, you feel a sense of excitement.
You wonder what the new day will bring.
---------------------------------------------
""")
        againalternate = input("""Would you like to play again?
a) Yes
b) No
-----------------------------------
""").lower()
        if againalternate == "a":
            playagain()

        elif againalternate == "b":
            print("Thank you for playing!")

        else:
            print("""I cannot believe you actually gave me an incorrect input at the end of the game.
Your lack of care proves to me that you do not want to play again.
Goodbye.""")

def subway(inventory, event):

    onPlatform = True
    while onPlatform == True:

        print("""----------------------------------------------
You look around the quiet station.
To your left, you see a strange object on a bench.
Straight ahead, the train seems to be idling for a peculiarly long time.
To your right, a frighteningly large rat scurries beneath the map board.
""")
        choice2 = input("""
a) look at the strange object
b) investigate the train
c) examine the rat
d) inspect the map board
e) return to previous options
-------------------------------------------------

""").lower()

        if choice2 == "a":
            if "metro card" in inventory:
                print("""You have already pocketed the metro card.
The bench is empty now, aside from you.
""")
                #They get this message if they have already picked up the metro card so they can't pick it up again. 
                continue

            else:
                print("""Upon closer inspection the strange object appears to be a peculiar metro card.
As a student your metro card was green, and beyond that it was always yellow.
This one however, appears to be lavendar and slightly metallic.
""")
                choice3 = input("""
a) Pick up the metro card
b) Leave the metro card
-------------------------------------------------

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

                elif choice3 =="b":
                    print("""That metro card is definitely someone else's trash.
Better to leave it alone.
""")
                    continue

                else:
                    print("""Your exhaustion must be getting the best of you because that is not an option.
Please review your choices and try again.""")
                    continue
            

        elif choice2 == "b":
            print("""
You move closer to the stalled vehicle.
Upon closer inspection, this seems to be the @!*#$ train.
How strange, you think. You usually take the Q.
""")
            choice4 = input("""
a) Board the train
b) Do not board the train
-------------------------------------------------

""").lower()
            if choice4 == "a":
                print("""
Feeling curious, you board the @!*#$ train, even though it is most certainly not the Q.
It suddenly jolts to life and begins speeding downtown.
'Why, this might just be the fastest train I've ever been on,' you think.
Suddenly you come to the realization that you are the only person in this train car, and it occurs to you that you might be the only person on this train!
Oddly enough, you do not feel afraid, but you are still quite tired, and decide to make yourself comfortable as the train speeds along, hopefully in the general direction of home.
""")
                train(inventory, event)
        
            elif choice4 =="b":
                print("""
This is most certainly not the Q, and therefore not the train you take home.
You decide that the @!*#$ is simply too suspicious to ride and return to the middle of the platform.
""")       
            else:
                print("""Your exhaustion must be getting the best of you because that is not an option.
Please review your choices and try again.""")
                continue

        elif choice2 == "c":
            if "idling rat" in event:
                print("""'That,' you think, 'is the biggest and most peculiar rat I have ever seen in my entire life.
You realize that just as you have been looking at the rat, it too has been looking at you.
In fact, though you can't seem to understand why, you feel a startling kinship for this rat.
All of a sudden he darts away and slips into a vent through a door at the far end of the platform.
""")
                event.remove("idling rat")
                event.append("followable rat")
                #This just means they know where the rat went

                choice5 = input("""
a) Follow the rat
b) Stay on the platform
-------------------------------------------------

""").lower()
                if choice5 == "a":
                    print("""You scurry after the rat to the end of the platform.
You see that the door is labeled 'Maintenance Room' and feel compelled to see if the door is unlocked.
Turning the knob the door opens with a resounding creek!
You step inside and are surprised to find a dimly lit hallway.
You hear skittering noises all around you and are quite sure the rat has many friends.
Venturing down the corridor, you come to a door at the other end and eagerly open it.
You gasp! This is a sight to behold!
Before you is another subway station!
This one however, is bustling with rats!
While your station was empty, this one is teeming with life.
There are rats readings newspapers, rats inspecting their own map board, rats scrounging through the garbage...
There are even two rats compelling commuters to hear the words of Jesus Christ!
At least, you think that's what they're doing as they skitter happily back and forth across a bible.
Finally, your eyes land on the rat you followed in, who seems to be playing a game of chess out of a briefcase on the bench.
You approach the rat cautiously and kneel down and he happily abandons his game to curl up on your shoulder.
Just then a train pulls into the station.
A rat conductor scurries up the side of the window to be at nearly eye level with you and motions for you to present something to her.
'She must want my metro card, you think.'
""")
                    if "metro card" in inventory:
                        print("""You fish around in your pockets but can't seem to find your metro card.
'How could I have lost it,' you think, puzzled.
Suddenly, you hand grasps something cold, and you remember the lavender card you pocketed earlier!
You excitedly present the card to the conductor whose rat eyes go wide.
She leaps up onto to your upturned wrist and takes a small bite of the card before motioning for you to board the train and slipping back inside.
The rat has fallen asleep on your shoulder and as your board the train, you get comfortable and envision your happy future together.
""")
                        inventory.append("companion rat")
                        train(inventory, event)

                    else:
                        print("""You fish around in your pockets but can't seem to find your metro card.
'How could I have lost it,' you think, puzzled.
You shake your head sadly and the conductor squeaks something angrily.
It seems as though you won't be able to board this train.
You look around for the door you entered through but it's no where to be found!
The rat nuzzles you one more time before leaping off your shoulder and scurrying away.
Sitting down on the bench, you put your head in your hands in frustration, and soon find yourself drifting off into a disappointing slumber.
""")
                        badending(inventory, event)

                elif choice5 == "b":
                    print("""You decide you'd rather not spend your night chasing a rat.
After all, just how interesting could a rat's life even be?
""")
                    continue

                else:
                    print("""Your exhaustion must be getting the best of you because that is not an option.
Please review your choices and try again.""")
                    continue

            elif "followable rat" in event:
                print("You remember seeing the rat go through the door at the far end of the station.")
                alternatechoice5 = input("""
a) Follow the rat
b) Stay on the platform
-------------------------------------------------

""").lower()
                if alternatechoice5 == "a":
                    print("""You scurry after the rat to the end of the platform.
You see that the door is labeled 'Maintenance Room' and feel compelled to see if the door is unlocked.
Turning the knob the door opens with a resounding creek!
You step inside and are surprised to find a dimly lit hallway.
You hear skittering noises all around you and are quite sure the rat has many friends.
Venturing down the corridor, you come to a door at the other end and eagerly open it.
You gasp! This is a sight to behold!
Before you is another subway station!
This one however, is bustling with rats!
While your station was empty, this one is teeming with life.
There are rats readings newspapers, rats inspecting their own map board, rats scrounging through the garbage...
There are even two rats compelling commuters to hear the words of Jesus Christ!
At least, you think that's what they're doing as they skitter happily back and forth across a bible.
Finally, your eyes land on the rat you followed in, who seems to be playing a game of chess out of a briefcase on the bench.
You approach the rat cautiously and kneel down and he happily abandons his game to curl up on your shoulder.
Just then a train pulls into the station.
A rat conductor scurries up the side of the window to be at nearly eye level with you and motions for you to present something to her.
'She must want my metro card, you think.'
""")
                    if "metro card" in inventory:
                        print("""You fish around in your pockets but can't seem to find your metro card.
'How could I have lost it,' you think, puzzled.
Suddenly, you hand grasps something cold, and you remember the lavender card you pocketed earlier!
You excitedly present the card to the conductor whose rat eyes go wide.
She leaps up onto to your upturned wrist and takes a small bite of the card before motioning for you to board the train and slipping back inside.
The rat has fallen asleep on your shoulder and as your board the train, you envision your happy future together.
""")
                        inventory.append("companion rat")
                        train(inventory, event)

                    else:
                        print("""You fish around in your pockets but can't seem to find your metro card.
'How could I have lost it,' you think, puzzled.
You shake your head sadly and the conductor squeaks something angrily.
It seems as though you won't be able to board this train.
You look around for the door you entered through but it's no where to be found!
The rat nuzzles you one more time before leaping off your shoulder and scurrying away.
Sitting down on the bench, you put your head in your hands in frustration, and soon find yourself drifting off into a disappointing slumber.
""")
                        badending(inventory, event)

                elif alternatechoice5 == "b":
                    print("""You decide you'd rather not spend your night chasing a rat.
After all, just how interesting could a rat's life even be?
""")
                    continue

                else:
                    print("""Your exhaustion must be getting the best of you because that is not an option.
Please review your choices and try again.""")
                    continue
                
            else:
                print("The abnormally large rat seems to have scurried away.")
                continue
    
                         
        elif choice2 == "d":
            if "broken map board" in event:
                print("You remember that you have broken the map board and slink away.")
                continue

            elif "directional knowledge" in event:
                print("You think you've learned everything there is to know about the map board already.")
                continue

            else:
                if "idling rat" in event:
                    print("""You idle up to the map board and begin inspecting it.
'Is it just me,' you think, 'or is this thing more complicated than usual?'
As you inspect the eerily flickering electronic map board and ponder how the train lines seems to be intersecting in new, dizzying ways,
the large rat underneath scurries away.
""")
                    event.remove("idling rat")

                    choice7 = input("""
a) Try and fix the map board
b) Study the train lines
-------------------------------------

""").lower()
                    if choice7 == "a":
                        print("""
You knock lightly on the map in hopes of recalibrating it.
The machine lets out an angry whir and the board goes dark.
It is safe to say that you have broken it.
You sheepishly return to the platform.
""")
                        event.append("broken map board")
                        continue
                
                    elif choice7 == "b":
                        print("""You study the train lines intently.
After a few minutes you begin to develop a strong headache and have to step away.
Still, you think your studies have imparted you with some important knowledge.
""")
                        event.append("directional knowledge")
                        continue

                    else:
                        print("""Your exhaustion must be getting the best of you because is not an option.
Please review your choices and try again.""")
                        continue
                    

                elif "followable rat" in event:
                    print("""
You idle up to the map board and begin inspecting it.
'Is it just me,' you think, 'or is this thing more complicated than usual?'
""")
                    alternatechoice7 = input("""
a) Try and fix the map board
b) Study the train lines
-------------------------------------

""").lower()
                    if alternatechoice7 == "a":
                        print("""
You knock lightly on the map in hopes of recalibrating it.
The machine lets out an angry whir and the board goes dark.
It is safe to say that you have broken it.
You sheepishly return to the platform.
""")
                        event.append("broken map board")
                        continue
                
                    elif alternatechoice7 == "b":
                        print("""You study the train lines intently.
After a few minutes you begin to develop a strong headache and have to step away.
Still, you think your studies have imparted you with some important knowledge.
""")
                        event.append("directional knowledge")
                        continue

                    else:
                        print("""Your exhaustion must be getting the best of you because is not an option.
Please review your choices and try again.""")
                        continue
            
                else: 
                    print("""You idle up to the map board and begin inspecting it.
'Is it just me,' you think, 'or is this thing more complicated than usual?
""")
                    altchoice7 = input("""
a) Try and fix the map board
b) Study the train lines
-------------------------------------

""").lower()
                    if altchoice7 == "a":
                        print("""
You knock lightly on the map in hopes of recalibrating it.
The machine lets out an angry whir and the board goes dark.
It is safe to say that you have broken it.
You sheepishly return to the platform.
""")
                        event.append("broken map board")
                        continue
                    #once the map board is broken they no longer get the option to use it
                
                    elif altchoice7 == "b":
                        print("""You study the train lines intently.
After a few minutes you begin to develop a strong headache and have to step away.
Still, you think your studies have imparted you with some important knowledge.
""")
                        event.append("directional knowledge")
                        continue
                    #comes in handy if they fall asleep on the train!

                    else:
                        print("""Your exhaustion must be getting the best of you because is not an option.
Please review your choices and try again.""")
                        continue                

        elif choice2 == "e":
            intro(inventory, event)

        else:
            print("""Your exhaustion must be getting the best of you because that is not an option.
Please review your choices and try again.""")
            continue        

def playagain():
    inventory = []
    event = []
    event.append("idling rat")
    intro(inventory, event)
    #this function clears the inventory before the start of intro. 

intro(inventory, event)


