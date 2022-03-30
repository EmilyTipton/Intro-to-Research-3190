import numpy as np
import numpy as np

def only_evens(list_of_numbers):
    """Take a list of numbers, and return a list of only the even numbers"""

    # This is an empty list that we'll append the even numbers onto
    even_numbers = []

    # Go through each number in the list of numbers
    for number in list_of_numbers:

        # If this number is an even number:
        if number % 2 == 0:

            # Append it to the list of even numbers
            even_numbers.append(number)

    # Then return the number
    return even_numbers
 # Define the function here
    
list_of_numbers = (3, 6, 9, 12, 15, 18, 21, 24)
only_evens(list_of_numbers)
        
    import numpy as np

# Define the function here

def only_evens_numpy(array):
    """Take a list of numbers, and return a list of only the even numbers"""
    
    arr = array[array%2==0]
    
    return arr

list_of_numbers = np.arange(0,50,1)
only_evens_numpy(list_of_numbers)