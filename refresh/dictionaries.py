#Dictionaries - stores keys and values
#Order is kept, cannot have duplicate keys

friends_ages = {"Bill": 35, "Adam": 35, "Jeff": 23}

print(friends_ages["Bill"])
#list/tuple of dictionaries

friends = (
  {"name": "John Smith", "age": 40},
  {"name": "Bill Murray", "age": 70},
  {"name": "Mike Jones", "age": 42}
)
print(friends)

grades = [95, 80, 88, 91, 82]
total_grade = sum(grades)
print(total_grade)
average_grade = sum(grades) / len(grades)
print(average_grade)
