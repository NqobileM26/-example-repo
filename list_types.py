# First create a list called friends_names
# Store the full names of three friends in this list
# Print the name of the first friend in the list
# Print the name of the last friend in the list
# Print the total number of friends (length of the list)
# Create another list called friends_ages
# Store the ages of the same three friends in corresponding order
# FOR each index in the range from 0 to the length of the list:
# Get the friend's name, Get the friend's age,
# Print a sentence like: "<Name> is <Age> years old"

# List of friends names
friend_names = ["Nqobile", "Iminathi", "Bheka"]

# print the name of the first friend
print("First friend:", friend_names[0])

# print the name of the last friend
print("Last friend:", friend_names[-1])

# Print the lenght of the list
print("Number of friends:", len(friend_names))

# List of the friends age
friends_age = [30, 20, 33]

# Print each friend with thier name and age
for i in range(len(friend_names)):
    print(f"{friend_names[i]} is {friends_age[i]} years old")