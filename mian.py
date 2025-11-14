
print("What is the weather forecast for tomorrow")


while True:
    temp_input = input("Temperature (C): ")
    try:
        temp = float(temp_input)
        break
    except ValueError:
        print("Please enter a valid number for temperature.")

print("The temperature is " + str(temp) + "°C")

print("Would you like it to be converted into Fahrenheit?")
user_choice = input("yes or no?: ").lower()

if user_choice == "yes":
    fahrenheit = temp * 9/5 + 32
    print(str(fahrenheit) + "°F")
else:
    print("Okay, I won’t convert it.")


if temp > 20:
    print("Wow, it's going to be a hot day!")

print("Will it rain?")
rain = input("yes or no?: ").lower()

if rain == "yes":
    print("Have an umbrella or raincoat — be fly and dry!")
else:
    print("Enjoy the weather! Wear some baggy jeans and a t-shirt, or shorts if you prefer.")

if temp < 10:
    print("Woah, that's a little cold—not my preference!")

print("Will it rain?")
rain = input("yes or no?: ").lower()

if rain == "yes":
    print("Wear a nice statement jacket or hoodie and bring an umbrella stay fly and dry.")
else:
    print("If you like the cold, enjoy it just dress appropriately!")

if temp < 5:
    print("It's really cold I do not like that!")

print("Will it rain?")
rain = input("yes or no?: ").lower()

if rain == "yes":
    print("Cover up completely cold AND rain is the worst combination.")
else:
    print("At least it's not raining but it's still cold Wear a ski mask a puffer jacket gloves and a beanie to stay warm.")



    

