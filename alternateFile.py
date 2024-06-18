# This version also works, but it is slightly different than main.py
def reverse_string(string: str) -> str:
    """Takes a string as argument and returns a string in reverse order."""
    # This function takes a string as input and returns its reversed version.
    return "".join(reversed(string))


# Initialize an empty list to store the words entered by the user.
reverse_lst = []

# Set a flag to control the loop for adding words.
isLooping = True

# Initialize a counter to keep track of the order of palindrome words printed.
orderingStart = 0

# Print a welcome message to the user.
print("Welcome to the palindrome sorter!")
print("This program will seperate all the palindrome words from a list of given words!")

# Loop until the user enters 'n' to stop adding words.
while isLooping == True:
    # Get a word input from the user and convert it to lowercase.
    word_input = input("What's the word you want to add in the sorting list:\n").lower()

    # Ask the user if they want to add more words and convert the input to lowercase.
    new_words = input("Are there any more words? [Y] for yes and [N] for no.\n").lower()

    # Add the entered word to the list.
    reverse_lst.append(word_input)

    # Check the user's response for adding more words.
    if new_words == "y":
        # Continue the loop if the user enters 'y'.
        continue
    elif new_words == "n":
        # If the user enters 'n', iterate through each word in the list.
        print("List of palindrome words:")
        for index in reverse_lst:
            # Get the current index of the word in the list.
            currentItemIndex = reverse_lst.index(index)

            # Reverse the word using the 'reverse_string' function.
            reversed_word = reverse_string(string=reverse_lst[currentItemIndex])

            # Check if the reversed word is the same as the original word (palindrome).
            if reversed_word == reverse_lst[currentItemIndex]:
                # If it's a palindrome, increment the counter and print the palindrome word.
                orderingStart += 1
                print(f"{str(orderingStart)}. {reversed_word.lower()}")
        # Exit the loop after processing all words.
        break
