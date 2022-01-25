# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lower_case_name_1 = name1.lower()
lower_case_name_2 = name2.lower()

together_lower_names = lower_case_name_1 + lower_case_name_2

true_count = together_lower_names.count("t") + together_lower_names.count("r") + together_lower_names.count("u") + together_lower_names.count("e")

love_count = together_lower_names.count("l") + together_lower_names.count("o") + together_lower_names.count("v") + together_lower_names.count("e")

total_score = int(str(true_count) + str(love_count)) 

if (total_score < 10) or (total_score > 90):
  print(f"Your score is {total_score}, you go together like coke and mentos.")
elif (total_score >= 40) and (total_score <= 50):
  print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {total_score}.")
   
