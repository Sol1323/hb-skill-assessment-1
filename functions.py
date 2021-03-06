"""
Skills function assessment.

Please read the instructions first. Your solutions should
go below this docstring.

"""


def is_hometown(town, hometown = "Canovanas"):
   """Given a string, return a bool if it matches hometown.


   Examples:
    
    If you got this string as input: "Aibonito"
    You should return: False
    
    
    Another example input: "Canovanas"
    Return value should be: True

   """

   return town == hometown


print("----is_hometown test-----")

print(is_hometown("Aibonito") == False)
print(is_hometown("Canovanas") == True)



def get_fullname(first_name, last_name):
   """Given a first and last name, return one string for fullname


   Examples:
    
    If you got this strings as input: "Sol", "Beniquez"
    You should return: "Sol Beniquez"
    
    
    Another example input: "Ada", "Lovelace"
    Return value should be: "Ada Lovelace"

   """
   
   fullname = first_name + " " + last_name
   
   return fullname


print("----get_fullname test-----")

print(get_fullname("Sol", "Beniquez") == "Sol Beniquez")
print(get_fullname("Ada", "Lovelace") == "Ada Lovelace")



def greeting(hometown, first_name, last_name):
   """Given 3 strings, return a greeting depending on the hometown


   Examples:
    
    If you got this strings as input: "Canovanas", "Sol", "Beniquez"
    You should return: "Hi, Sol Beniquez, we're from the same place!"
    
    
    Another example input: "London", "Ada", "Lovelace"
    Return value should be: "Hi Ada Lovelace, I'd like to visit London!"

   """

   fullname = get_fullname(first_name, last_name)
   
   if is_hometown(hometown):
      print("Hi, {}, we're from the same place!".format(fullname))
   else: 
      print("Hi {}, I'd like to visit {}!".format(fullname, hometown))


print("----greeting test-----")

print(greeting("Canovanas", "Sol", "Beniquez")) 
print(greeting("London", "Ada", "Lovelace"))



def is_berry(fruit):
   """Given 1 string, return a bool if it is a berry.


   Examples:
    
    If you got this string as input: "strawberry"
    You should return: True
    
    If the input varies in upper & lower cases 
    (not case sensitive): "sTraWberry"
    You should return: True
    
    Another example input: "apple"
    Return value should be: False

   """

   berries = ["strawberry", "raspberry", "blackberry", "currant"]

   fruit = fruit.lower()

   return fruit in berries


print("----is_berry test-----")

print(is_berry("strawberry") == True)
print(is_berry("sTraWberry") == True) 
print(is_berry("apple") == False)
print(is_berry("BlackBerry") == True)



def shipping_cost(fruit):
   """Given 1 string, return shipping cost for fruit.
   

   Examples:
    
    If you got this string as input: "strawberry"
    You should return: 0
    
    If the input varies in upper & lower cases 
    (not case sensitive): "sTraWberry"
    You should return: 0
    
    Another example input: "apple"
    Return value should be: 5

   """

   shipping_cost = 5

   if is_berry(fruit):
      shipping_cost = 0

   return shipping_cost


print("----shipping_cost test-----")

print(shipping_cost("strawberry") == 0)
print(shipping_cost("sTraWberry") == 0) 
print(shipping_cost("apple") == 5)
print(shipping_cost("BlackBerry") == 0)


def get_all_fruits(fruit, fruits):
   """Given 1 string and a list return a new list
   with the fruit added to the end 
   
   Returned list should be all lowercase. Assume given list is lowercase.


   Examples:
    
    If you got this string and list as input: "strawberry", 
    ['apple', 'banana', 'orange']
    You should return: ['apple', 'banana', 'orange', 'strawberry']
    
    If the input varies in upper & lower cases: "sTraWberry",
    ['apple', 'banana', 'orange']
    You should return: ['apple', 'banana', 'orange', 'strawberry']
    
    If the input is already on the list: "apple",
    ['apple', 'banana', 'orange']
    Return value should be: ['apple', 'banana', 'orange', 'apple']

   """

   fruit = fruit.lower()
   fruits.append(fruit)
   all_fruits = fruits[::]

   return all_fruits


print("----get_all_fruits test-----")

print(get_all_fruits("strawberry", ['apple', 'banana', 'orange']) == ['apple', 'banana', 'orange', 'strawberry'])
print(get_all_fruits("sTraWberry", ['apple', 'banana', 'orange']) == ['apple', 'banana', 'orange', 'strawberry']) 
print(get_all_fruits("apple", ['apple', 'banana', 'orange']) == ['apple', 'banana', 'orange', 'apple'])



def calculate_price(base_price, state, tax = .05):
   """Given 2 integers and a string. 
   Return a string total cost with fees and tax included.

   Arguments format example: 
      base_price = 5.25 (limit to two digit-decimal)
      state = CA (limit to two letter uppercase)
      tax = .05 (limit to two digit-decimal) 


   Examples:
    
    If you got this integers and string as input: 
    10.25, 'CA', 0.07
    You should return: "$11.30"

    If you got this integers and string as input: 
    50.75, 'MA', .06
    You should return: "$54.80"

    If you got this integers and string as input: 
    99.99, 'PA', .06
    You should return: "$107.99"

    If there is no tax argument default should be %5: 
    100.00, 'NY'
    You should return: "$105.00"

   """  

   total_cost = base_price * (tax + 1)

   if state == "CA":
      total_cost *= 1.03
   elif state == "PA":
      total_cost += 2.00
   elif state == "MA" and base_price <= 100:
      total_cost += 1.00 
   
   return "${:.2f}".format(total_cost)


print("----calculate_price-----")

print(calculate_price(10.25, 'CA', .07) == "$11.30")
print(calculate_price(50.75, 'MA', .06) == "$54.80") 
print(calculate_price(101.25, 'MA', .06) == "$107.33")
print(calculate_price(99.99, 'PA', .06) == "$107.99") 
print(calculate_price(100.00, 'NY') == "$105.00")


###############################################################################


# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

   # 1.  Write a function that takes a town name as a string and returns
   #     `True` if it is your hometown, and `False` otherwise.

   # 2.  Write a function that takes a first and last name as arguments and
   #     returns the concatenation of the two names in one string.

   # 3.  Write a function that takes a home town, a first name, and a last name
   #     as arguments, calls both functions from part (a) and (b) and prints
   #     "Hi, 'full name here', we're from the same place!", or "Hi 'full name
   #     here', I'd like to visit 'town name here'!" depending on what the function
   #     from part (a) evaluates to.

   # 4.  Write a function, `is_berry()`, which takes a fruit name as a string
   #     and returns a boolean if the fruit is a "strawberry", "raspberry",
   #     "blackberry", or "currant."

   # 5.  Write another function, shipping_cost(), which calculates shipping
   #     cost by taking a fruit name as a string and calling the `is_berry()`
   #     function within the `shipping_cost()` function. Your function should
   #     return 0 if is_berry() == True, and 5 if is_berry() == False.

   # 6.  Make a function that takes in a fruit name and a list of fruits. It should
   #     return a new list containing the elements of the input list, along with
   #     given fruit, which should be at the end of the new list.

   # 7.  Write a function calculate_price to calculate an item's total cost by
   #     adding tax and any fees required by state law.

   #     Your function will take as parameters (in this order): the base price of
   #     the item, a two-letter state abbreviation, and the tax percentage (as a
   #     two-digit decimal, so, for instance, 5% will be .05). If the user does not
   #     provide a tax rate it should default to 5%.

   #     CA law requires stores to collect a 3% recycling fee, PA requires a $2
   #     highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
   #     items with a base price of $100 or less and $3 for items over $100. Fees are
   #     added *after* the tax is calculated.

   #     Your function should return the total cost of the item, including tax and
   #     fees.

