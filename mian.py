print("What is the weather forcast for tomorrow")
while True:
    temp = input("Temperature: " )
    try:
        float(temp)
        break
    except ValueError:
        print("please enter a valid number for temperature")

print("the Temperature is " + temp)

print("would you like it to be converted into fahrenheit ? ")

user_choice = input("yes or no ?: ")


try:
    if user_choice == "yes":
        fahrenheit = float(temp) * 9/5 + 32
        print(fahrenheit)
    else:
         print("okay i wont convert it")

except ValueError:
    print("please enter a valid number for temperature")

