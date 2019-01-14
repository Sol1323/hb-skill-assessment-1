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

