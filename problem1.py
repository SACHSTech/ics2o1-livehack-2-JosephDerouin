'''
-------------------------------------------------------------------------------
Name:        problem1.py
Purpose:    Speedlimit Decider>

Author:    Derouin.J

Created:    date in 23/02/2021
------------------------------------------------------------------------------
'''



#Enter Speed Limit
speedlimit = float(input("Enter the speed limit: "))
#Enter Your Speed
yourspeed = float(input("Enter the recorded speed of the car: "))


overlimit = int(yourspeed - speedlimit)

#Formula
if overlimit >= 31 :
  print("You are speeding and your fine is $570. ")

elif overlimit >= 21 and overlimit <= 30 :
  print("You are speeding and your fine is $270 ")

elif overlimit >= 1 and overlimit <= 20 :
  print ("You are speeding and your fine is $100 ")

elif overlimit <= 1 :
  print("Congratulations, you are within the speed limit!")

run = "python problem2.py"