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

if user_choice == "yes":
    fahrenheit = float(temp) * 9/5 + 32
    print(fahrenheit + " F")
else:
    print("okay i wont convert it")

# except ValueError:
#     print("please enter a valid number for temperature") 

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
if rain == "yes":
    print("have a statement piece with you like the jacket or hoodie that you have been wanting to wear but haven't had the chance to yet and a umbrella as an acessory be fly and dry")
else:
    print("cold is not really my liking but if you like the cold enjoy the weather dress apropreately")

if float(temp) < 5:
    print("it is really cold i do not like that ")
print("will it rain ?")
 
rain = input("yes or no ?: ")

if rain == "yes":
    print("cover up completely not only is it cold but its raining too which is the worse ")
else:
    print("atleast its not raining but its still pretty cold weather so wear your ski mask and 700 northface puffer jacket or canada goose if you have one and some gloves and a beanie to keep you warm")



    

