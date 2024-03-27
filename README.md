Question 1: Modules and Functions
------------
In the functions.py file, write a function called all_odd_or_even to meet the following
specifications:
- Accept any number of arguments
- Return True if
  - it receives at least one argument, AND
  - all the arguments are integers, AND
  - the arguments are either all odd OR all even
- Return False in all other situations (including the situation in which it is called with no arguments or invalid arguments)

Import this function, and this function only, into your main program in a2_q1.py.

In this main program, you are going to ask the user to input all of the arguments into this
function by doing the following:
- Begin by introducing what you are doing to the user and ask if they would like to participate in this activity. Only proceed if the user answers yes.
- Ask the user for an integer to add to this function.
- If an integer is provided:
  - Save the integer so you can send it to the function later
  - Ask if they would like to add another integer. Only proceed if they say yes.
- If an integer is not provided:
  - Quit, and give the user an error message.
- When the user is done, call the function on the integers provided by the user


Question 2: Social Networks using Dictionaries 
-------------
Friendship data is the key construct in creating a social network model. In this question, we will
use dictionaries to store information about a local social network. In a social network, each
person is represented by a node and if two people are friends they have an edge connecting
them. The number of edges that connect to a node is called the degree of the node. In a Social
Network, the degree is simply the number of friends a person has. An example of a social
network is in the image below:
