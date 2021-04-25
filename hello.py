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
        


