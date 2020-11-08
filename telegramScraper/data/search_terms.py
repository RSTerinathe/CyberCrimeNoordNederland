from enum import Enum

class Crimes(Enum):
    # Set the values for each Crime.
    # The value is derived by using a bitwise shift
    # When adding a new Crime, increment the number after the '<<' by 1
    ACCOUNTS = 1 << 0
    TEST = 1 << 1
    TEST2 = 1 << 2

    # ALL needs to be twice the last constant - 1
    ALL = (1 << 3) - 1

# Assign the search terms related to a crime in here.
# The search terms should be at least 4 characters
# Put the search terms in alphabetic order

# Account takeovers
account_take_over = [
    'felyx'
]
# Test array
test = [
    'other',
    'term1'
]
# Test array 2
test2 = [
    'test'
]
# Other crimes

# Return the list of all the search terms that are selected
def returnSearchTerms(selected):
    list = []

    # If the ACCOUNTS array is selected, add it to the list returned
    if (selected & Crimes.ACCOUNTS.value) != 0:
        list += account_take_over

    # If the TEST array is selected, add it to the list returned
    if (selected & Crimes.TEST.value) != 0:
        list += test

    # If the TEST array is selected, add it to the list returned
    if (selected & Crimes.TEST2.value) != 0:
        list += test

    return list
