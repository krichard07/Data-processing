#1. task: Prompt the user to enter a sentence and then print the sentence in uppercase letters.

sentence = input("Please enter a sentence: ").upper()
print(sentence)

#2. task: Prompt the user to enter a paragraph and then count the number of words in the paragraph.

paraghraph = input("Please enter a paragraph: ")
print(len(paraghraph.split()))

#3. task: Prompt the user for a string, and check if all the characters in the string are digits. Output true or false.

digit_or_string = input("Please enter a string: ")
result = all(char.isdigit() for char in digit_or_string)
print(str(result))

#4. task: Prompt the user for a string, and replace all occurrences of the letter "a" with the letter "o".

replaced_words = input("Please enter another string: ").replace("a", "o")
print(replaced_words)

#5. task: Prompt the user to enter their full name and then print their initials. Assume that the user will enter their full name with a space between each name.

initial_name = input("Please enter your full name: ").split(" ")
capitalized_name = "".join([name[0].upper()for name in initial_name])
print(capitalized_name)

# 6. task: Prompt the user for a string, then print its length.

lenght_of_strings = input("Please enter one more string: ")
all_letters = len(lenght_of_strings)
print(f"The length of your string is: {all_letters}")