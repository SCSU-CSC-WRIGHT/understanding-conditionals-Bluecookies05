## ============ temperature check ================
temp_check = int(input("What is the weather temp today in celcuis?: "))

if temp_check>30: 
    print(" Its a hot day! ")
else: 
    print(" the weather is cool  ")

## ============ Number comparision ===============

number1 = int(input(" what is the first number? "))
number2 = int(input(" what is the secpnd number? "))

if number1<number2:
    print( number2 )
elif number1>number2:
    print( number1 )
else:  
    print(" both numbers are the same! ")

## ============ password checker =================
user_password = input("Type your password in: ")
admin_password = "admin"  

if admin_password == user_password:
    print("Access granted!")
else:
    print("STRANGER ALERT GET OUT!!!!")

## ============ simple calculatior ===============

number_1 = int(input("What is the first number? "))
number_2 = int(input("What is the second number? "))
op = input("Enter operator (+, -, *, /): ") 

if op == '+':
    print(number_1 + number_2)
elif op == '-':
    print(number_1 - number_2)
elif op == '*':
    print(number_1 * number_2)
elif op == '/':
    print(number_1 / number_2)
else:
    print("Invalid operator!")

## ============ positive, negative or 0 ==========

mystery = int(input(" what is your number?:  "))

if mystery>1:
    print(" your number is a positive! ")
elif mystery<1:
    print(" your number is less than one! ")
else:
    print(" your number is equal to 0!! ")

## ============ day of the week ==================

day_of_week = int(input("Put a number between 1-7: "))

if day_of_week == 1:
    print("Monday")
elif day_of_week == 2:
    print("Tuesday")    
elif day_of_week == 3:
    print("Wednesday")
elif day_of_week == 4:
    print("Thursday")
elif day_of_week == 5:
    print("Friday")
elif day_of_week == 6:
    print("Saturday")
elif day_of_week == 7:
    print("Sunday")
else:
    print("Invalid number! Please enter a number between 1 and 7.")
