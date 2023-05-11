friend_name = "Adam"
greeting = "Hi, my name is {name}"

#Taking in a string while running format
final_greeting = greeting.format(name=friend_name)

print(final_greeting)

#input function
your_name = input("Enter your name:")
print(f"Hello {your_name}. My name is {friend_name}!")

age = input("Enter your age: ")
#must make the string into an integer
age_num = int(age)
print(f"You have lived for {age_num * 12} months")

#making dynamic input static with nesting

age = int(input("Enter your age: "))
print(f"You have lived for {age * 12} months.")
