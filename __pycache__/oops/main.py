from postoffice import post_office

# Create an instance of the post_office class
g1 = post_office()

# Calculate interest for predefined customers
g1.intrest_calc("yeswanth", 5, 1500, 32)
g1.intrest_calc("yesh", 20, 2500, 50)
g1.intrest_calc("ganesh", 4, 2500, 67)

# Calculate interest for user input
name = input("Enter your name: ")
years = int(input("Enter the number of years to invest: "))
amount = int(input("Enter the amount to invest per month: "))
age = int(input("Enter your age: "))

g1.intrest_calc(name, years, amount, age)

