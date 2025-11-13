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

if float(temp) > 20:
    print("wow its going to be a hot day")

print("will it rain ?")

rain = input("yes or no ?: ")

if rain == "yes":
    print("have an umbrella with you or a rain coat be fly and dry")
else:
    print("enjoy the weather and wear some baggy jeans and a t shirt or if your not a fan of baggy jeans then just wear some shorts and a t shirt")

if float(temp) < 10:
    print("woah thats a lil cold not really my liking ")
print("will it rain ?")

rain = input("yes or no ?: ")



    

