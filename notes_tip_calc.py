#Data Types
#String: "XXXXXX". Wite anything within quatation marks.
#Integer: number without decimals. Write a number as so: 12345.
#float: decimal numbers. 34.543.
#Boolean: Only has 'True' or 'False'. Test for true or false.
#Below is subscripting - Pulling an element out of a string
#print("Hello"[4]) - pulls element out of position 4.
#Function: type() - type whatever you want in function to find data type.
#Type casting: Changing data type. str()

#Small Challange
#Take the input, and then subscript the digits.

#two_digit_num = input("Type a 2 digit number: ")
#first_one = two_digit_num[0]
#second_one = two_digit_num[1]

#Turns the string variables to integers and adds them.

#results = int(first_one) + int(second_one)
#print(results)

#BMI Calculator

#height = input("Enter you height in m: ")
#weight = input("Enter your weight in kg: ")
#BMI = int(weight) / float(height) ** 2
#bmi_as_int = int(BMI)
#print(bmi_as_int)

#F-strings: infront of a string, type 'f' - you can add values into string.
#Using F-strings allows you to insert many data types into one string.
#the  {} are where the variables are placed.
#score = 0
#height = 1.8
#isWinning = True
#print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#age  = input("What is your current age? ")
#year_days =  365
#year_weeks = 52
#final_age = 90
#age_left_days = (final_age - int(age)) * 365
#age_left_weeks = (final_age - int(age)) * 52
#print(f"you have {age_left_days} days and {age_left_weeks} weeks left in your lifetime")

#Tip Calculator

print("Welcome to the tip calculator!")

total_bill = input ("What was the total bill? ")
bill_tip = input("What top would you like to give? 10, 12 or 15%? ")
total_bill_w_tip = round(float(total_bill) + (float(total_bill) * float(bill_tip) / 100), 2)

print(f"The new total of the bill is: ${total_bill_w_tip}")

total_people = input("How many people are splitting the bill? ")
bill_split = round(total_bill_w_tip / int(total_people), 2)

print(f"Each person should pay: ${bill_split}")