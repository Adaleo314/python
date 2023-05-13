# if statements
#Simple if input statement
friend = "Joe"
user_name = input("Enter your name here: ")

#if/else boolean example
if user_name == friend:
  print("Whats up, bro")
else:
  print("I dont know you!")   


friends_list = ["Bill", "Steve", "Mike"]
family_list = ["Lei", "Nicole"]

#Can put as many elif statments, eval in order
if user_name in friends_list:
  print("Whats up friend")
elif user_name in family_list:
  print("Whats up Fam!")
else:
  print("Stranger Danger")
