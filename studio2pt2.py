#######################################################################
# Program Filename: studio2
# Author:  John Von Worley
# Date: 4/5/2022
# Description: Script to calculate how many gallons of gas a car will use per year
# Input:  "mpg"
# Output: "actual_power"
#######################################################################

mpg = float(input("Input the average miles per gallon that your car gets."))
#finds how many gallons the user's car gets

gal_year = 14032/mpg
#calculates how many gallons of gas you use per year based on mpg of car

print("your total yearly usage is", gal_year, "gallons per year.")
#prints the final message with total gallons per year used