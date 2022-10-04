# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


low_name1 = name1.lower()
low_name2 = name2.lower()

two_names = low_name1+low_name2

truecount = two_names.count("t") + two_names.count("r") + two_names.count("u") + two_names.count("e")
# print(truecount, type(truecount))

lovecount = two_names.count("l") + two_names.count("o") + two_names.count("v") + two_names.count("e")
# print(lovecount, type(lovecount))

truelovecount = int(str(truecount)+str(lovecount))
# print(truelovecount, type(truelovecount))

if truelovecount < 10 or truelovecount > 90:
    print(f"Your score is {truelovecount}, you go together like coke and mentos.")
elif truelovecount > 40 and truelovecount < 50:
    print(f"Your score is {truelovecount}, you are alright together.")
else:
    print(f"Your score is {truelovecount}.")
