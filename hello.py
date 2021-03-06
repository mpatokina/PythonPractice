print("Hi, Python!")
def lucky_number(name):
    number = len(name)*9
    print("Hello " + name + ". Your lucky number is " + str(number))
lucky_number("Maria")
lucky_number("Ivan")    
lucky_number("Lidia")
lucky_number("Konstantin")

def area_rectangle(a,b):
    area = a*b
    print("Rectangle area is " + str(area))
area_rectangle(4,6)   

def convert_seconds(seconds):
    days = seconds // 86400
    hours = (seconds - days*86400) // 3600
    minutes = (seconds - days*86400 - hours*3600) // 60
    remaining_seconds = seconds - days*86400 - hours*3600 - minutes*60
    #print(days, hours, minutes, remaining_seconds)
    print("Days: " + str(days) + " | Hours: " + str(hours) + " | Minutes: " +  str(minutes) + " | Seconds: " + str(remaining_seconds))
convert_seconds(4500)    
    #return hours, minutes, remaining_seconds
#hours, minutes, seconds = convert_seconds(20000)
#print (hours, minutes, seconds)

def month_days(month, days):
    print(month + " has " + str(days) + " days.")
month_days("June", 30)    
month_days("July", 31)

def circle_area(radius):
    pi = 3.14
    area = pi*(radius**2)
    print(area)
circle_area(5)    

def order_numbers(number1, number2):
    if number1 > number2:
        return number2, number1
    else:
        return number1, number2

smaller_number, bigger_number = order_numbers(100, 90)
print(smaller_number, bigger_number)   

def lucky_number2(name):
    number = len(name)*9
    message = "Hello " + name + ". Your lucky number is " + str(number)
    return message
print(lucky_number2("Tim"))   

def convert_distance(miles):
    km = 1.6*miles
    return km
distance_miles = 55
distance_km = convert_distance(distance_miles)
print("My distance is " + str(distance_km) + " km.")

print(10<1)

print(1 != 2)

print("cat" > "Cat")

print(not 42 == 24)

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long.")    
    else:
        print("Valid username.")    
hint_username("ok") 
hint_username("dog")  
hint_username("verylongusername")

def is_even(number):
    if number % 2 == 0:
        return True
    return False
print(is_even(100)) 
print(is_even(99))   

def number_group(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    return "Zero"
print(number_group(10))  
print(number_group(-5))  
print(number_group(0))   

# While Loops
x=0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x+1
print("x=" + str(x))   

def attempt(n):
    x=1
    while x <= n:
        print("Attempt " + str(x))
        x +=1
    print("Done")
attempt(7) 

def count_down(start_number):
    current = start_number
    while current > 0:
        print(current)
        current -=1
    print("Zero!")
count_down(5)  

def print_range(start, end):
    n = start
    while n <= end:
        print(n)
        n += 1
print_range(1,5)  

def is_power_of_two(n):
    while n > 1 and n % 2 ==0:
        n = n / 2
    if n == 1:
        return True    
    return False
print(is_power_of_two(0)) 
print(is_power_of_two(1)) 
print(is_power_of_two(2))  
print(is_power_of_two(16)) 
print(is_power_of_two(9)) 

# this function returns the sum of all the divisors of a number, without including it.
def sum_divisors(n):
    sum = 0
    divisor = 1
    while divisor < n:
        if n % divisor == 0:
            sum = sum + divisor
        divisor +=1
    return sum
print(sum_divisors(0))
print(sum_divisors(3))   
print(sum_divisors(36)) 
print(sum_divisors(102))    

#The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5. 
# An additional requirement is that the result is not to exceed 25, which is done with the break statement.
def multiplication_table(number):
    multiplier = 1
    while multiplier <= 5:
        product = number * multiplier
        if product > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(product))
        multiplier +=1
 
multiplication_table(1) 
multiplication_table(3) 
multiplication_table(5) 
multiplication_table(8) 
multiplication_table(0) 
multiplication_table(25)   

# This function print all the prime factors of a number.

def print_prime_factors(number):
    factor = 2
    while factor <= number:
        if number % factor == 0:
            print(factor)
            number = number / factor
        else:
            factor += 1
    return "Done"        
print_prime_factors(5)  
print_prime_factors(0) 
print_prime_factors(37)
print_prime_factors(36)

# For Loops
for x in range(5): # 0,1,2,3,4
    print(x)

# this function returns the sum of all the squares of numbers between 0 and x (not included). 
def square(n):
    return n*n
def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum
print(sum_squares(10))  # s/be 285 

friends = ['Alex', 'Zoe', 'Pat']
for friend in friends:
    print("Hi " + friend)

# calculating sum and average
values = [8, 11, 14, 17]
sum = 0
length = 0
for value in values:
    sum += value
    length +=1
print("Sum: " + str(sum) + " | Average: " + str(sum/length)) 

# calculating product from 1 to 10
product = 1
for n in range(1,10):
    product = product*n
print(product) 

# factorial of 4 (4!)
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result*i
    return result
print(factorial(4))  # should return 24
print(factorial(5))  # should return 120

# convert to Celsius table
def to_celsius(x):
    return (x-32)*5/9
for x in range(0, 101, 10): #starts at 0, ends at 100, jumps by 10
    print(x, to_celsius(x))  

# Nested for Loops

#dominoes
for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()  

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns'] 
for home_team in teams:
     for away_team in teams:
         if home_team != away_team :
             print(home_team + " vs " + away_team) 

def is_valid(user):
    if len(user) >= 3:
        return True
    else:
        return False    
def validate_users(users):
    for user in [users]:
        if is_valid(user):
            print(user + " is valid")
        else:
            print(user + " is invalid")
validate_users("purplecat") 
validate_users("mu")            
     
# print the first 10 factorials (from 0 to 9) with the corresponding number
def factorial(n):
    result = 1
    for n in range(1, n+1):
        result = result*n
    return result
for n in range(0, 11):  
    print(n, factorial(n))  

# print the first 10 cube numbers (x**3) 
for x in range(1, 11):
    print(x**3)      

# print multiples of 7 from 0 to 100
for x in range(0, 101, 7):
    print(x)  

# factorial using recursion
def factorial(n):
    if n < 2:
        return 1
    return n*factorial(n-1) 
print(factorial(4))  

# sum of positive numbers
def sum_positive_numbers(n):
    if n < 1:
        return 0
    return n + sum_positive_numbers(n-1)
print(sum_positive_numbers(3)) # s/be 6
print(sum_positive_numbers(5)) # s/be 15   

# function returns whether the number is a power of the given base
def is_power_of(number,base):
    if number < base: # Base case: when number is smaller than base
        return number == 1 # If number is equal to 1, it's a power (base**0)
    return is_power_of(number/base, base) # Recursive case: keep dividing number by base 
print(is_power_of(8,2)) #s/be True
print(is_power_of(64,4)) #s/be True
print(is_power_of(70,10)) #s/be False

# Module 3 Graded Assessment

# print out the numbers 1 through 7

number = 1
while number <= 7:
	print(number, end=" ")
	number +=1
 
# print out each letter of a word on a separate line

def show_letters(word):
    for letter in word:
        print(letter)
show_letters(" Hello") 

# function digits(n) that returns how many digits the number has
def digits(n):
    count = 0
    if n == 0:
        return 1
    while n > 0:
        count += 1
        n = n//10
    return count
print(digits(100)) 
print(digits(25)) 
print(digits(9))
print(digits(0)) 

# This function prints out a multiplication table 
# (where each number is the result of multiplying the first number of its row by the number at the top of its column)

def multiplication_table(start, stop):
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            print(str(x*y), end = " ")
        print()        
multiplication_table(1, 3) 

# The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. 

def counter(start, stop):
    x = start
    if x > stop:
        return_string = "Counting down: "
        while x >= stop:
            return_string +=  str(x)
            if x > stop:
                return_string += ", "
            x = x - 1
    else:
        return_string = "Counting up: "
        while x <= stop:
            return_string += str(x)
            if x < stop:
                return_string += ", "
            x = x + 1
    return return_string        
print(counter(1, 5)) 
print(counter(7, 1))
print(counter(7, 7))                

# The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2, up to and including the maximum that's passed into the function.

def even_numbers(maximum):
    return_string = ""
    for x in range(2, maximum+1, 2):
        return_string += str(x) + " "
    return return_string.strip()
print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed  

# How does this function need to be called to print yes, no, and maybe as possible options to vote for?
def votes(params):
	for vote in params:
	    print("Possible option:" + vote)
votes(['Yes', 'No', 'Maybe'])        

# Week 4
#Strings

name = "Maria"
print(name[0])
print(name[4])
print(name[-3])
print(name[1:3])
print(len(name))

fruit = "Pineapple"
print(fruit[:4])
print(fruit[4:])

message = "A kong string"
new_message = message[0:2] + "l" + message[3:]
print(new_message)


pets = "Cats & Dogs"
print(pets.index("&"))
print(pets.index("C"))
print(pets.index("Dogs"))
print(pets.index("s")) # shows only the first one

print("Dragons" in pets)
print("Dogs" in pets)

print("Mountains".upper())
print("Mountains".lower())

answer = "YES"
if answer.lower() == "yes":
    print("User said yes")

print("Electricity".count("t"))  

print("Forest".endswith("rest"))

print("Forest".isnumeric())

print("12345".isnumeric())

print(int("123") + int("567"))

print("@".join(["name", "hotmail.com"]))

print("This is another example".split())

name = "Maria"
number = len(name) * 3
print("Hello, {} your lucky number is {}".format(name, number))

print("Your lucky number is {number}, {name}".format(name=name, number=len(name)*3))

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

def to_celsius_new(x):
    return (x-32)*5/9
for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius_new(x))) 
    
def double_word(word):
    return word*2 + str(len(word)*2)
print(double_word("hello")) 

def first_last(message):
    if len(message) == 0:
        return True
    elif message[0] == message[-1]:
        return True
    else:
        return False
print(first_last("else"))   
print(first_last("Mom"))    
print(first_last(""))    

word = "abcdefghijklmnopqrstuvwxyz"
print(word.index('p'))

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return result.upper()
print(initials("local area network"))   

def student(name, grade):
    return "{} received {}% on the exam".format(name, grade)
print(student("Anna", 99))   

def is_polindrome(input_string):
    input_string = input_string.lower()
    new_string = ""
    reverse_string = ""
    for x in input_string:
        if x != " ":
            new_string = new_string + x
            reverse_string = x + reverse_string
    if new_string == reverse_string:
        return True  
    return False
print(is_polindrome("Never Odd or Even"))  
print(is_polindrome("abc"))     
print(is_polindrome("kayak"))

def nametag(first_name, last_name):
    return ("{} {:.1s}.".format(first_name, last_name))
print(nametag("Anna", "Smith")) 

def replace_ending(sentence, old, new):
    if sentence.endswith(old):
       # i = len(sentence)
       # l = len(old)
       # new_sentence = sentence[0: i-l] + new
        i = len(old)
        new_sentence = sentence[:-i] + new
        return new_sentence
    return sentence
print(replace_ending("it's raining cats and cats", "cats", "dogs")) 
print(replace_ending("I have a cat", "Cat", "Dog"))
print(replace_ending("I have a Cat", "Cat", "Dog"))   

def string_repeats_letters(string):
    for i in range (0, len(string) - 1):
        for j in range (i+1, len(string)):
            if string[i] == string[j]:
                return True
    return False
print(string_repeats_letters("hello"))
print(string_repeats_letters("bye")) 
print(string_repeats_letters("abcdefghijklmnopqrstuvwxyz"))
print(string_repeats_letters("abcdefga"))      

for i in range (1, 100):
    if (i % 3 == 0) and (i % 5 == 0):
        print("buzzfuzz")
    elif (i % 3 == 0):
        print("buzz")
    elif (i % 5 == 0):
        print("fuzz")
    else:
        print(i)

def is_leap(year):
    leap = False
    if (year % 400 == 0):
        leap = True
    elif (year % 100 == 0):
        leap = False
    elif (year % 4 == 0):
        leap = True
    print(leap)
is_leap(1900) 
is_leap(2000)  
is_leap(1700) 
is_leap(2000)
is_leap(2021)     

#Lists
x = ["Now", "we", "are", "cooking!"]
print(type(x))
print(x)
print(len(x))
print(len(x[3]))
print("are" in x)
print("you" in x)
print(x[-1])
print(x[0])
print(x[1:3])
print(x[:2])
print(x[2:])

def get_word(sentence, n):
    if n > 0:
        word = sentence.split()
        if n <= len(word):
            return (word[n-1])
    return ("")
print(get_word("Now we are cooking!", 4)) 
print(get_word("Now we are cooking!", 5)) 
print(get_word("Now we are cooking!", 0))    


fruits = ["Pineapple", "Banana", "Apple"]
fruits.append("Kiwi")
print(fruits)
fruits.insert(0, "Orange")
print(fruits)
fruits.remove("Apple")
print(fruits)
fruits.pop(1)
print(fruits)
fruits[1] = "Strawberry"
print(fruits)

def skip_elements(elements):
    new_list = []
    for i in range (len(elements)):
        if (i % 2 == 0):
            new_list.append(elements[i])
        i += 1
    return new_list
print(skip_elements(["a", "b", "c", "d", "e", "f"])) 
print(skip_elements([]))    

# Iterating over Lists and Tuples
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

def skip_elements2(elements):
    new_elements = []
    for index, element in enumerate(elements):
        if (index % 2 == 0):
            new_elements.append(element)
    return new_elements
print(skip_elements2(["a", "b", "c", "d", "e", "f"]))       

#List Comprehensions
multiples = []
for x in range(1, 11):
    multiples.append(x*7)
print(multiples)  

multiples2 = [x*7 for x in range(1, 11)]
print(multiples2)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range(0,101) if x % 3 == 0]
print(z)

def odd_numbers(n):
    return [x for x in range(0, n+1) if x % 2 != 0]
print(odd_numbers(17))   


#Practice Quiz: Lists (Week 4)
#Question 1
#Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks in the code using any of the methods you???ve learned thus far, like a for loop or a list comprehension.
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

new_filenames = []
for filename in filenames:
    if filename.endswith(".hpp"):
        l = len(filename) - 4
        filename = filename[:l] + ".h" 
        new_filenames.append(filename)
    else:
        new_filenames.append(filename)     

print(new_filenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


#Question 2
#Let's create a function that turns text into pig latin: a simple text transformation that modifies each word moving the first character to the end and appending "ay" to the end. For example, python ends up as ythonpay.
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    new_word = word[1:] + word[0] + "ay "
    # Turn the list back into a phrase
    say += new_word
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"



#Question 3
#The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
#For example: 
#640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
#755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
#Fill in the blanks to make the code convert a permission in octal format into a string format.

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for digit in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digit >= value:
                result += letter
                digit -= value
                
            else:
                result += "-"
                
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------
print(octal_to_string(777)) # Should be rwxrwxrwx
print(octal_to_string(111)) # Should be --x--x--x
print(octal_to_string(222)) # Should be -w--w--w-
print(octal_to_string(444)) # Should be r--r--r--

# Question 5
# The group_list function accepts a group name and a list of members, and returns a string with the format: group_name: member1, member2, ??? For example, group_list("g", ["a","b","c"]) returns "g: a, b, c". Fill in the gaps in this function to do that.
def group_list(group, users):
  members = ""
  l=0
  for user in users:
    members += user + ", "
    l=len(members)
  return "{}: {}".format(group, members[0:l-2])

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

# Question 6
#The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, and prints the sentence "Guest is X years old and works as __." for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer. Fill in the gaps in this function to do that. 
def guest_list(guests):
	for guest in guests:
		name, age, job = guest
		print("{} is {} years old and works as {}".format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

# Dictionaries

x = {}
print(type(x))


# The "toc" dictionary represents the table of contents for a book. Fill in the blanks to do the following: 	# 
# 1) Add an entry for Epilogue on page 39. 	2) Change the page number for Chapter 3 to 24. 	
# 3) Display the new dictionary contents. 	
# # 4) Display True if there is Chapter 5, False if there isn't.

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39
toc["Chapter 3"] = 24
del toc["Introduction"]
print(toc)
print("Chapter 5" in toc)

# Iterating over the contents of a dictionary

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extention in file_counts:
    print(extention)

for value in file_counts.values():
    print(value)    

for ext, amount in file_counts.items(): # items method
    print("There are {} files with the.{} extention.".format(amount, ext))   

print(file_counts.keys())   

print(file_counts.values())

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for ext, amount in cool_beasts.items():
    print("{} have {}".format(ext, amount))

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result
print(count_letters("hello, how are you?"))            
        
wardrobe = {"shirt":["red", "blue", "white"], "jeans":["blue", "black"]}
for outfit, colors in wardrobe.items():
    for color in colors:
        print("{} {}".format(color, outfit))

# 1
# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
    emails = []
    for domain, names in domains.items():
        for name in names:
            emails.append("{}@{}".format(name, domain))
    return emails    
print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

#5
# The add_prices function returns the total price of all of the groceries in the  dictionary. Fill in the blanks to complete this function.

def add_prices(basket):
    total = 0
    for value in basket.values():
        total += value
    return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

# 2. The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user not in user_groups:
				user_groups[user] = []
			user_groups[user].append(group)	
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

# Mod4 assessment

# 1 The format_address function separates out parts of the address string into new strings: house_number and street_name, and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by the street name which may contain numbers, but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive".

def format_address(address_string):
    new_address = address_string.split()
    house = new_address.pop(0)
    street = ""
    for part in new_address:
        street += part + " "
    return ("house number {} on street {}".format(house, street))

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

# 2 The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day".

def highlight_word(sentence, word):
	return sentence.replace(word, word.upper())

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

# 3 A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. 
# After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. 
# Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

def combine_lists(list1, list2):
  new_list = []
  list1.reverse()
  new_list = list2 + list1
  return new_list
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

# 4 

def squares(start, end):
	return [ value ** 2 for value in range(start, end + 1) ]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 5 
def car_listing(car_prices):
  result = ""
  for name, price in car_prices.items():
    result += "{} costs {} dollars".format(name, price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

# 6
# Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, but Rory's list has more current information about the number of guests. Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. Then print the resulting dictionary.

def combine_guests(guests1, guests2):
  guests2.update(guests1)
  return guests2

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

# Week 5 OOP

# 2

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    temp = me.apples       
    me.apples = you.apples
    you.apples = temp
    return you.apples, me.apples
def exchange_ideas(you, me):
    you.ideas = you.ideas + me.ideas
    me.ideas = you.ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


#3
# The City class has the following attributes: name, country (where the city is located), elevation (measured in meters), and population (approximate, according to recent statistics). Fill in the blanks of the max_elevation_city function to return the name of the city and its country (separated by a comma), when comparing the 3 defined instances for a specified minimal population. For example, calling the function for a minimum population of 1 million: max_elevation_city(1000000) should return "Sofia, Bulgaria". 

class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	highest_elevation = 0
	
# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	return_city = City()
	if (city1.population >= min_population) and (city1.elevation > highest_elevation):
		return_city = city1
		highest_elevation = city1.elevation
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if (city2.population >= min_population) and (city2.elevation > highest_elevation):
		return_city = city2
		highest_elevation = city2.elevation
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if (city3.population >= min_population) and (city3.elevation > highest_elevation):
		return_city = city3
		highest_elevation = city3.elevation

	#Format the return string
	if return_city.name:
		return ("{}, {}".format(return_city.name, return_city.country))
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""

#5
class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"

class Piglet:
    def speak(self):
        print("oink oink")
hamlet = Piglet()
hamlet.speak()

class Piglet:
    name = "piglet"
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()
petunia = Piglet()
petunia.name = "Petunia" 
petunia.speak()       

class Piglet:
    years = 0
    def pig_years(self):
        return self.years * 18
piggy = Piglet()
print(piggy.pig_years())  
piggy.years = 2
print(piggy.pig_years())    

# Constructors


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
jonagold = Apple("red", "sweet")
print(jonagold.color) 

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return ("hi, my name is {}".format(self.name))  
some_person = Person("Anna")       
print(some_person.greeting())   

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor) 
jonagold = Apple("red", "sweet") 
print(jonagold)   

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        lidia = Person("Lidia")
        print("Hello! My name is {name}".format(name = self.name))

# Classes and Methods
# lab
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top 
        self.current = current
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < self.top:
            self.current += 1
        else:
            self.curret = self.top
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > self.bottom:
            self.current -= 1
        else:
            self.current = self.bottom
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        
    def __str__(self):
        return "Current floor: {}".format(self.current)


elevator = Elevator(-1, 10, 0)

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

elevator.go_to(5)
print(elevator)

# Code Reuse
# Inheritance

class Fruit: #Parent
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
class Apple(Fruit):
    pass
class Grape(Fruit):
    pass
granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")
print(granny_smith.flavor)
print(carnelian.color)

class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name = self.name, sound = self.sound))
class Piglet(Animal):
    sound = "Oink!" 
hamlet = Piglet("Hamlet")
hamlet.speak()
class Cow(Animal):
    sound = "Mooooo!"
milky = Cow("Milky White")  
milky.speak()     

class Clothing:
    material = ""
    def __init__(self, name):
        self.name = name
    def checkmaterial(self):
        print("This {} is made of {}".format(self.name, self.material)) 
class Shirt(Clothing):
    material = "cotton"    
polo = Shirt("Polo") 
polo.checkmaterial()   

class Clothing:
  stock={ 'name': [],'material' :[], 'amount':[]}
  def __init__(self,name):
    material = ""
    self.name = name
  def add_item(self, name, material, amount):
    Clothing.stock['name'].append(self.name)
    Clothing.stock['material'].append(self.material)
    Clothing.stock['amount'].append(amount)
  def Stock_by_Material(self, material):
    count=0
    n=0
    for item in Clothing.stock['material']:
      if item == material:
        count += Clothing.stock['amount'][n]
        n+=1
    return count

class shirt(Clothing):
  material="Cotton"
class pants(Clothing):
  material="Cotton"
  
polo = shirt("Polo")
sweatpants = pants("Sweatpants")
polo.add_item(polo.name, polo.material, 4)
sweatpants.add_item(sweatpants.name, sweatpants.material, 6)
current_stock = polo.Stock_by_Material("Cotton")
print(current_stock)


# Python Modules
import random
x = random.randint(1,10)
print(x)

import datetime
now = datetime.datetime.now()
print(type(now))
print(now)
print(now.year)
print(now + datetime.timedelta(days=90))

# lab
class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category = "reptile"

print(Turtle.category)

class Snake(Animal):
    category = "reptile"

class Bear(Animal):
    category = "mammal"    

class Zoo:
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class
bear = Bear("Bear")

zoo.add_animal(turtle)
zoo.add_animal(snake)
zoo.add_animal(bear)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category
print(zoo.total_of_category("mammal")) #how many zoo animal types in the reptile category

# Final assessment Week 5

#In this exercise, we'll create a few classes to simulate a server that's taking connections from the outside and then a load balancer that ensures that there are enough servers to serve those connections.
#To represent the servers that are taking care of the connections, we'll use a Server class. Each connection is represented by an id, that could, for example, be the IP address of the computer connecting to the server.
#For our simulation, each connection creates a random amount of load in the server, between 1 and 10.

#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        if connection_id in self.connections:
            del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for load in self.connections.values():
            total += load
        
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

server = Server()
server.add_connection("192.168.1.1")

print(server.load())

server.close_connection("192.168.1.1")
print(server.load())

class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server
        server.add_connection(connection_id)
        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer
        for server in self.servers:
            if connection_id in server.connections:
                server.close_connection(connection_id)
                break
    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total_load = 0
        total_server = 0
        for server in self.servers:
            total_load += server.load()
            total_server += 1
            
        return total_load/total_server
    

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            self.servers.append(Server())
            
        #pass
    

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))        

l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

l.servers.append(Server())
print(l.avg_load())

l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

for connection in range(20):
    l.add_connection(connection)
print(l)

print(l.avg_load())

# Week 6

# sort list
numbers = [5,4,2,7,1]
numbers.sort()
print(numbers)

names = ["Carlos", "Ray", "Alex", "Kelly"]
print(sorted(names))
print(names)
print(sorted(names, key=len))

# Practice

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout" and event.user in machines[event.machine]:
        machines[event.machine].remove(event.user)
        
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
        user_list = ", ".join(users)
    print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)


# Final Assignment

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    new_file_contents = "".join((char if char.isalpha() else " ") for char in file_contents).lower().split()
    filter  = [word for word in new_file_contents if word not in list(punctuations) + uninteresting_words]
    frequencies = {word: file_contents.count(word) for word in filter}
    
   
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

    
# another version
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE   

    words = file_contents.split()
    cleaned_file_contents = []

    
    for word in words:
        if word not in punctuations:
            cleaned_file_contents += word
            
    return cleaned_file_contents

    lower_file_contents = cleaned_file_contents.lower()
     
    frequencies = {}
    
    for word in lower_file_contents:
        if word not in uninteresting_words:
            if word not in frequencies:
                frequencies[word] = 1
            else:    
                frequencies[word] += 1
                
    return frequencies

