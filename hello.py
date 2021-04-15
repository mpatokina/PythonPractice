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
print_prime_factors(100)  
print_prime_factors(0) 
print_prime_factors(39)
print_prime_factors(36)
        