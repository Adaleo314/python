#Lists

friends = ["Bill", "Tom", "Steve", "Lei", "Joe"]
friends_age = ["Joe", 33], ["Nicole", 36], ["Sparky", 7]
print(friends)
print(friends[3])

print(friends_age)
print(friends_age[2])

#add to a list
friends.append("Zac")
print(friends)
friends.remove("Steve")

#Tuples - comma = a tuple
# can not append/add to a tuple
tuple = ("Mike", "Josh")
tuple_list = [("Mike", "Josh")]

#Sets - Do not hold an order
#Curly braces = a set
golf_bros = {"Jordan", "Kenny", "Matt", "Steven"}
bball_bros = {"Mike", "Steven", "Bryant"}

golf_not_bball = golf_bros.difference(bball_bros)
print(golf_not_bball)

not_in_both = golf_bros.symmetric_difference(bball_bros)
print(not_in_both)

golf_and_bball = golf_bros.intersection(bball_bros)
print(golf_and_bball)

all_bros = golf_bros.union(bball_bros)
print(all_bros)
