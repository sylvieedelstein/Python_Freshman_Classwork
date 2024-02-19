#distance.py
#Sylvie Edelstein
#9/20/22
#This program finds the distance between two points.

import math
def main():
  print ("This program finds the distance between two points")
  print ("")
  x1, y1 = eval(input("Enter an x coordinate and a y coordinate seperated by a comma. "))
  x2, y2 = eval(input("Enter a second x coordinate and y coordinate seperated by a comma. "))
  leg1 = (x2-x1)
  leg2 = (y2-y1)
  distance = math.sqrt((leg1)*(leg1) + (leg2)*(leg2))
  distance1 = round(distance)
  distance2 = round(distance, 1)
  distance3 = math.ceil(distance)
  print("")
  print("The distance rounded to the nearest whole number, tenth, and the nearest higher number is", distance1, distance2, distance3)
  print("")
  print("Thank you for finding a distance! Press the <Enter> key to quit!")

main()
