#1 Python program to calculate the total number of Vowels and Count of each individual vowel in a given string
input_string = "Guvi Geeks Network Private Limited"
vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
input_string = input_string.lower()

total_vowels = 0
for char in input_string:
    if char in vowels:
        vowels[char] += 1
        total_vowels += 1

print("Total number of vowels:", total_vowels)
print("Count of each individual vowel:")
for vowel, count in vowels.items():
    print(vowel, ":", count)

#2 Pyramid of Numbers from 1 to 20 using For loop
for i in range(1, 21):
    print(" " * (20 - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#3 program that takes a string and returns a new string with all the vowels removed

input_string = input("Enter a string: ")
result_string = ""

for char in input_string:
    if char.lower() not in 'aeiou':
        result_string += char

print("String with vowels removed:", result_string)

#4 Program that takes a string and returns the number of unique characters in it
input_string = input("Enter a string: ")
unique_characters = []

for char in input_string:
    if char not in unique_characters:
        unique_characters.append(char)

print("Number of unique characters:", len(unique_characters))

#5 Palindrome

input_string = input("Enter a string: ")

# Reverse the input string
reversed_string = input_string[::-1]

# Check if the input string is equal to its reverse
if input_string == reversed_string:
    print("Is palindrome: True")
else:
    print("Is palindrome: False")
#6 the longest common substring between them

# Taking two strings as input
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Initialize variables to store the longest common substring
longest_length = 0
longest_substring = ""

# Nested loops to iterate through all possible substrings of the two input strings
for i in range(len(string1)):
    for j in range(len(string2)):
        length = 0
        while (i + length < len(string1) and j + length < len(string2)) and (string1[i + length] == string2[j + length]):
            length += 1
        if length > longest_length:
            longest_length = length
            longest_substring = string1[i:i + length]

# Printing the result
print("Longest common substring:", longest_substring)

#7 the most frequent character in string
input_string = input("Enter a string: ")

char_freq = {}

# Count the frequency of each character
for char in input_string:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

# Find the most frequent character
most_frequent_char = max(char_freq, key=char_freq.get)

print("Most frequent character:", most_frequent_char)

#8 Anagram

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Remove spaces and convert to lowercase
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

# Check if lengths are different
if len(string1) != len(string2):
    is_anagram = False
else:
    # Sort both strings and check if they are equal
    is_anagram = sorted(string1) == sorted(string2)

print("Are the strings anagrams?", is_anagram)

#9 program that takes a string and returns the number of words in it

input_string = input("Enter a string: ")

# Initialize word count to 1 to account for the last word
word_count = 1

# Iterate through each character in the input string
for char in input_string:
    # Check if the current character is a space
    if char == " ":
        # If a space is found, increment the word count
        word_count += 1

print("Number of words in the string:", word_count)

