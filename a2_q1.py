"""
CISC-121 2023W
Name: Anneth Sivakumar
Student Number: 20320973
Email:  21as221@queensu.ca
Date: 2023-02-01
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity.
"""
from functions import all_odd_or_even

def main():
  """
  This function implements the interface for the program.
  Parameters: None.
  Return: None.
  """
  # Print the purpose of this program.
  print(
    "-----------------------------------------" +
    "\n" +
    "This program allows you to enter as many numbers as you would like." +
    "\n" +
    "If your set of numbers are all even or all odd..." +
    "\n" + 
    "The program will print 'True', otherwise it will print 'False'." +
    "\n" +
    "-----------------------------------------" + 
    "\n")
  # Create an empty list to store numbers given by user.
  data_list =  []
  # Ask user if they would like to participate.
  print("Would you like to participate in this activity?")
  play = input("Enter 'yes' to continue or any other key to quit: ").lower()
  if (play == "yes"):
    # try - except is used to only accept integer values.
    try:
      # Ask user for integers for the function, and append number to the list.
      num = int(input("Please enter an integer into the function: "))
      data_list.append(num)
      # Ask user if they would like to continue adding numbers.
      print("\n" + "Would you like to enter another number?")
      play = input("Enter 'yes' to continue or any other key to quit: ").lower()
      while (play == "yes"):
        # Append all others number into the list, until user stops.
        additional_num = int(input("Please enter another number: "))
        data_list.append(additional_num)
        print("\n" + "Would you like to enter another number?")
        play = input("Enter 'yes' to continue or any other key to quit: ").lower()
      if(play != "yes"):
        # Convert list into a tuple for function and printing.
        data_tuple = tuple(data_list)
        # Print user's numbers and the output of the all_odd_or_even function.
        print("\n" + "Your chosen numbers: " + str(data_tuple))
        print("Set of Numbers Are All Even or Odd: " + str(all_odd_or_even(*data_tuple)))
    except ValueError:
      print("\n" + "ERROR: ENTERED VALUE WAS NOT AN INTEGER!")
  else:
    print("\n" + "You choose not to participate.")


main()