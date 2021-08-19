# PROGRAM STRUCTURE REQUIRED

# """Module docstring"""
#
#
# # imports
# # CONSTANTS
#
# def main():
#     """Function docstring"""
#     # statements...
#     # variables...
#     do_stuff()
#
#
# def do_stuff():
#     """Function docstring"""
#     # statements...
#
#
# main()


# INDEXING
"""
numbers = [1, 2, 3, 4, 5]
indexes of the numbers in the list is from 0-4
numbers[0] = 1
numbers[4] = 5

len(numbers) = 5   - This returns the length without zero
if using this is a for loop it needs to have a -1 after it
to align the indexes only if using length to find the last
element of the list. See below:

numbers = [1, 2, 3, 4, 5]
length = len(numbers)
print(numbers[length])  # this will be incorrect
print(numbers[length-1])

length = len(numbers) can be used in:
for i in range(0, length)  # There is no issue here as 5 is not included

random_number = random.randint(0, 3) - includes 0 and 3

for loop index from 0 - X but doesn't include X
This often works fine when looping through a list
as with numbers = [1, 2, 3, 4, 5] the first element is 0
and the last is 4, so the loop range(0, 5) includes the
index 0, 1, 2, 3, 4

numbers = [1, 2, 3, 4, 5]
for i in range(0, 5):    # loops through 0, 1, 2, 3, 4 (not 5)
    print(numbers[i])
>> 1, 2, 3, 4, 5

"""

# numbers = [1, 2, 3, 4, 5]
#
# for i in range(0, 5):
#     print(numbers[i])
#
# length = len(numbers)
# # print(numbers[length])  # this will be incorrect
# print(numbers[length-1])


# SLICING STRINGS, TUPLES AND LISTS
"""
Notes:
- The first element of a 'string' is 0, like in a list[]
- Slicing includes up to but not the last number:

text = "Programming"
print(text[0:4])  # this prints index 0, 1, 2, 3 (not 4)
>> Prog

"""

# text = "Programming is fun"
#
# print(text[0:4])
# print(text[4:7])
# print(text[0:-4])
# print(text[0:-4:2])
# print(text[0:len(text)])
# print(text[0:-1])


# METHODS
"""
The object is separated from the method by a dot .
object.method() etc
.upper() - changes all to upper case
.lower() - changes all to lower case
.title() - changes first letters to upper case

Test if a string Is Something with these methods:
.isdigit()
.isalpha()
.isupper()

phone_number = input("Phone: ")
if not phone_number.isdigit():
    print("Invalid phone number")
    
name = input("Name: ")
if not name.isalpha():
    print("Alphabetical only")
    
expression = input("Say something: ")
if expression.isupper():
    print("No need to shout")
"""

# text = "Programming is fun"
# print(text.upper())
# print(text.lower())
# print(text.title())
# print("Enter a number ({}-{}): ".format(1, 10))


# FORMATTING and ESCAPE CHARACTERS
"""
Some snippets of formatting that can save time to remember

print("Enter a number ({}-{}): ".format(1, 10))

drink = coffee
print(f"Enjoy your {drink}")  - the f"..." enables variable into the {}

print(f"Enjoy your {drink:12}!")  - allocates 12 spaces to name

print(f"The average score was {score_average:.3f}")   :.3f is to 3 decimal places
print(f"The average score was {score_average:.4f}")   :.4f is to 3 decimal places

print("Hello, ", name, sep="")   # this changes the default space after commas to none
print("Hello", end="-")          # this adds that character "-" as a separator, can be any
                                   character with any amount of spaces
>> H-e-l-l-o-

\n = new line
\t = tab
"""

# print("JCU Douglas Campus\nTownsville\n\tQLD")
# print('JCU Douglas Campus\nTownsville\n\tQLD')


# FILES ANDS EXCEPTIONS

"""
out_file = open("text.txt", 'w')  # The program sends data out and writes to a new file
in_file =  open(FILENAME, 'r')   # The program reads data from a file
in_file =  open(FILENAME)       # The open function is set to mode 'r' by default if not specified

text = in_file.read()

out_file.close()
in_file.close()   

"""
# Example: reading from an existing file testfile.txt
# FILENAME = "testfile.txt"
# in_file = open(FILENAME)
# text = in_file.read()
# in_file.close()
# print(text)

# # EXAMPLE READ A SECRET NUMBER FROM A FILE AND USE IT IN A VARIABLE
# # Step 1: Create the file object with open() and read from an existing file and assign it a variable
# in_file = open("secret.txt", "r")
# # Step 2: Read the file. Store it in a variable
# # All text files are string format, numbers need converting to int type
# secret = int(in_file.read())
# # Step 3: Close the file. Avoid data corruption from leaving files open
# in_file.close()
#
# print("Guess a number between 1 and 10")
# guess = int(input("? "))
# while guess != secret:
#     print("Keep guessing")
#     guess = int(input("? "))
# print("You got it!")

# EXAMPLE LOOPING OVER THE LINES IN A FILE
# Python's for loop reads each line of the file, it knows the length
# Note this prints a gap line between each line as it has a default \n
# in_file = open("testfile.txt", "r")
# for line in in_file:
#     print(line)
# in_file.close()
#
# THIS one will remove the default \n from the end of each line
# in_file = open("testfile.txt", "r")
# for line in in_file:
#     print(line, end="")
# in_file.close()
#
# BUT the better way to do it is with the method .strip()
# in_file = open("testfile.txt", "r")
# for line in in_file:
#     print(line.strip())
# in_file.close()

# EXAMPLE WRITING TO A FILE WITH MODE "a" APPEND
# out_file = open("testfile.txt", "a")
# for i in range(5):
#     print("\nname", file=out_file, end="")
# out_file.close()

# EXAMPLE CREATING A FILE AND WRITING TO IT WITH MODE 'w' WRITE
# filename = "this_is_a_name.txt"
# out_file = open(filename, 'w')
# gross_income = 1000
# net_income = gross_income - 0.31*gross_income
# print(f"${net_income:.2f}", file=out_file)
# out_file.close()


numbers = [10, 20, 30, 40]

print(numbers[1])
print(numbers[1:4])
print(numbers[1:2:3])







