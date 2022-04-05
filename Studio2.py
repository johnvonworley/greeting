#######################################################################
# Program Filename: studio2
# Author:  John Von Worley
# Date: 4/5/2022
# Description: Script to calculate how many gallons of gas a car will use per year
# Input: "cost_gallon" "mpg" "gal_year"
# Output: "" "actual_power"
#######################################################################

#################################################################
#How many gallons of gasoline was used total for the year in Oregon in 2019?
#https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=A103650411&f=M   How many people have a license in Oregon?   	https://www.oregon.gov/odot/dmv/pages/news/factsstats.aspx
#Calculate the number of gallons of gas that were used per person in Oregon in 2019.
#Print output.
###########################################################################

gas_2019 = (97.7+99.7+104.3+103.8+101.4+110.2+110.7+112.2+106.1+112.4+98.3+105.8)*30000
#total amount of gas used in Oregon through 2019 in gallons

drivers = 3100000
#total oregon drivers who are registered

avggas2019 = (gas_2019/drivers)

print("Driving Oregonians used an average of", round(avggas2019, 2), "gallons of gas per person in 2019")




