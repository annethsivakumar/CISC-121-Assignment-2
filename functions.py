"""
CISC-121 2023W
Name: Anneth Sivakumar
Student Number: 20320973
Email:  21as221@queensu.ca
Date: 2023-02-01
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity.
"""

def all_odd_or_even(*args):
  """
  This function is used to determine if the user given value meet the specific conditions.
  Parameters: *args - a variable that accepts any number of arguments.
  Return: True, if all conditions are met.
          False, if a condition is not met.
  """
  # Check if there is at least one argument.
  if (len(args) == 0):
    return False
  # Check if elements in args are all integer.
  for elements in args:
    if (isinstance(elements, int) == False):
      return False
  # Check if all elements are even or odd.
  is_even = 0  # Track number of even numbers.
  is_odd = 0  # Track number of odd numbers.
  for elements in args:
    if (elements % 2) == 0:
      is_even += 1
    else:
      is_odd += 1
  if ((is_even == len(args)) or (is_odd == len(args))):
    return True
  else:
    return False


def friends_to_dictionary():
  """
  This function reads friendship.txt, and converts the file into a dictionary.
  Parameters: None.
  Returns: dictionary - a dictionary of users and their friends.
  """
  # Create empty dictionary to store user and friends.
  user_friends = {}
  # Open friendship.txt file for reading.
  file = open("friendship.txt", "r")
  for line in file:
    # Convert each line into a list.
    # Split the list into person1 and person2.
    person1, person2 = line.strip().split()
    # If user is not present in dictionary keys, make the name a key.
    # Put the friend into a list and make it the value.
    if person1 not in user_friends:
      user_friends[person1] = [person2]
    # If user does exist in dictionary, append friend to the list of values.
    else:
      user_friends[person1].append(person2)
    # Do the same thing, but person2 is friends with person1.
    if person2 not in user_friends:
      user_friends[person2] = [person1]
    else:
      user_friends[person2].append(person1)
  file.close()
  return user_friends


def all_my_friends(friend):
  """
  This function allows the user to search a person's friends.
  Parameters: person - the person being searched.
  Return: list - a list of that person's friends.
  """
  # Call friends_to_dictionary() to create a dictionary.
  dict = friends_to_dictionary()
  # Return the value using the user or error message is user not found.
  if friend in dict:
    return dict[friend]
  else:
    return "ERROR: NAME NOT FOUND!"


def friendship_degree(dict):
  """
  This function writes the number of friends each person has along with their names.
  Parameters: dict - a dictionary of the user's and their person.
  Return: None.
  """
  # Loop through each key in the dictionary and print number of friends and their names.
  for key in dict:
    if (len(dict[key]) <= 1):
      print(key + " has " + str(len(dict[key])) + " friend: " +
            str(tuple(dict[key])).replace(",", "").replace("'", ""))
    else:
      print(key + " has " + str(len(dict[key])) + " friends: " +
            str(tuple(dict[key])).replace("'", ""))
