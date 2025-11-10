print("What is the weather forcast for tomorrow")

temp = input("Temperature: " )

print("the Temperature is " + (temp))

print("would you like it to be converted into fahrenheit ? ")

user_choice = input("yes or no ?: ")


try:
    if user_choice == "yes":
        fahrenheit = temp * 9/5 + 32
    else:
        print("okay i wont convert it")
except ValueError:
    print("please enter a valid response")