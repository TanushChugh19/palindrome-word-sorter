def reverse_string(string: str) -> str:
    """Takes a string as argument and returns a string in reverse order."""
    # This function reverses a string.
    return "".join(
        reversed(string)
    )  # It flips the letters and joins them back into a string.


# This is a list to store all the words the user enters.
reverse_lst = []

# This acts like a switch to keep the main program running.
isLooping = True

# This keeps track of the order of the palindrome words we find.
orderingStart = 0

# This prints a welcoming message to the user.
print("Welcome to the palindrome sorter!")
print("This program will seperate all the palindrome words from a list of given words!")

# This loop keeps asking for words until the user types 'n'.
while isLooping == True:
    # Asks the user for a word and makes it lowercase.
    word_input = input("What's the word you want to add in the sorting list:\n").lower()
    # Check if the the input has letters or other characters.
    while not word_input.isalpha():
        print("Please enter a valid word (only letters).")
        word_input = input(
            "What's the word you want to add in the sorting list:\n"
        ).lower()
    # Asks the user if they want to add more words and makes their answer lowercase.
    new_words = input("Are there any more words? [Y] for yes and [N] for no.\n").lower()

    # Adds the word to the list.
    reverse_lst.append(word_input)

    # Checks if the user wants to add more words.
    if new_words == "y":
        # If they said 'y', keep going and ask for another word.
        continue
    elif new_words == "n":
        # If they said 'n', it's time to check for palindromes!
        print("List of palindrome words:")
        # Look at each word in the list.
        for index, word in enumerate(reverse_lst):
            # Reverse the word using our function.
            reversed_word = reverse_string(string=word)

            # Check if the reversed word is the same as the original word.
            if reversed_word == word:
                # If they're the same, it's a palindrome!
                orderingStart += 1  # Increase the counter.
                print(
                    f"{orderingStart}. {reversed_word.title()}"
                )  # Print the palindrome with its order.
        # The user wants to stop, so we break out of the loop.
        break
