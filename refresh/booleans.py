#Booleans  True/False
age = 20

is_over_age = age >= 18
is_under_age = age < 18
is_twenty = age == 20

my_number = 5
user_number = int(input("Enter a number: "))
print(my_number == user_number)

#And/or statements
age = int(input("Enter your age: ")) 
can_learn = age > 0 and age < 100

print(f"You can learn programming: {can_learn}.")
