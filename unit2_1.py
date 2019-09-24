# by Ariana Daney
# Last modified September 23, 2019
# Unit 2 final project, option 1

name = (input("What is your name?"))
print("Hello", name, ", my name is Pablo, its nice to meet you!")

location = (input("Where are you from?"))
print("I have never been to", location, "but I would love to visit")

favorite_number = int(input("what is your favorite number?"))
my_number = (favorite_number / 2)
print("your favorite number, ", favorite_number, "is double of my favorite number", my_number, "!")

dream_car = input("What is your favorite car?")
print("A", dream_car, "sounds like an awesome car")

car_cost = float(input("What does your dream car cost?"))
print("Wow!", car_cost, "is a lot!")

years = int(input("How many years would you take a loan to get your car"))

annual_rate = float(input("Whats the annual interest rate for your car?"))
monthly_interest = (annual_rate / 100) / 12
number_of_monthly_payments = years * 12
monthly_payment = ((monthly_interest * car_cost) / (1 - (1 + monthly_interest) ** -number_of_monthly_payments))
total_cost = monthly_payment * (years * 12)
print("Your monthly payment for your", dream_car, "would be $", monthly_payment, "and your total cost would be $",
      total_cost, "good luck!")
print("I have to go now", name, ", but it was nice talking to you!")

