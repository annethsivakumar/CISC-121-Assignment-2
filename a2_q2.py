import functions

def main():
  """
  This function implements the interface for the program.
  Parameters: None.
  Return: None.
  """
  # Initialize dictionary
  friend_dict = functions.friends_to_dictionary()
  # Call friendship_degree function
  functions.friendship_degree(friend_dict)
  # Print the friends of a users
  name = "Max"
  print("\n" + name + "'s friends:  " + str(functions.all_my_friends(name)))


main()
